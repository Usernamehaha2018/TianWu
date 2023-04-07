/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */

#include "ipv4-tianwu-routing.h"
#include "ns3/node.h"
#include "ns3/flow-id-tag.h"
#include "ns3/log.h"
#include "ns3/simulator.h"
#include "ns3/net-device.h"
#include "ns3/channel.h"
#include "ns3/node.h"
#include "ns3/ipv4-l3-protocol.h"
#include "ns3/traffic-control-layer.h"
#include "ns3/point-to-point-net-device.h"
#include "ns3/global-value.h"

#include <algorithm>

namespace ns3
{

  NS_LOG_COMPONENT_DEFINE("Ipv4TianWuRouting");

  NS_OBJECT_ENSURE_REGISTERED(Ipv4TianWuRouting);
  int Ipv4TianWuRouting::tianwuid = 0;

  Ipv4TianWuRouting::Ipv4TianWuRouting() : m_flowletTimeout(MicroSeconds(500)), // The default value of flowlet timeout is small for experimental purpose
                                           m_ipv4(0)
  {
    Simulator::Schedule(8*m_flowletTimeout, &Ipv4TianWuRouting::CalculateUtilized, this);
    t_id = tianwuid;
    tianwuid += 1;
    NS_LOG_FUNCTION(this);
  }

  Ipv4TianWuRouting::~Ipv4TianWuRouting()
  {
    NS_LOG_FUNCTION(this);
  }

  TypeId
  Ipv4TianWuRouting::GetTypeId(void)
  {
    static TypeId tid = TypeId("ns3::Ipv4TianWuRouting")
                            .SetParent<Object>()
                            .SetGroupName("Internet")
                            .AddConstructor<Ipv4TianWuRouting>();
    

    return tid;
  }

  void
  Ipv4TianWuRouting::AddRoute(Ipv4Address network, Ipv4Mask networkMask, uint32_t port)
  {
    NS_LOG_LOGIC(this << " Add TianWu routing entry: " << network << "/" << networkMask << " would go through port: " << port);
    TianWuRouteEntry tianWuRouteEntry;
    tianWuRouteEntry.network = network;
    tianWuRouteEntry.networkMask = networkMask;
    tianWuRouteEntry.port = port;
    m_routeEntryList.push_back(tianWuRouteEntry);
  }

  std::vector<TianWuRouteEntry>
  Ipv4TianWuRouting::LookupTianWuRouteEntries(Ipv4Address dest)
  {
    std::vector<TianWuRouteEntry> tianWuRouteEntries;
    std::vector<TianWuRouteEntry>::iterator itr = m_routeEntryList.begin();
    for (; itr != m_routeEntryList.end(); ++itr)
    {
      if ((*itr).networkMask.IsMatch(dest, (*itr).network))
      {
        tianWuRouteEntries.push_back(*itr);
      }
    }
    return tianWuRouteEntries;
  }

  Ptr<Ipv4Route>
  Ipv4TianWuRouting::ConstructIpv4Route(uint32_t port, Ipv4Address destAddress)
  {
    Ptr<NetDevice> dev = m_ipv4->GetNetDevice(port);
    Ptr<Channel> channel = dev->GetChannel();
    uint32_t otherEnd = (channel->GetDevice(0) == dev) ? 1 : 0;
    Ptr<Node> nextHop = channel->GetDevice(otherEnd)->GetNode();
    uint32_t nextIf = channel->GetDevice(otherEnd)->GetIfIndex();
    Ipv4Address nextHopAddr = nextHop->GetObject<Ipv4>()->GetAddress(nextIf, 0).GetLocal();
    Ptr<Ipv4Route> route = Create<Ipv4Route>();
    route->SetOutputDevice(m_ipv4->GetNetDevice(port));
    route->SetGateway(nextHopAddr);
    route->SetSource(m_ipv4->GetAddress(port, 0).GetLocal());
    route->SetDestination(destAddress);
    return route;
  }

  void
  Ipv4TianWuRouting::SetFlowletTimeout(Time timeout)
  {
    m_flowletTimeout = timeout;
  }

