
#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"
#include "ns3/flow-monitor-module.h"
#include "ns3/ipv4-global-routing-helper.h"
#include "ns3/ipv4-static-routing-helper.h"
#include "ns3/ipv4-tlb-probing.h"
#include "ns3/link-monitor-module.h"
#include "ns3/traffic-control-module.h"
#include "ns3/tcp-resequence-buffer.h"
#include "ns3/ipv4-letflow-routing-helper.h"
#include "ns3/ipv4-tianwu-routing-helper.h"
#include "ns3/global-value.h"

#include <vector>
#include <map>
#include <utility>
#include <set>

// The CDF in TrafficGenerator
extern "C"
{
#include "cdf.h"
}

#define LINK_CAPACITY_BASE 1000000000 // 1Gbps
#define BUFFER_SIZE 600               // 250 packets

#define RED_QUEUE_MARKING 65 // 65 Packets (available only in DcTcp)

// The flow port range, each flow will be assigned a random port number within this range
#define PORT_START 10000
#define PORT_END 50000

// Adopted from the simulation from WANG PENG
// Acknowledged to https://williamcityu@bitbucket.org/williamcityu/2016-socc-simulation.git
#define PACKET_SIZE 1400

#define PRESTO_RATIO 10

using namespace ns3;

NS_LOG_COMPONENT_DEFINE("CongaSimulationLarge");

enum RunMode
{

    ECMP,
    LetFlow,
    TianWu
};

void print_time(){
    // std::cout<<" At " << Simulator::Now().GetSeconds() << "\n";
    Simulator::Schedule(Seconds(0.0001), &print_time);
}


// Port from Traffic Generator
// Acknowledged to https://github.com/HKUST-SING/TrafficGenerator/blob/master/src/common/common.c
double poission_gen_interval(double avg_rate)
{
    if (avg_rate > 0)
        return -logf(1.0 - (double)rand() / RAND_MAX) / avg_rate;
    else
        return 0;
}

template <typename T>
T rand_range(T min, T max)
{
    return min + ((double)max - min) * rand() / RAND_MAX;
}

void install_applications(int fromLeafId, NodeContainer servers, double requestRate, struct cdf_table *cdfTable,
                          long &flowCount, long &totalFlowSize, int SERVER_COUNT, int LEAF_COUNT, double START_TIME, double END_TIME, double FLOW_LAUNCH_END_TIME, uint32_t applicationPauseThresh, uint32_t applicationPauseTime)
{
    NS_LOG_INFO("Install applications:");
    for (int i = 0; i < SERVER_COUNT; i++)
    {
        int fromServerIndex = fromLeafId * SERVER_COUNT + i;

        double startTime = START_TIME + poission_gen_interval(requestRate);
        while (startTime < FLOW_LAUNCH_END_TIME)
        {
            flowCount++;
            uint16_t port = rand_range(PORT_START, PORT_END);

            int destServerIndex = fromServerIndex;
            while (destServerIndex >= fromLeafId * SERVER_COUNT && destServerIndex < fromLeafId * SERVER_COUNT + SERVER_COUNT)
            {
                destServerIndex = rand_range(0, SERVER_COUNT * LEAF_COUNT);
            }

            Ptr<Node> destServer = servers.Get(destServerIndex);
            Ptr<Ipv4> ipv4 = destServer->GetObject<Ipv4>();
            Ipv4InterfaceAddress destInterface = ipv4->GetAddress(1, 0);
            Ipv4Address destAddress = destInterface.GetLocal();

            BulkSendHelper source("ns3::TcpSocketFactory", InetSocketAddress(destAddress, port));
            uint32_t flowSize = gen_random_cdf(cdfTable);
            // if(fromLeafId == 0)std::cout<<flowSize<<"\n";

            totalFlowSize += flowSize;
            // std::cout<<flowCount<<" "<< flowSize<<" "<<startTime<<std::endl;
            source.SetAttribute("SendSize", UintegerValue(PACKET_SIZE));
            source.SetAttribute("MaxBytes", UintegerValue(flowSize));
            source.SetAttribute("DelayThresh", UintegerValue(applicationPauseThresh));
            source.SetAttribute("DelayTime", TimeValue(MicroSeconds(applicationPauseTime)));

            // Install apps
            ApplicationContainer sourceApp = source.Install(servers.Get(fromServerIndex));
            sourceApp.Start(Seconds(startTime));
            sourceApp.Stop(Seconds(END_TIME));

            // Install packet sinks
            PacketSinkHelper sink("ns3::TcpSocketFactory",
                                  InetSocketAddress(Ipv4Address::GetAny(), port));
            ApplicationContainer sinkApp = sink.Install(servers.Get(destServerIndex));
            sinkApp.Start(Seconds(START_TIME));
            sinkApp.Stop(Seconds(END_TIME));

            /*
            NS_LOG_INFO ("\tFlow from server: " << fromServerIndex << " to server: "
                    << destServerIndex << " on port: " << port << " with flow size: "
                    << flowSize << " [start time: " << startTime <<"]");
            */
        //    std::cout<<"\tFlow from server: " << fromServerIndex << " to server: "
        //             << destServerIndex << " on port: " << port << " with flow size: "
        //             << flowSize << " [start time: " << startTime <<"]\n";

            startTime += poission_gen_interval(requestRate);
        }
    }
    
    
}

