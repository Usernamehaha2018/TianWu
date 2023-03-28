/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
#ifndef IPV4_TIANWU_ROUTING_HELPER_H
#define IPV4_TIANWU_ROUTING_HELPER_H

#include "ns3/ipv4-tianwu-routing.h"
#include "ns3/ipv4-routing-helper.h"

namespace ns3 {

class Ipv4TianWuRoutingHelper : public Ipv4RoutingHelper
{
public:
    Ipv4TianWuRoutingHelper ();
    Ipv4TianWuRoutingHelper (const Ipv4TianWuRoutingHelper&);

    Ipv4TianWuRoutingHelper *Copy (void) const;

    virtual Ptr<Ipv4RoutingProtocol> Create (Ptr<Node> node) const;

    Ptr<Ipv4TianWuRouting> GetTianWuRouting (Ptr<Ipv4> ipv4) const;
};

}

#endif /* TIANWU_ROUTING_HELPER_H */