  void
  Ipv4TianWuRouting::SetChangeAble()
  {
    changeAble = 1;
  }
  void
  Ipv4TianWuRouting::CalculateUtilized()
  {
    changeAble = 0;
    auto iter = m_portTransmit.begin();
    m_highUtilizedPortSet.clear();
    m_underUtilizedPortSet.clear();
    while(iter != m_portTransmit.end()) {
      if((m_flowletTimeout.GetMicroSeconds() *10 *0.8*10000000000)/(8*1000000) < iter->second )
        {
          m_highUtilizedPortSet.push_back(iter->first);
          // if(iter->first>=9)std::cout <<t_id<<"\n";
        }
      if((m_flowletTimeout.GetMicroSeconds() *10 *0.2*10000000000)/(8*1000000) > iter->second )
        {
          m_underUtilizedPortSet.push_back(iter->first);
        }
        if(t_id == 7)std::cout<<" At " << Simulator::Now().GetSeconds() <<" port "<<iter->first<<" "<< (double)iter->second/((m_flowletTimeout.GetMicroSeconds() *10 *10000000000)/(8*1000000))<<std::endl;
        iter->second = 0;
        iter++;
        
    }
    
    if(t_id == 7){
      std::cout<<"\n";
      for(auto j= m_flowPort.begin();j!=m_flowPort.end();j++){
        std::cout<<j->first<<" ";
        for(auto m = j->second.begin(); m!=j->second.end();m++)
          std::cout << m->flowid<<" "<<m->network1<<" "<<m->network2<<"\n";
      }
    }
     m_flowPortOld.clear();
     m_flowSeenOld.clear();
    for(auto j= m_flowPort.begin();j!=m_flowPort.end();j++){
      for(auto m:j->second)
        m_flowPortOld[j->first].push_back(m);
    }

    m_flowPort.clear();
    m_flowSeen.clear();
    // std::cout<<m_flowPortOld.size()<<"\n";
    Simulator::Schedule(10*m_flowletTimeout, &Ipv4TianWuRouting::CalculateUtilized, this);
    // Simulator::Schedule(5*m_flowletTimeout, &Ipv4TianWuRouting::SetChangeAble, this);
  }

  Ptr<Ipv4Route>
  Ipv4TianWuRouting::RouteOutput(Ptr<Packet> packet, const Ipv4Header &header, Ptr<NetDevice> oif, Socket::SocketErrno &sockerr)
  {
    NS_LOG_ERROR(this << " TianWu routing is not support for local routing output");
    return 0;
  }



uint32_t
  Ipv4TianWuRouting::CalculateQueueLength (uint32_t interface)
{
  Ptr<Ipv4L3Protocol> ipv4L3Protocol = DynamicCast<Ipv4L3Protocol> (m_ipv4);
  if (!ipv4L3Protocol)
  {
    NS_LOG_ERROR (this << " Drill routing cannot work other than Ipv4L3Protocol");
    return 0;
  }

  uint32_t totalLength = 0;

  const Ptr<NetDevice> netDevice = m_ipv4->GetNetDevice (interface);

  if (netDevice->IsPointToPoint ())
  {
    Ptr<PointToPointNetDevice> p2pNetDevice = DynamicCast<PointToPointNetDevice> (netDevice);
    if (p2pNetDevice)
    {
      totalLength += p2pNetDevice->GetQueue ()->GetNBytes ();
    }
  }

  Ptr<TrafficControlLayer> tc = ipv4L3Protocol->GetNode ()->GetObject<TrafficControlLayer> ();

  if (!tc)
  {
    return totalLength;
  }

  Ptr<QueueDisc> queueDisc = tc->GetRootQueueDiscOnDevice (netDevice);
  if (queueDisc)
  {
    totalLength += queueDisc->GetNBytes ();
  }
  return totalLength;
}