static void CwndChange(uint32_t oldv, uint32_t nv)
{
}


int main(int argc, char *argv[])
{

#if 1
    LogComponentEnable("CongaSimulationLarge", LOG_LEVEL_INFO);
#endif

    GlobalValue uint = GlobalValue("DupAckCnt", "help text",
                                   UintegerValue(0),
                                   MakeUintegerChecker<uint32_t>());

    // Command line parameters parsing
    std::string id = "0";
    std::string runModeStr = "ECMP";
    unsigned randomSeed = 0;
    std::string cdfFileName = "";
    double load = 0.0;
    std::string transportProt = "DcTcp";

    // The simulation starting and ending time
    double START_TIME = 0.0;
    double END_TIME = 10;

    double FLOW_LAUNCH_END_TIME = 0.15;

    uint32_t linkLatency = 10;

    int SERVER_COUNT = 8;
    int CORE_COUNT = 16;
    int SPINE_COUNT = 32;
    int LEAF_COUNT = 32;
    int LINK_COUNT = 1;

    uint64_t spineLeafCapacity = 100;
    uint64_t leafServerCapacity = 100;

    bool tcpPause = false;

    uint32_t applicationPauseThresh = 0;
    uint32_t applicationPauseTime = 1000;

    uint32_t quantifyRTTBase = 10;

    bool enableLargeDupAck = false;

    uint32_t letFlowFlowletTimeout = 500;
    uint32_t tianWuFlowletTimeout = 500;
    double tianwu_max = 0.9;
    double tianwu_min = 0.9;
    uint32_t tianwu_sched_freq = 10;

    // 0 symmetry 1 leaf-spine asm 2 fat-tree 3 fat-tree asm
    uint32_t zte_mode = 0;

    CommandLine cmd;
    cmd.AddValue("ID", "Running ID", id);
    cmd.AddValue("StartTime", "Start time of the simulation", START_TIME);
    cmd.AddValue("EndTime", "End time of the simulation", END_TIME);
    cmd.AddValue("FlowLaunchEndTime", "End time of the flow launch period", FLOW_LAUNCH_END_TIME);
    cmd.AddValue("runMode", "Running mode of this simulation: Conga, Conga-flow, Presto, Weighted-Presto, DRB, FlowBender, ECMP, Clove, DRILL, LetFlow, TianWu", runModeStr);
    cmd.AddValue("randomSeed", "Random seed, 0 for random generated", randomSeed);
    cmd.AddValue("cdfFileName", "File name for flow distribution", cdfFileName);
    cmd.AddValue("load", "Load of the network, 0.0 - 1.0", load);
    cmd.AddValue("transportProt", "Transport protocol to use: Tcp, DcTcp", transportProt);
    cmd.AddValue("linkLatency", "Link latency, should be in MicroSeconds", linkLatency);

    cmd.AddValue("spineLeafCapacity", "Spine <-> Leaf capacity in Gbps", spineLeafCapacity);
    cmd.AddValue("leafServerCapacity", "Leaf <-> Server capacity in Gbps", leafServerCapacity);

    cmd.AddValue("applicationPauseThresh", "How many packets can pass before we have delay, 0 for disable", applicationPauseThresh);
    cmd.AddValue("applicationPauseTime", "The time for a delay, in MicroSeconds", applicationPauseTime);

    cmd.AddValue("enableLargeDupAck", "Whether to set the ReTxThreshold to a very large value to mask reordering", enableLargeDupAck);

    cmd.AddValue("letFlowFlowletTimeout", "Flowlet timeout in LetFlow", letFlowFlowletTimeout);
    cmd.AddValue("tianWuFlowletTimeout", "Flowlet timeout in TianWu", tianWuFlowletTimeout);
    cmd.AddValue("tianWuSchedFreq", "Schedule frequency in TianWu", tianwu_sched_freq);

    cmd.AddValue("zteMode", "for zte configuration", zte_mode);

    cmd.Parse(argc, argv);

    uint64_t SPINE_LEAF_CAPACITY = spineLeafCapacity * LINK_CAPACITY_BASE;
    uint64_t LEAF_SERVER_CAPACITY = leafServerCapacity * LINK_CAPACITY_BASE;
    Time LINK_LATENCY = MicroSeconds(linkLatency);

    RunMode runMode;
    if (runModeStr.compare("ECMP") == 0)
    {
        runMode = ECMP;
    }
    else if (runModeStr.compare("LetFlow") == 0)
    {
        runMode = LetFlow;
    }
    else if (runModeStr.compare("TianWu") == 0)
    {
        runMode = TianWu;
    }
    else
    {
        NS_LOG_ERROR("The running mode should be ECMP, LetFlow and TianWu");
        return 0;
    }

    if (load < 0.0 || load >= 1.0)
    {
        NS_LOG_ERROR("The network load should within 0.0 and 1.0");
        return 0;
    }

    if (transportProt.compare("DcTcp") == 0)
    {
        NS_LOG_INFO("Enabling DcTcp");
        Config::SetDefault("ns3::TcpL4Protocol::SocketType", TypeIdValue(TcpDCTCP::GetTypeId()));
        Config::SetDefault("ns3::RedQueueDisc::Mode", StringValue("QUEUE_MODE_BYTES"));
        Config::SetDefault("ns3::RedQueueDisc::MeanPktSize", UintegerValue(PACKET_SIZE));
        Config::SetDefault("ns3::RedQueueDisc::QueueLimit", UintegerValue(BUFFER_SIZE * PACKET_SIZE));
        // Config::SetDefault ("ns3::QueueDisc::Quota", UintegerValue (BUFFER_SIZE));
        Config::SetDefault("ns3::RedQueueDisc::Gentle", BooleanValue(false));
    }

    if (tcpPause)
    {
        NS_LOG_INFO("Enabling TCP pause");
        Config::SetDefault("ns3::TcpSocketBase::Pause", BooleanValue(true));
    }

    NS_LOG_INFO("Config parameters");
    Config::SetDefault("ns3::TcpSocket::SegmentSize", UintegerValue(PACKET_SIZE));
    Config::SetDefault("ns3::TcpSocket::DelAckCount", UintegerValue(0));
    Config::SetDefault("ns3::TcpSocket::ConnTimeout", TimeValue(MilliSeconds(5)));
    Config::SetDefault("ns3::TcpSocket::InitialCwnd", UintegerValue(10));
    Config::SetDefault("ns3::TcpSocketBase::MinRto", TimeValue(MilliSeconds(5)));
    Config::SetDefault("ns3::TcpSocketBase::ClockGranularity", TimeValue(MicroSeconds(100)));
    Config::SetDefault("ns3::RttEstimator::InitialEstimation", TimeValue(MicroSeconds(80)));
    Config::SetDefault("ns3::TcpSocket::SndBufSize", UintegerValue(160000000));
    Config::SetDefault("ns3::TcpSocket::RcvBufSize", UintegerValue(160000000));

    if (enableLargeDupAck)
    {
        Config::SetDefault("ns3::TcpSocketBase::ReTxThreshold", UintegerValue(1000));
    }

    NodeContainer core_switches;
    core_switches.Create(CORE_COUNT);
    NodeContainer spines;
    spines.Create(SPINE_COUNT);
    NodeContainer leaves;
    leaves.Create(LEAF_COUNT);
    NodeContainer servers;
    servers.Create(SERVER_COUNT * LEAF_COUNT);

    NS_LOG_INFO("Install Internet stacks");
    InternetStackHelper internet;
    Ipv4StaticRoutingHelper staticRoutingHelper;
    Ipv4GlobalRoutingHelper globalRoutingHelper;
    Ipv4LetFlowRoutingHelper letFlowRoutingHelper;
    Ipv4TianWuRoutingHelper tianWuRoutingHelper;

    if (runMode == LetFlow)
    {
        internet.SetRoutingHelper(staticRoutingHelper);
        internet.Install(servers);

        internet.SetRoutingHelper(letFlowRoutingHelper);
        internet.Install(spines);
        internet.Install(leaves);
        internet.Install(core_switches);
    }
    else if (runMode == TianWu)
    {
        internet.SetRoutingHelper(staticRoutingHelper);
        internet.Install(servers);

        internet.SetRoutingHelper(tianWuRoutingHelper);
        internet.Install(spines);
        internet.Install(leaves);
        internet.Install(core_switches);
    }
    else if (runMode == ECMP)
    {
        internet.SetRoutingHelper(globalRoutingHelper);
        Config::SetDefault("ns3::Ipv4GlobalRouting::PerflowEcmpRouting", BooleanValue(true));

        internet.Install(servers);
        internet.Install(spines);
        internet.Install(leaves);
        internet.Install(core_switches);
    }

    NS_LOG_INFO("Install channels and assign addresses");

    PointToPointHelper p2p;
    Ipv4AddressHelper ipv4;

    TrafficControlHelper tc;
    if (transportProt.compare("DcTcp") == 0)
    {
        tc.SetRootQueueDisc("ns3::RedQueueDisc", "MinTh", DoubleValue(RED_QUEUE_MARKING * PACKET_SIZE),
                            "MaxTh", DoubleValue(RED_QUEUE_MARKING * PACKET_SIZE));
    }

    NS_LOG_INFO("Configuring servers");
    // Setting servers
    p2p.SetDeviceAttribute("DataRate", DataRateValue(DataRate(LEAF_SERVER_CAPACITY)));
    p2p.SetChannelAttribute("Delay", TimeValue(LINK_LATENCY));
    if (transportProt.compare("Tcp") == 0)
    {
        p2p.SetQueue("ns3::DropTailQueue", "MaxPackets", UintegerValue(BUFFER_SIZE));
    }
    else
    {
        p2p.SetQueue("ns3::DropTailQueue", "MaxPackets", UintegerValue(10));
    }

    ipv4.SetBase("10.1.0.0", "255.255.255.0");

    std::vector<Ipv4Address> leafNetworks(LEAF_COUNT);

    std::vector<Ipv4Address> serverAddresses(SERVER_COUNT * LEAF_COUNT);

    std::map<std::pair<int, int>, uint32_t> leafToSpinePath;
    std::map<std::pair<int, int>, uint32_t> spineToLeafPath;

    for (int i = 0; i < LEAF_COUNT; i++)
    {
        Ipv4Address network = ipv4.NewNetwork();
        leafNetworks[i] = network;

        for (int j = 0; j < SERVER_COUNT; j++)
        {
            int serverIndex = i * SERVER_COUNT + j;
            NodeContainer nodeContainer = NodeContainer(leaves.Get(i), servers.Get(serverIndex));
            NetDeviceContainer netDeviceContainer = p2p.Install(nodeContainer);

            if (transportProt.compare("DcTcp") == 0)
            {
                NS_LOG_INFO("Install RED Queue for leaf: " << i << " and server: " << serverIndex);
                tc.Install(netDeviceContainer);
            }
            Ipv4InterfaceContainer interfaceContainer = ipv4.Assign(netDeviceContainer);

            NS_LOG_INFO("Leaf - " << i << " is connected to Server - " << serverIndex << " with address "
                                  << interfaceContainer.GetAddress(0) << " <-> " << interfaceContainer.GetAddress(1)
                                  << " with port " << netDeviceContainer.Get(0)->GetIfIndex() << " <-> " << netDeviceContainer.Get(1)->GetIfIndex());
            // std::cout<<"Leaf - " << i << " is connected to Server - " << serverIndex << " with address "
            //                       << interfaceContainer.GetAddress(0) << " <-> " << interfaceContainer.GetAddress(1)
            //                       << " with port " << netDeviceContainer.Get(0)->GetIfIndex() << " <-> " << netDeviceContainer.Get(1)->GetIfIndex()<<"\n";

            serverAddresses[serverIndex] = interfaceContainer.GetAddress(1);
            if (transportProt.compare("Tcp") == 0)
            {
                tc.Uninstall(netDeviceContainer);
            }

            if (runMode == LetFlow)
            {
                // All servers just forward the packet to leaf switch
                staticRoutingHelper.GetStaticRouting(servers.Get(serverIndex)->GetObject<Ipv4>())->AddNetworkRouteTo(Ipv4Address("0.0.0.0"), Ipv4Mask("0.0.0.0"), netDeviceContainer.Get(1)->GetIfIndex());

                Ptr<Ipv4LetFlowRouting> letFlowLeaf = letFlowRoutingHelper.GetLetFlowRouting(leaves.Get(i)->GetObject<Ipv4>());

                // LetFlow leaf switches forward the packet to the correct servers
                letFlowLeaf->AddRoute(interfaceContainer.GetAddress(1),
                                      Ipv4Mask("255.255.255.255"),
                                      netDeviceContainer.Get(0)->GetIfIndex());
                letFlowLeaf->SetFlowletTimeout(MicroSeconds(letFlowFlowletTimeout));
            }
            if (runMode == TianWu)
            {
                // All servers just forward the packet to leaf switch
                staticRoutingHelper.GetStaticRouting(servers.Get(serverIndex)->GetObject<Ipv4>())->AddNetworkRouteTo(Ipv4Address("0.0.0.0"), Ipv4Mask("0.0.0.0"), netDeviceContainer.Get(1)->GetIfIndex());

                Ptr<Ipv4TianWuRouting> tianWuLeaf = tianWuRoutingHelper.GetTianWuRouting(leaves.Get(i)->GetObject<Ipv4>());

                // TianWu leaf switches forward the packet to the correct servers
                tianWuLeaf->AddRoute(interfaceContainer.GetAddress(1),
                                     Ipv4Mask("255.255.255.255"),
                                     netDeviceContainer.Get(0)->GetIfIndex());
                tianWuLeaf->SetFlowletTimeout(MicroSeconds(tianWuFlowletTimeout));
                tianWuLeaf->SetTianwuParas(tianwu_max, tianwu_min, SPINE_LEAF_CAPACITY, tianwu_sched_freq, 1);
            }

        }
    }

    NS_LOG_INFO("Configuring switches");
    // Setting up switches
    p2p.SetDeviceAttribute("DataRate", DataRateValue(DataRate(SPINE_LEAF_CAPACITY)));
    std::set<std::pair<uint32_t, uint32_t>> asymLink; // set< (A, B) > Leaf A -> Spine B is asymmetric

    for(int i = 0; i < SERVER_COUNT*LEAF_COUNT/SPINE_COUNT; i++){

    for (int j = 0; j < 4; j++)
    {
        for (int k = 0; k < 4; k++)
        {
            uint32_t leaf_index = i*4 + j;
            uint32_t spine_index = i*4 + k;


                // TODO
                uint64_t spineLeafCapacity = SPINE_LEAF_CAPACITY;

                // For ZTE asymmetry
                // if(zte_mode == 3){
                //     if( LEAF_COUNT!=8 || SPINE_COUNT!=8 || SPINE_LEAF_CAPACITY!=100 * LINK_CAPACITY_BASE){
                //         std::cout<<"False leaf, spine or rate configuration\n";
                //         exit(1);
                //     }
                //     if(j == 0)spineLeafCapacity = 60 * LINK_CAPACITY_BASE;
                //     else if(j == 1)spineLeafCapacity = 80 * LINK_CAPACITY_BASE;
                //     else if(j == 2)spineLeafCapacity = 120 * LINK_CAPACITY_BASE;
                //     else if(j == 3)spineLeafCapacity = 140 * LINK_CAPACITY_BASE;
                // }

                p2p.SetDeviceAttribute("DataRate", DataRateValue(DataRate(spineLeafCapacity)));
                ipv4.NewNetwork();

                NodeContainer nodeContainer = NodeContainer(leaves.Get(leaf_index), spines.Get(spine_index));
                NetDeviceContainer netDeviceContainer = p2p.Install(nodeContainer);
                if (transportProt.compare("DcTcp") == 0)
                {
                    NS_LOG_INFO("Install RED Queue for leaf: " << leaf_index << " and spine: " << spine_index);
                    tc.Install(netDeviceContainer); 
                }
                Ipv4InterfaceContainer ipv4InterfaceContainer = ipv4.Assign(netDeviceContainer);
                NS_LOG_INFO("Leaf - " << leaf_index << " is connected to Spine - " << spine_index << " with address "
                                      << ipv4InterfaceContainer.GetAddress(0) << " <-> " << ipv4InterfaceContainer.GetAddress(1)
                                      << " with port " << netDeviceContainer.Get(0)->GetIfIndex() << " <-> " << netDeviceContainer.Get(1)->GetIfIndex()
                                      << " with data rate " << spineLeafCapacity);


                // std::cout<<"Leaf - " << leaf_index << " is connected to Spine - " << spine_index << " with address "
                //                       << ipv4InterfaceContainer.GetAddress(0) << " <-> " << ipv4InterfaceContainer.GetAddress(1)
                //                       << " with port " << netDeviceContainer.Get(0)->GetIfIndex() << " <-> " << netDeviceContainer.Get(1)->GetIfIndex()
                //                       << " with data rate " << spineLeafCapacity<<"\n";


                if (transportProt.compare("Tcp") == 0)
                {
                    tc.Uninstall(netDeviceContainer);
                }

                if (runMode == LetFlow)
                {
                    // For each LetFlow leaf switch, routing entry to route the packet to OTHER leaves should be added
                    for (int k = 0; k < LEAF_COUNT; k++)
                    {
                        if (k != leaf_index)
                        {
                            letFlowRoutingHelper.GetLetFlowRouting(leaves.Get(leaf_index)->GetObject<Ipv4>())->AddRoute(leafNetworks[k], Ipv4Mask("255.255.255.0"), netDeviceContainer.Get(0)->GetIfIndex());
                        }
                    }

                    // For each LetFlow spine switch, routing entry to THIS leaf switch should be added
                    Ptr<Ipv4LetFlowRouting> letFlowSpine = letFlowRoutingHelper.GetLetFlowRouting(spines.Get(spine_index)->GetObject<Ipv4>());
                    letFlowSpine->AddRoute(leafNetworks[leaf_index],
                                           Ipv4Mask("255.255.255.0"),
                                           netDeviceContainer.Get(1)->GetIfIndex());
                    letFlowSpine->SetFlowletTimeout(MicroSeconds(letFlowFlowletTimeout));
                }
                if (runMode == TianWu)
                {
                    // For each TianWu leaf switch, routing entry to route the packet to OTHER leaves should be added
                    for (int k = 0; k < LEAF_COUNT; k++)
                    {
                        if (k != leaf_index)
                        {
                            tianWuRoutingHelper.GetTianWuRouting(leaves.Get(leaf_index)->GetObject<Ipv4>())->AddRoute(leafNetworks[k], Ipv4Mask("255.255.255.0"), netDeviceContainer.Get(0)->GetIfIndex());
                        }
                    }

                    // For each TianWu spine switch, routing entry to THIS leaf switch should be added
                    Ptr<Ipv4TianWuRouting> tianWuSpine = tianWuRoutingHelper.GetTianWuRouting(spines.Get(spine_index)->GetObject<Ipv4>());
                    tianWuSpine->AddRoute(leafNetworks[leaf_index],
                                          Ipv4Mask("255.255.255.0"),
                                          netDeviceContainer.Get(1)->GetIfIndex());
                    tianWuSpine->SetFlowletTimeout(MicroSeconds(tianWuFlowletTimeout));
                    tianWuSpine->SetTianwuParas(tianwu_max, tianwu_min, SPINE_LEAF_CAPACITY, tianwu_sched_freq, 0);
                }
            
        }
    }
    }

    for(int i = 0; i< SPINE_COUNT; i++){
        for(int j = 0; j < 4; j++){
            uint64_t spineLeafCapacity = SPINE_LEAF_CAPACITY;
            uint32_t spine_index = i;
            uint32_t core_index = 4*(i%4)+j;
            p2p.SetDeviceAttribute("DataRate", DataRateValue(DataRate(spineLeafCapacity)));
            ipv4.NewNetwork();
            
            NodeContainer nodeContainer = NodeContainer(spines.Get(spine_index), core_switches.Get(core_index));
            NetDeviceContainer netDeviceContainer = p2p.Install(nodeContainer);

            if (transportProt.compare("DcTcp") == 0)
                {
                    NS_LOG_INFO("Install RED Queue for spine: " << spine_index << " and core: " << core_index);
                    tc.Install(netDeviceContainer); 
                }
                Ipv4InterfaceContainer ipv4InterfaceContainer = ipv4.Assign(netDeviceContainer);
                NS_LOG_INFO("Spine - " << spine_index << " is connected to Core - " << core_index << " with address "
                                      << ipv4InterfaceContainer.GetAddress(0) << " <-> " << ipv4InterfaceContainer.GetAddress(1)
                                      << " with port " << netDeviceContainer.Get(0)->GetIfIndex() << " <-> " << netDeviceContainer.Get(1)->GetIfIndex()
                                      << " with data rate " << spineLeafCapacity);


                // std::cout<<"Spine - " << spine_index << " is connected to Core - " << core_index << " with address "
                //                       << ipv4InterfaceContainer.GetAddress(0) << " <-> " << ipv4InterfaceContainer.GetAddress(1)
                //                       << " with port " << netDeviceContainer.Get(0)->GetIfIndex() << " <-> " << netDeviceContainer.Get(1)->GetIfIndex()
                //                       << " with data rate " << spineLeafCapacity<<"\n";


                if (transportProt.compare("Tcp") == 0)
                {
                    tc.Uninstall(netDeviceContainer);
                }

                if (runMode == LetFlow)
                {
                    // For each LetFlow leaf switch, routing entry to route the packet to OTHER leaves should be added
                    for (int k = 0; k < LEAF_COUNT; k++)
                    {
                        if (k < (spine_index/4)*4 || k>= (spine_index/4)*4+4)
                        {
                            letFlowRoutingHelper.GetLetFlowRouting(spines.Get(spine_index)->GetObject<Ipv4>())->AddRoute(leafNetworks[k], Ipv4Mask("255.255.255.0"), netDeviceContainer.Get(0)->GetIfIndex());
                        }
                    }

                    for (int k = 0; k < LEAF_COUNT; k++)
                    {
                        if (k >= (spine_index/4)*4 && k< (spine_index/4)*4+4)
                        {
                            letFlowRoutingHelper.GetLetFlowRouting(core_switches.Get(core_index)->GetObject<Ipv4>())->AddRoute(leafNetworks[k], Ipv4Mask("255.255.255.0"), netDeviceContainer.Get(1)->GetIfIndex());
                        }
                    }
                }
                if (runMode == TianWu)
                {
                    // For each TianWu leaf switch, routing entry to route the packet to OTHER leaves should be added
                    for (int k = 0; k < LEAF_COUNT; k++)
                    {
                        if (k < (spine_index/4)*4 || k>= (spine_index/4)*4+4)
                        {
                            tianWuRoutingHelper.GetTianWuRouting(spines.Get(spine_index)->GetObject<Ipv4>())->AddRoute(leafNetworks[k], Ipv4Mask("255.255.255.0"), netDeviceContainer.Get(0)->GetIfIndex());
                        }
                    }

                    for (int k = 0; k < LEAF_COUNT; k++)
                    {
                        if (k >= (spine_index/4)*4 && k< (spine_index/4)*4+4)
                        {
                            tianWuRoutingHelper.GetTianWuRouting(core_switches.Get(core_index)->GetObject<Ipv4>())->AddRoute(leafNetworks[k], Ipv4Mask("255.255.255.0"), netDeviceContainer.Get(1)->GetIfIndex());
                            Ptr<Ipv4TianWuRouting> tianWuCore = tianWuRoutingHelper.GetTianWuRouting(core_switches.Get(core_index)->GetObject<Ipv4>());
                            tianWuCore->SetFlowletTimeout(MicroSeconds(tianWuFlowletTimeout));
                            tianWuCore->SetTianwuParas(tianwu_max, tianwu_min, SPINE_LEAF_CAPACITY, tianwu_sched_freq, 0);
                        }
                    }
                }


        }
    }

    if (runMode == ECMP )
    {
        NS_LOG_INFO("Populate global routing tables");
        Ipv4GlobalRoutingHelper::PopulateRoutingTables();
    }

    double oversubRatio = static_cast<double>(SERVER_COUNT * LEAF_COUNT* LEAF_SERVER_CAPACITY) / (SPINE_COUNT * 4 * LINK_COUNT * SPINE_LEAF_CAPACITY);
    NS_LOG_INFO("Over-subscription ratio: " << oversubRatio);

    NS_LOG_INFO("Initialize CDF table");
    struct cdf_table *cdfTable = new cdf_table();
    init_cdf(cdfTable);
    load_cdf(cdfTable, cdfFileName.c_str());

    NS_LOG_INFO("Calculating request rate");

    double requestRate = load * LEAF_SERVER_CAPACITY  / oversubRatio / (8 * avg_cdf(cdfTable)) ;
    // std::cout<< LEAF_SERVER_CAPACITY<<" "<<oversubRatio<<" "<< avg_cdf(cdfTable)<<" "<<  requestRate<<"\n";
    NS_LOG_INFO("Average request rate: " << requestRate << " per second");

    NS_LOG_INFO("Initialize random seed: " << randomSeed);
    if (randomSeed == 0)
    {
        srand((unsigned)time(NULL));
    }
    else
    {
        srand(randomSeed);
    }

    NS_LOG_INFO("Create applications");

    long flowCount = 0;
    long totalFlowSize = 0;

    if (requestRate > 0.0001)
        for (int fromLeafId = 0; fromLeafId < LEAF_COUNT; fromLeafId++)
        {
            install_applications(fromLeafId, servers, requestRate, cdfTable, flowCount, totalFlowSize, SERVER_COUNT, LEAF_COUNT, START_TIME, END_TIME, FLOW_LAUNCH_END_TIME, applicationPauseThresh, applicationPauseTime);
        }
        std::cout << flowCount<<std::endl;

    // install_applications_new(servers, START_TIME, END_TIME, SERVER_COUNT);

    NS_LOG_INFO("Total flow: " << flowCount);

    NS_LOG_INFO("Actual average flow size: " << static_cast<double>(totalFlowSize) / flowCount);

    NS_LOG_INFO("Enabling flow monitor");

    Ptr<FlowMonitor> flowMonitor;
    FlowMonitorHelper flowHelper;
    flowMonitor = flowHelper.InstallAll();

    NS_LOG_INFO("Enabling link monitor");

    Ptr<LinkMonitor> linkMonitor = Create<LinkMonitor>();

    linkMonitor->Start(Seconds(START_TIME));
    linkMonitor->Stop(Seconds(END_TIME));

    flowMonitor->CheckForLostPackets();

    std::stringstream flowMonitorFilename;
    std::stringstream linkMonitorFilename;

    flowMonitorFilename << id << "-1-large-load-" << LEAF_COUNT << "X" << SPINE_COUNT << "-" << load << "-" << transportProt << "-";
    linkMonitorFilename << id << "-1-large-load-" << LEAF_COUNT << "X" << SPINE_COUNT << "-" << load << "-" << transportProt << "-";

    if (runMode == ECMP)
    {
        flowMonitorFilename << "ecmp-simulation-";
        linkMonitorFilename << "ecmp-simulation-";
    }
    else if (runMode == LetFlow)
    {
        // flowMonitorFilename << "letflow-simulation-" << letFlowFlowletTimeout << "-";
        // linkMonitorFilename << "letflow-simulation-" << letFlowFlowletTimeout << "-";
        flowMonitorFilename << "letflow-simulation-";
        linkMonitorFilename << "letflow-simulation-";
    }
    else if (runMode == TianWu)
    {
        // flowMonitorFilename << "tianwu-simulation-" << tianWuFlowletTimeout << "-";
        // linkMonitorFilename << "tianwu-simulation-" << tianWuFlowletTimeout << "-";
        flowMonitorFilename << "tianwu-simulation-";
        linkMonitorFilename << "tianwu-simulation-";
    }

    flowMonitorFilename << randomSeed << "-";
    linkMonitorFilename << randomSeed << "-";

    flowMonitorFilename << "b" << BUFFER_SIZE << ".xml";
    linkMonitorFilename << "b" << BUFFER_SIZE << "-link-utility.out";

    NS_LOG_INFO("Start simulation");
    Simulator::Schedule(Seconds(0.00001), &print_time);
    std::cout<<"start\n";
    Simulator::Stop(Seconds(END_TIME));
    Simulator::Run();

    flowMonitor->SerializeToXmlFile(flowMonitorFilename.str(), true, true);
    linkMonitor->OutputToFile(linkMonitorFilename.str(), &LinkMonitor::DefaultFormat);

    Simulator::Destroy();
    free_cdf(cdfTable);
    NS_LOG_INFO("Stop simulation");
}
