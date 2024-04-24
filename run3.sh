./waf --run "conga-simulation-large --ID=test2 --load=0.8 --runMode=LetFlow --transportProt=DcTcp --cdfFileName=mix/hadoop.txt --randomSeed=100 --FlowLaunchEndTime=0.0005 --leafServerCapacity=100 --spineLeafCapacity=100 --tianWuFlowletTimeout=100 --tianWuSchedFreq=10" &

./waf --run "conga-simulation-large --ID=test2 --load=0.8 --runMode=TianWu --transportProt=DcTcp --cdfFileName=mix/hadoop.txt --randomSeed=100 --FlowLaunchEndTime=0.0005 --leafServerCapacity=100 --spineLeafCapacity=100 --tianWuFlowletTimeout=100 --tianWuSchedFreq=10" &

./waf --run "conga-simulation-large --ID=test2 --load=0.8 --runMode=ECMP --transportProt=DcTcp --cdfFileName=mix/hadoop.txt --randomSeed=100 --FlowLaunchEndTime=0.0005 --leafServerCapacity=100 --spineLeafCapacity=100 --tianWuFlowletTimeout=100 --tianWuSchedFreq=10" &
