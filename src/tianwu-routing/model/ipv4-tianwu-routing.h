/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
#ifndef IPV4_TIANWU_ROUTING_H
#define IPV4_TIANWU_ROUTING_H

#include "ns3/ipv4-routing-protocol.h"
#include "ns3/ipv4-route.h"
#include "ns3/object.h"
#include "ns3/packet.h"
#include "ns3/ipv4-header.h"
#include "ns3/data-rate.h"
#include "ns3/nstime.h"
#include "ns3/event-id.h"

namespace ns3 {

struct TianWuFlowlet {
  uint32_t port;
  Time activeTime;
  int lastSeen;
  Time lastSeenTime;
};

struct TianWuRouteEntry {
  Ipv4Address network;
  Ipv4Mask networkMask;
  uint32_t port;
};

struct TianWuRouteFlow {
  Ipv4Address network1;
  Ipv4Address network2;
  Ipv4Mask networkMask;
  uint32_t flowid;
};

class Ipv4TianWuRouting : public Ipv4RoutingProtocol
{
public:
  Ipv4TianWuRouting ();
  ~Ipv4TianWuRouting ();

  static TypeId GetTypeId (void);
  static int tianwuid;
  int t_id;

  void AddRoute (Ipv4Address network, Ipv4Mask networkMask, uint32_t port);

  /* Inherit From Ipv4RoutingProtocol */
  virtual Ptr<Ipv4Route> RouteOutput (Ptr<Packet> p, const Ipv4Header &header, Ptr<NetDevice> oif, Socket::SocketErrno &sockerr);
  virtual bool RouteInput (Ptr<const Packet> p, const Ipv4Header &header, Ptr<const NetDevice> idev,
                           UnicastForwardCallback ucb, MulticastForwardCallback mcb,
                           LocalDeliverCallback lcb, ErrorCallback ecb);
  virtual void NotifyInterfaceUp (uint32_t interface);
  virtual void NotifyInterfaceDown (uint32_t interface);
  virtual void NotifyAddAddress (uint32_t interface, Ipv4InterfaceAddress address);
  virtual void NotifyRemoveAddress (uint32_t interface, Ipv4InterfaceAddress address);
  virtual void SetIpv4 (Ptr<Ipv4> ipv4);
  virtual void PrintRoutingTable (Ptr<OutputStreamWrapper> stream) const;

  uint32_t CalculateQueueLength (uint32_t interface);
  

  virtual void DoDispose (void);

  std::vector<TianWuRouteEntry> LookupTianWuRouteEntries (Ipv4Address dest);
  Ptr<Ipv4Route> ConstructIpv4Route (uint32_t port, Ipv4Address destAddress);

  void SetFlowletTimeout (Time timeout);
  void SetTianwuParas (double max, double min, uint64_t speed, uint32_t freq, uint32_t leaf);
  void SetChangeAble ();
  void CalculateUtilized();
  std::vector<int> m_underUtilizedPortSet;
  std::vector<int> m_highUtilizedPortSet;

  std::map<uint32_t, std::vector<TianWuRouteFlow>> m_flowPort;
  std::vector<uint32_t> m_flowSeen;

  std::map<uint32_t, std::vector<TianWuRouteFlow>> m_flowPortOld;
  std::vector<uint32_t> m_flowSeenOld;

  std::map<int, uint32_t> m_portTransmit;
  int changeAble;

private:
  // Flowlet Timeout
  Time m_flowletTimeout;
  
  uint32_t m_trans ;
  double m_max;
  double m_min;
  uint64_t m_spine_speed;
  uint32_t m_sched_freq;
  uint32_t is_leaf;

  // Ipv4 associated with this router
  Ptr<Ipv4> m_ipv4;

  // Flowlet Table
  std::map<uint32_t, TianWuFlowlet> m_flowletTable;

  // Route table
  std::vector<TianWuRouteEntry> m_routeEntryList;
};

}

#endif /* TIANWU_ROUTING_H */

