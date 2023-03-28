/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */

#include "ipv4-tianwu-routing-helper.h"
#include "ns3/log.h"

namespace ns3 {

NS_LOG_COMPONENT_DEFINE ("Ipv4DTianWuRoutingHelper");

Ipv4TianWuRoutingHelper::Ipv4TianWuRoutingHelper ()
{

}

Ipv4TianWuRoutingHelper::Ipv4TianWuRoutingHelper (const Ipv4TianWuRoutingHelper&)
{

}

Ipv4TianWuRoutingHelper*
Ipv4TianWuRoutingHelper::Copy (void) const
{
  return new Ipv4TianWuRoutingHelper (*this);
}

Ptr<Ipv4RoutingProtocol>
Ipv4TianWuRoutingHelper::Create (Ptr<Node> node) const
{
  Ptr<Ipv4TianWuRouting> tianWuRouting = CreateObject<Ipv4TianWuRouting> ();
  return tianWuRouting;
}

Ptr<Ipv4TianWuRouting>
Ipv4TianWuRoutingHelper::GetTianWuRouting (Ptr<Ipv4> ipv4) const
{
  Ptr<Ipv4RoutingProtocol> ipv4rp = ipv4->GetRoutingProtocol ();
  if (DynamicCast<Ipv4TianWuRouting> (ipv4rp))
  {
    return DynamicCast<Ipv4TianWuRouting> (ipv4rp);
  }
  if (DynamicCast<Ipv4ListRouting> (ipv4rp))
  {
    Ptr<Ipv4ListRouting> lrp = DynamicCast<Ipv4ListRouting> (ipv4rp);
    int16_t priority;
    for (uint32_t i = 0; i < lrp->GetNRoutingProtocols ();  i++)
    {
      Ptr<Ipv4RoutingProtocol> temp = lrp->GetRoutingProtocol (i, priority);
      if (DynamicCast<Ipv4TianWuRouting> (temp))
      {
        return DynamicCast<Ipv4TianWuRouting> (temp);
      }
    }
  }

  return 0;
}

}

