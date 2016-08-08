/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */

#include "ipv4-link-probe.h"

#include "ns3/log.h"
#include "ns3/config.h"
#include "ns3/simulator.h"
#include "ns3/ipv4-header.h"

#include "link-monitor.h"

namespace ns3 {

NS_LOG_COMPONENT_DEFINE ("Ipv4LinkProbe");

NS_OBJECT_ENSURE_REGISTERED (Ipv4LinkProbe);

TypeId
Ipv4LinkProbe::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::Ipv4LinkProbe")
      .SetParent<LinkProbe> ()
      .SetGroupName ("LinkMonitor");

  return tid;
}

Ipv4LinkProbe::Ipv4LinkProbe (Ptr<Node> node, Ptr<LinkMonitor> linkMonitor)
    :LinkProbe (linkMonitor),
     m_checkTime (MicroSeconds (100))
{
  NS_LOG_FUNCTION (this);

  m_ipv4 = m_ipv4 = node->GetObject<Ipv4L3Protocol> ();

  // Notice, the interface at 0 is loopback, we simply ignore it
  for (uint32_t interface = 1; interface < m_ipv4->GetNInterfaces (); ++interface)
  {
    m_accumulatedTxBytes[interface] = 0;
    m_accumulatedDequeueBytes[interface] = 0;

    m_queueProbe[interface] = Create<Ipv4QueueProbe> ();
    m_queueProbe[interface]->SetInterfaceId (interface);
    m_queueProbe[interface]->SetIpv4LinkProbe (this);

    std::ostringstream oss;
    oss << "/NodeList/" << node->GetId () << "/DeviceList/" << interface << "/TxQueue/Dequeue";
    Config::ConnectWithoutContext (oss.str (),
            MakeCallback (&Ipv4QueueProbe::DequeueLogger, m_queueProbe[interface]));
  }

  if (!m_ipv4->TraceConnectWithoutContext ("Tx",
              MakeCallback (&Ipv4LinkProbe::TxLogger, this)))
  {
    NS_FATAL_ERROR ("trace fail");
  }
}

void
Ipv4LinkProbe::SetDataRateAll (DataRate dataRate)
{
  for (uint32_t interface = 1; interface < m_ipv4->GetNInterfaces (); ++interface)
  {
    m_dataRate[interface] = dataRate;
  }
}

void
Ipv4LinkProbe::TxLogger (Ptr<const Packet> packet, Ptr<Ipv4> ipv4, uint32_t interface)
{
  uint32_t size = packet->GetSize ();
  NS_LOG_LOGIC ("Trace " << size << " bytes TX on port: " << interface);
  m_accumulatedTxBytes[interface] = m_accumulatedTxBytes[interface] + size;
}

void
Ipv4LinkProbe::DequeueLogger (Ptr<const Packet> packet, uint32_t interface)
{
  uint32_t size = packet->GetSize ();
  NS_LOG_LOGIC ("Trace " << size << " bytes dequeued on port: " << interface);
  m_accumulatedDequeueBytes[interface] = m_accumulatedDequeueBytes[interface] + size;
}

void
Ipv4LinkProbe::CheckCurrentStatus ()
{
  for (uint32_t interface = 1; interface < m_ipv4->GetNInterfaces (); ++interface)
  {
    uint64_t lastTxBytes = 0;
    uint64_t lastDequeueBytes = 0;

    std::map<uint32_t, std::vector<struct LinkProbe::LinkStats> >::iterator itr = m_stats.find (interface);
    if (itr == m_stats.end ())
    {
      struct LinkProbe::LinkStats newStats;
      newStats.checkTime = Simulator::Now ();
      newStats.accumulatedTxBytes = m_accumulatedTxBytes[interface];
      newStats.txLinkUtility =
          Ipv4LinkProbe::GetLinkUtility (interface, m_accumulatedTxBytes[interface] - lastTxBytes, m_checkTime);
      newStats.accumulatedDequeueBytes = m_accumulatedDequeueBytes[interface];
      newStats.dequeueLinkUtility =
          Ipv4LinkProbe::GetLinkUtility (interface, m_accumulatedDequeueBytes[interface] - lastDequeueBytes, m_checkTime);
      std::vector<struct LinkProbe::LinkStats> newVector;
      newVector.push_back (newStats);
      m_stats[interface] = newVector;
    }
    else
    {
      lastTxBytes = (itr->second).back ().accumulatedTxBytes;
      lastDequeueBytes = (itr->second).back ().accumulatedDequeueBytes;
      struct LinkProbe::LinkStats newStats;
      newStats.checkTime = Simulator::Now ();
      newStats.accumulatedTxBytes = m_accumulatedTxBytes[interface];
      newStats.txLinkUtility =
          Ipv4LinkProbe::GetLinkUtility (interface, m_accumulatedTxBytes[interface] - lastTxBytes, m_checkTime);
      newStats.accumulatedDequeueBytes = m_accumulatedDequeueBytes[interface];
      newStats.dequeueLinkUtility =
          Ipv4LinkProbe::GetLinkUtility (interface, m_accumulatedDequeueBytes[interface] - lastDequeueBytes, m_checkTime);
      (itr->second).push_back (newStats);
    }
  }

  m_checkEvent = Simulator::Schedule (m_checkTime, &Ipv4LinkProbe::CheckCurrentStatus, this);

}

void
Ipv4LinkProbe::Start ()
{
  m_checkEvent = Simulator::Schedule (m_checkTime, &Ipv4LinkProbe::CheckCurrentStatus, this);
}

void
Ipv4LinkProbe::Stop ()
{
  m_checkEvent.Cancel ();
}

double
Ipv4LinkProbe::GetLinkUtility (uint32_t interface, uint64_t bytes, Time time)
{
  std::map<uint32_t, DataRate>::iterator itr = m_dataRate.find (interface);
  if (itr == m_dataRate.end ())
  {
    return 0.0f;
  }

  return static_cast<double> (bytes * 8) / ((itr->second).GetBitRate () * time.GetSeconds ());
}

void
Ipv4LinkProbe::SetCheckTime (Time checkTime)
{
  m_checkTime = checkTime;
}

}