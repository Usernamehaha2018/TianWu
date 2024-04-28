loads=( "0.5 0.8")
algs=("TianWu" )
# algs=( "DRILL" "LetFlow")
# algs=("TianWu")
# workloads = ("datamining", "ml", "websearch")
seeds=("11")

workloads=("hadoop")
for load in ${loads[@]}; do
    for alg in ${algs[@]}; do
        for seed in ${seeds[@]}; do
	        for workload in ${workloads[@]}; do
                # (time ./waf --run "conga-simulation-large --ID=$workload --load=$load --runMode=$alg --transportProt=DcTcp --cdfFileName=mix/$workload.txt --randomSeed=$seed --FlowLaunchEndTime=0.15 --serverCount=32 --spineLeafCapacity=40 --spineCount=4 --leafCount=4";) &
                (time ./waf --run "conga-simulation-large --ID=$workload --load=$load --runMode=$alg --transportProt=DcTcp --cdfFileName=mix/$workload.txt --randomSeed=$seed --FlowLaunchEndTime=0.005 --spineLeafCapacity=100 --leafServerCapacity=100 --tianWuFlowletTimeout=200  --tianWuSchedFreq=20";) &
                sleep 2
            done
	    done
    done
done