  bool
  Ipv4TianWuRouting::RouteInput(Ptr<const Packet> p, const Ipv4Header &header, Ptr<const NetDevice> idev,
                                UnicastForwardCallback ucb, MulticastForwardCallback mcb,
                                LocalDeliverCallback lcb, ErrorCallback ecb)
  {
    NS_LOG_LOGIC(this << " RouteInput: " << p << "Ip header: " << header);

    NS_ASSERT(m_ipv4->GetInterfaceForDevice(idev) >= 0);

    Ptr<Packet> packet = ConstCast<Packet>(p);

    Ipv4Address destAddress = header.GetDestination();

    // TianWu routing only supports unicast
    if (destAddress.IsMulticast() || destAddress.IsBroadcast())
    {
      NS_LOG_ERROR(this << " TianWu routing only supports unicast");
      ecb(packet, header, Socket::ERROR_NOROUTETOHOST);
      return false;
    }

    // Check if input device supports IP forwarding
    uint32_t iif = m_ipv4->GetInterfaceForDevice(idev);
    if (m_ipv4->IsForwarding(iif) == false)
    {
      NS_LOG_ERROR(this << " Forwarding disabled for this interface");
      ecb(packet, header, Socket::ERROR_NOROUTETOHOST);
      return false;
    }

    // Packet arrival time
    Time now = Simulator::Now();

    // Extract the flow id
    uint32_t flowId = 0;
    FlowIdTag flowIdTag;
    bool flowIdFound = packet->PeekPacketTag(flowIdTag);
    if (!flowIdFound)
    {
      NS_LOG_ERROR(this << " TianWu routing cannot extract the flow id");
      ecb(packet, header, Socket::ERROR_NOROUTETOHOST);
      return false;
    }
    flowId = flowIdTag.GetFlowId();

    std::vector<TianWuRouteEntry> routeEntries = Ipv4TianWuRouting::LookupTianWuRouteEntries(destAddress);

    if (routeEntries.empty())
    {
      NS_LOG_ERROR(this << " TianWu routing cannot find routing entry");
      ecb(packet, header, Socket::ERROR_NOROUTETOHOST);
      return false;
    }

    uint32_t selectedPort;

    // If the flowlet table entry is valid, return the port
    std::map<uint32_t, struct TianWuFlowlet>::iterator flowletItr = m_flowletTable.find(flowId);
    if (flowletItr != m_flowletTable.end())
    {


      TianWuFlowlet flowlet = flowletItr->second;
      
      if (now - flowlet.activeTime <= m_flowletTimeout && flowlet.lastSeen < 20)
      {

        if (now - flowlet.lastSeenTime > m_flowletTimeout / 2)
        {
          flowlet.lastSeen += 1;
          // Do not forget to update the flowlet active time
          flowlet.lastSeenTime = now;
        }

        // Do not forget to update the flowlet active time
        flowlet.activeTime = now;

        // Return the port information used for routing routine to select the port
        selectedPort = flowlet.port;

        Ptr<Ipv4Route> route = Ipv4TianWuRouting::ConstructIpv4Route(selectedPort, destAddress);
        ucb(route, packet, header);

        m_flowletTable[flowId] = flowlet;

        m_portTransmit[selectedPort] += p->GetSize();

        return true;
      }
      else if (now - flowlet.activeTime <= m_flowletTimeout )
      {
        // record flow
        auto s = std::find(m_flowSeen.begin(), m_flowSeen.end(), flowId);
        if(s==m_flowSeen.end() && p->GetSize()>1000){
          struct TianWuRouteFlow t;
          t.flowid = flowId;
          t.network1 = destAddress;
          t.network2 = header.GetSource();
          m_flowPort[flowlet.port].push_back(t);
          m_flowSeen.push_back(flowId);
          // std::cout<<p->GetSize()<<"\n";
        }
        auto j = std::find(m_highUtilizedPortSet.begin(), m_highUtilizedPortSet.end(), flowlet.port);
        if (j != m_highUtilizedPortSet.end())
        {

          for (auto entry : routeEntries)
          {
            auto i = std::find(m_underUtilizedPortSet.begin(), m_underUtilizedPortSet.end(), entry.port);
            if (i != m_underUtilizedPortSet.end() &&((m_flowPortOld.find(entry.port) ==m_flowPortOld.end() && (m_flowPortOld.find(flowlet.port) !=m_flowPortOld.end()&&m_flowPortOld[flowlet.port].size()>1))
              || m_flowPortOld[flowlet.port].size() > m_flowPortOld[entry.port].size()+1))
            { 
              if(t_id==7){std::cout<< Simulator::Now().GetSeconds()<< " "<<"tianwu change port "<<flowId<< " from " <<flowlet.port <<" to "<< entry.port<<std::endl;
              
              }
              selectedPort = entry.port;
              m_underUtilizedPortSet.erase(i);
              flowlet.lastSeenTime = now;
              flowlet.activeTime = now;
              flowlet.port = selectedPort;
              Ptr<Ipv4Route> route = Ipv4TianWuRouting::ConstructIpv4Route(selectedPort, destAddress);
              ucb(route, packet, header);
              m_flowletTable[flowId] = flowlet;

              m_portTransmit[selectedPort] += p->GetSize();
              return true;
            }
          }

          // this means no available under utilized port
        }
        // std::cout <<"No available port "<<t_id<<" "<<flowlet.lastSeen<<std::endl;
        flowlet.activeTime = now;
        selectedPort = flowlet.port;
        Ptr<Ipv4Route> route = Ipv4TianWuRouting::ConstructIpv4Route(selectedPort, destAddress);
        ucb(route, packet, header);
        m_flowletTable[flowId] = flowlet;

        m_portTransmit[selectedPort] += p->GetSize();
        return true;
      }
      else if (now - flowlet.activeTime > m_flowletTimeout && flowlet.lastSeen > 15 ){
        flowlet.activeTime = now;
        selectedPort = flowlet.port;
        Ptr<Ipv4Route> route = Ipv4TianWuRouting::ConstructIpv4Route(selectedPort, destAddress);
        ucb(route, packet, header);
        m_flowletTable[flowId] = flowlet;

        m_portTransmit[selectedPort] += p->GetSize();
        return true;


      }
    }

    // Not hit. Random Select the Port
    if(t_id == 7&&flowletItr!=m_flowletTable.end()&&flowletItr->second.lastSeen>10)
    {std::cout<<"timeout for " <<flowId<<"\n";}
    selectedPort = routeEntries[rand() % routeEntries.size()].port;

    TianWuFlowlet flowlet;

    flowlet.port = selectedPort;
    flowlet.activeTime = now;
    flowlet.lastSeen = 0;
    flowlet.lastSeenTime = now;

    Ptr<Ipv4Route> route = Ipv4TianWuRouting::ConstructIpv4Route(selectedPort, destAddress);
    ucb(route, packet, header);

    m_flowletTable[flowId] = flowlet;
     m_portTransmit[selectedPort] += p->GetSize();
    return true;
  }

  void
  Ipv4TianWuRouting::NotifyInterfaceUp(uint32_t interface)
  
  {
    m_portTransmit[interface] = 0;
  }

  void
  Ipv4TianWuRouting::NotifyInterfaceDown(uint32_t interface)
  {
  }

  void
  Ipv4TianWuRouting::NotifyAddAddress(uint32_t interface, Ipv4InterfaceAddress address)
  {
  }

  void
  Ipv4TianWuRouting::NotifyRemoveAddress(uint32_t interface, Ipv4InterfaceAddress address)
  {
  }

  void
  Ipv4TianWuRouting::SetIpv4(Ptr<Ipv4> ipv4)
  {
    NS_LOG_LOGIC(this << "Setting up Ipv4: " << ipv4);
    NS_ASSERT(m_ipv4 == 0 && ipv4 != 0);
    m_ipv4 = ipv4;
  }

  void
  Ipv4TianWuRouting::PrintRoutingTable(Ptr<OutputStreamWrapper> stream) const
  {
  }

  void
  Ipv4TianWuRouting::DoDispose(void)
  {
    m_ipv4 = 0;
    Ipv4RoutingProtocol::DoDispose();
  }

}
