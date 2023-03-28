#! /usr/bin/env python

# Programs that are runnable.
ns3_runnable_programs = ['build/src/aodv/examples/ns3-dev-aodv-optimized', 'build/src/bridge/examples/ns3-dev-csma-bridge-optimized', 'build/src/bridge/examples/ns3-dev-csma-bridge-one-hop-optimized', 'build/src/buildings/examples/ns3-dev-buildings-pathloss-profiler-optimized', 'build/src/clove/examples/ns3-dev-clove-example-optimized', 'build/src/config-store/examples/ns3-dev-config-store-save-optimized', 'build/src/conga-routing/examples/ns3-dev-ipv4-conga-routing-example-optimized', 'build/src/congestion-probing/examples/ns3-dev-congestion-probing-example-optimized', 'build/src/core/examples/ns3-dev-main-callback-optimized', 'build/src/core/examples/ns3-dev-sample-simulator-optimized', 'build/src/core/examples/ns3-dev-main-ptr-optimized', 'build/src/core/examples/ns3-dev-main-random-variable-optimized', 'build/src/core/examples/ns3-dev-main-random-variable-stream-optimized', 'build/src/core/examples/ns3-dev-sample-random-variable-optimized', 'build/src/core/examples/ns3-dev-sample-random-variable-stream-optimized', 'build/src/core/examples/ns3-dev-command-line-example-optimized', 'build/src/core/examples/ns3-dev-hash-example-optimized', 'build/src/core/examples/ns3-dev-main-test-sync-optimized', 'build/src/csma/examples/ns3-dev-csma-one-subnet-optimized', 'build/src/csma/examples/ns3-dev-csma-broadcast-optimized', 'build/src/csma/examples/ns3-dev-csma-packet-socket-optimized', 'build/src/csma/examples/ns3-dev-csma-multicast-optimized', 'build/src/csma/examples/ns3-dev-csma-raw-ip-socket-optimized', 'build/src/csma/examples/ns3-dev-csma-ping-optimized', 'build/src/csma-layout/examples/ns3-dev-csma-star-optimized', 'build/src/drb-routing/examples/ns3-dev-drb-routing-example-optimized', 'build/src/drill-routing/examples/ns3-dev-drill-routing-example-optimized', 'build/src/dsdv/examples/ns3-dev-dsdv-manet-optimized', 'build/src/dsr/examples/ns3-dev-dsr-optimized', 'build/src/energy/examples/ns3-dev-li-ion-energy-source-optimized', 'build/src/energy/examples/ns3-dev-rv-battery-model-test-optimized', 'build/src/energy/examples/ns3-dev-basic-energy-model-test-optimized', 'build/src/fd-net-device/examples/ns3-dev-dummy-network-optimized', 'build/src/fd-net-device/examples/ns3-dev-fd2fd-onoff-optimized', 'build/src/fd-net-device/examples/ns3-dev-realtime-dummy-network-optimized', 'build/src/fd-net-device/examples/ns3-dev-realtime-fd2fd-onoff-optimized', 'build/src/fd-net-device/examples/ns3-dev-fd-emu-ping-optimized', 'build/src/fd-net-device/examples/ns3-dev-fd-emu-udp-echo-optimized', 'build/src/fd-net-device/examples/ns3-dev-fd-emu-onoff-optimized', 'build/src/fd-net-device/examples/ns3-dev-fd-tap-ping-optimized', 'build/src/fd-net-device/examples/ns3-dev-fd-tap-ping6-optimized', 'build/src/internet/examples/ns3-dev-main-simple-optimized', 'build/src/letflow-routing/examples/ns3-dev-letflow-routing-example-optimized', 'build/src/link-monitor/examples/ns3-dev-link-monitor-example-optimized', 'build/src/lr-wpan/examples/ns3-dev-lr-wpan-packet-print-optimized', 'build/src/lr-wpan/examples/ns3-dev-lr-wpan-phy-test-optimized', 'build/src/lr-wpan/examples/ns3-dev-lr-wpan-data-optimized', 'build/src/lr-wpan/examples/ns3-dev-lr-wpan-error-model-plot-optimized', 'build/src/lr-wpan/examples/ns3-dev-lr-wpan-error-distance-plot-optimized', 'build/src/lte/examples/ns3-dev-lena-cqi-threshold-optimized', 'build/src/lte/examples/ns3-dev-lena-dual-stripe-optimized', 'build/src/lte/examples/ns3-dev-lena-fading-optimized', 'build/src/lte/examples/ns3-dev-lena-intercell-interference-optimized', 'build/src/lte/examples/ns3-dev-lena-pathloss-traces-optimized', 'build/src/lte/examples/ns3-dev-lena-profiling-optimized', 'build/src/lte/examples/ns3-dev-lena-rem-optimized', 'build/src/lte/examples/ns3-dev-lena-rem-sector-antenna-optimized', 'build/src/lte/examples/ns3-dev-lena-rlc-traces-optimized', 'build/src/lte/examples/ns3-dev-lena-simple-optimized', 'build/src/lte/examples/ns3-dev-lena-simple-epc-optimized', 'build/src/lte/examples/ns3-dev-lena-deactivate-bearer-optimized', 'build/src/lte/examples/ns3-dev-lena-x2-handover-optimized', 'build/src/lte/examples/ns3-dev-lena-x2-handover-measures-optimized', 'build/src/lte/examples/ns3-dev-lena-frequency-reuse-optimized', 'build/src/lte/examples/ns3-dev-lena-distributed-ffr-optimized', 'build/src/lte/examples/ns3-dev-lena-uplink-power-control-optimized', 'build/src/mesh/examples/ns3-dev-mesh-optimized', 'build/src/mobility/examples/ns3-dev-main-grid-topology-optimized', 'build/src/mobility/examples/ns3-dev-main-random-topology-optimized', 'build/src/mobility/examples/ns3-dev-main-random-walk-optimized', 'build/src/mobility/examples/ns3-dev-mobility-trace-example-optimized', 'build/src/mobility/examples/ns3-dev-ns2-mobility-trace-optimized', 'build/src/mobility/examples/ns3-dev-bonnmotion-ns2-example-optimized', 'build/src/mpi/examples/ns3-dev-simple-distributed-optimized', 'build/src/mpi/examples/ns3-dev-third-distributed-optimized', 'build/src/mpi/examples/ns3-dev-nms-p2p-nix-distributed-optimized', 'build/src/mpi/examples/ns3-dev-simple-distributed-empty-node-optimized', 'build/src/netanim/examples/ns3-dev-dumbbell-animation-optimized', 'build/src/netanim/examples/ns3-dev-grid-animation-optimized', 'build/src/netanim/examples/ns3-dev-star-animation-optimized', 'build/src/netanim/examples/ns3-dev-wireless-animation-optimized', 'build/src/netanim/examples/ns3-dev-uan-animation-optimized', 'build/src/netanim/examples/ns3-dev-colors-link-description-optimized', 'build/src/netanim/examples/ns3-dev-resources-counters-optimized', 'build/src/network/examples/ns3-dev-main-packet-header-optimized', 'build/src/network/examples/ns3-dev-main-packet-tag-optimized', 'build/src/network/examples/ns3-dev-packet-socket-apps-optimized', 'build/src/nix-vector-routing/examples/ns3-dev-nix-simple-optimized', 'build/src/nix-vector-routing/examples/ns3-dev-nms-p2p-nix-optimized', 'build/src/olsr/examples/ns3-dev-simple-point-to-point-olsr-optimized', 'build/src/olsr/examples/ns3-dev-olsr-hna-optimized', 'build/src/point-to-point/examples/ns3-dev-main-attribute-value-optimized', 'build/src/propagation/examples/ns3-dev-main-propagation-loss-optimized', 'build/src/propagation/examples/ns3-dev-jakes-propagation-model-example-optimized', 'build/src/sixlowpan/examples/ns3-dev-example-sixlowpan-optimized', 'build/src/sixlowpan/examples/ns3-dev-example-ping-lr-wpan-optimized', 'build/src/spectrum/examples/ns3-dev-adhoc-aloha-ideal-phy-optimized', 'build/src/spectrum/examples/ns3-dev-adhoc-aloha-ideal-phy-matrix-propagation-loss-model-optimized', 'build/src/spectrum/examples/ns3-dev-adhoc-aloha-ideal-phy-with-microwave-oven-optimized', 'build/src/spectrum/examples/ns3-dev-tv-trans-example-optimized', 'build/src/spectrum/examples/ns3-dev-tv-trans-regional-example-optimized', 'build/src/stats/examples/ns3-dev-gnuplot-example-optimized', 'build/src/stats/examples/ns3-dev-double-probe-example-optimized', 'build/src/stats/examples/ns3-dev-time-probe-example-optimized', 'build/src/stats/examples/ns3-dev-gnuplot-aggregator-example-optimized', 'build/src/stats/examples/ns3-dev-gnuplot-helper-example-optimized', 'build/src/stats/examples/ns3-dev-file-aggregator-example-optimized', 'build/src/stats/examples/ns3-dev-file-helper-example-optimized', 'build/src/tap-bridge/examples/ns3-dev-tap-csma-optimized', 'build/src/tap-bridge/examples/ns3-dev-tap-csma-virtual-machine-optimized', 'build/src/tap-bridge/examples/ns3-dev-tap-wifi-virtual-machine-optimized', 'build/src/tap-bridge/examples/ns3-dev-tap-wifi-dumbbell-optimized', 'build/src/tianwu-routing/examples/ns3-dev-tianwu-routing-example-optimized', 'build/src/tlb/examples/ns3-dev-tlb-example-optimized', 'build/src/tlb-probing/examples/ns3-dev-tlb-probing-example-optimized', 'build/src/topology-read/examples/ns3-dev-topology-example-sim-optimized', 'build/src/traffic-control/examples/ns3-dev-red-tests-optimized', 'build/src/traffic-control/examples/ns3-dev-red-vs-ared-optimized', 'build/src/traffic-control/examples/ns3-dev-adaptive-red-tests-optimized', 'build/src/traffic-control/examples/ns3-dev-pfifo-vs-red-optimized', 'build/src/traffic-control/examples/ns3-dev-codel-vs-pfifo-basic-test-optimized', 'build/src/traffic-control/examples/ns3-dev-codel-vs-pfifo-asymmetric-optimized', 'build/src/uan/examples/ns3-dev-uan-cw-example-optimized', 'build/src/uan/examples/ns3-dev-uan-rc-example-optimized', 'build/src/virtual-net-device/examples/ns3-dev-virtual-net-device-optimized', 'build/src/wave/examples/ns3-dev-wave-simple-80211p-optimized', 'build/src/wave/examples/ns3-dev-wave-simple-device-optimized', 'build/src/wave/examples/ns3-dev-vanet-routing-compare-optimized', 'build/src/wifi/examples/ns3-dev-wifi-phy-test-optimized', 'build/src/wifi/examples/ns3-dev-test-interference-helper-optimized', 'build/src/wifi/examples/ns3-dev-ideal-wifi-manager-example-optimized', 'build/src/wifi/examples/ns3-dev-minstrel-ht-wifi-manager-example-optimized', 'build/src/wimax/examples/ns3-dev-wimax-ipv4-optimized', 'build/src/wimax/examples/ns3-dev-wimax-multicast-optimized', 'build/src/wimax/examples/ns3-dev-wimax-simple-optimized', 'build/src/xpath-routing/examples/ns3-dev-xpath-routing-example-optimized', 'build/examples/udp-client-server/ns3-dev-udp-client-server-optimized', 'build/examples/udp-client-server/ns3-dev-udp-trace-client-server-optimized', 'build/examples/traffic-control/ns3-dev-traffic-control-optimized', 'build/examples/load-balance/ns3-dev-dctcp-drb-original-optimized', 'build/examples/load-balance/ns3-dev-conga-simulation-optimized', 'build/examples/load-balance/ns3-dev-conga-flowlet-test-optimized', 'build/examples/load-balance/ns3-dev-conga-simulation-large-optimized', 'build/examples/load-balance/ns3-dev-spark-shuffle-optimized', 'build/examples/load-balance/ns3-dev-xpath-routing-optimized', 'build/examples/load-balance/ns3-dev-tlb-simulation-optimized', 'build/examples/load-balance/ns3-dev-tlb-ecmp-simulation-optimized', 'build/examples/load-balance/ns3-dev-tlb-drb-simulation-optimized', 'build/examples/load-balance/ns3-dev-tlb-conga-simulation-optimized', 'build/examples/load-balance/ns3-dev-fattree-simulation-optimized', 'build/examples/stats/ns3-dev-wifi-example-sim-optimized', 'build/examples/routing/ns3-dev-dynamic-global-routing-optimized', 'build/examples/routing/ns3-dev-static-routing-slash32-optimized', 'build/examples/routing/ns3-dev-global-routing-slash32-optimized', 'build/examples/routing/ns3-dev-global-injection-slash32-optimized', 'build/examples/routing/ns3-dev-simple-global-routing-optimized', 'build/examples/routing/ns3-dev-simple-alternate-routing-optimized', 'build/examples/routing/ns3-dev-mixed-global-routing-optimized', 'build/examples/routing/ns3-dev-simple-routing-ping6-optimized', 'build/examples/routing/ns3-dev-manet-routing-compare-optimized', 'build/examples/routing/ns3-dev-ripng-simple-network-optimized', 'build/examples/routing/ns3-dev-rip-simple-network-optimized', 'build/examples/routing/ns3-dev-global-routing-multi-switch-plus-router-optimized', 'build/examples/routing/ns3-dev-per-flow-ecmp-routing-optimized', 'build/examples/routing/ns3-dev-drb-routing-optimized', 'build/examples/matrix-topology/ns3-dev-matrix-topology-optimized', 'build/examples/energy/ns3-dev-energy-model-example-optimized', 'build/examples/energy/ns3-dev-energy-model-with-harvesting-example-optimized', 'build/examples/realtime/ns3-dev-realtime-udp-echo-optimized', 'build/examples/udp/ns3-dev-udp-echo-optimized', 'build/examples/error-model/ns3-dev-simple-error-model-optimized', 'build/examples/tutorial/ns3-dev-hello-simulator-optimized', 'build/examples/tutorial/ns3-dev-first-optimized', 'build/examples/tutorial/ns3-dev-second-optimized', 'build/examples/tutorial/ns3-dev-third-optimized', 'build/examples/tutorial/ns3-dev-fourth-optimized', 'build/examples/tutorial/ns3-dev-fifth-optimized', 'build/examples/tutorial/ns3-dev-sixth-optimized', 'build/examples/tutorial/ns3-dev-seventh-optimized', 'build/examples/ipv6/ns3-dev-icmpv6-redirect-optimized', 'build/examples/ipv6/ns3-dev-ping6-optimized', 'build/examples/ipv6/ns3-dev-radvd-optimized', 'build/examples/ipv6/ns3-dev-radvd-two-prefix-optimized', 'build/examples/ipv6/ns3-dev-test-ipv6-optimized', 'build/examples/ipv6/ns3-dev-fragmentation-ipv6-optimized', 'build/examples/ipv6/ns3-dev-fragmentation-ipv6-two-MTU-optimized', 'build/examples/ipv6/ns3-dev-loose-routing-ipv6-optimized', 'build/examples/ipv6/ns3-dev-wsn-ping6-optimized', 'build/examples/tcp/ns3-dev-tcp-large-transfer-optimized', 'build/examples/tcp/ns3-dev-tcp-nsc-lfn-optimized', 'build/examples/tcp/ns3-dev-tcp-nsc-zoo-optimized', 'build/examples/tcp/ns3-dev-tcp-star-server-optimized', 'build/examples/tcp/ns3-dev-star-optimized', 'build/examples/tcp/ns3-dev-tcp-bulk-send-optimized', 'build/examples/tcp/ns3-dev-tcp-pcap-nanosec-example-optimized', 'build/examples/tcp/ns3-dev-tcp-nsc-comparison-optimized', 'build/examples/tcp/ns3-dev-tcp-variants-comparison-optimized', 'build/examples/wireless/ns3-dev-mixed-wireless-optimized', 'build/examples/wireless/ns3-dev-wifi-adhoc-optimized', 'build/examples/wireless/ns3-dev-wifi-clear-channel-cmu-optimized', 'build/examples/wireless/ns3-dev-wifi-ap-optimized', 'build/examples/wireless/ns3-dev-wifi-wired-bridging-optimized', 'build/examples/wireless/ns3-dev-multirate-optimized', 'build/examples/wireless/ns3-dev-wifi-simple-adhoc-optimized', 'build/examples/wireless/ns3-dev-wifi-simple-adhoc-grid-optimized', 'build/examples/wireless/ns3-dev-wifi-simple-infra-optimized', 'build/examples/wireless/ns3-dev-wifi-simple-interference-optimized', 'build/examples/wireless/ns3-dev-wifi-blockack-optimized', 'build/examples/wireless/ns3-dev-ofdm-validation-optimized', 'build/examples/wireless/ns3-dev-ofdm-ht-validation-optimized', 'build/examples/wireless/ns3-dev-ofdm-vht-validation-optimized', 'build/examples/wireless/ns3-dev-wifi-hidden-terminal-optimized', 'build/examples/wireless/ns3-dev-ht-wifi-network-optimized', 'build/examples/wireless/ns3-dev-vht-wifi-network-optimized', 'build/examples/wireless/ns3-dev-wifi-timing-attributes-optimized', 'build/examples/wireless/ns3-dev-wifi-sleep-optimized', 'build/examples/wireless/ns3-dev-power-adaptation-distance-optimized', 'build/examples/wireless/ns3-dev-power-adaptation-interference-optimized', 'build/examples/wireless/ns3-dev-rate-adaptation-distance-optimized', 'build/examples/wireless/ns3-dev-wifi-aggregation-optimized', 'build/examples/wireless/ns3-dev-simple-ht-hidden-stations-optimized', 'build/examples/wireless/ns3-dev-80211n-mimo-optimized', 'build/examples/wireless/ns3-dev-mixed-bg-network-optimized', 'build/examples/wireless/ns3-dev-wifi-tcp-optimized', 'build/examples/naming/ns3-dev-object-names-optimized', 'build/examples/socket/ns3-dev-socket-bound-static-routing-optimized', 'build/examples/socket/ns3-dev-socket-bound-tcp-static-routing-optimized', 'build/examples/socket/ns3-dev-socket-options-ipv4-optimized', 'build/examples/socket/ns3-dev-socket-options-ipv6-optimized', 'build/scratch/ns3-dev-hidden-terminal-optimized', 'build/scratch/subdir/ns3-dev-subdir-optimized', 'build/scratch/ns3-dev-scratch-simulator-optimized']

# Scripts that are runnable.
ns3_runnable_scripts = ['csma-bridge.py', 'sample-simulator.py', 'wifi-olsr-flowmon.py', 'tap-csma-virtual-machine.py', 'tap-wifi-virtual-machine.py', 'simple-routing-ping6.py', 'realtime-udp-echo.py', 'first.py', 'second.py', 'third.py', 'mixed-wireless.py', 'wifi-ap.py']

