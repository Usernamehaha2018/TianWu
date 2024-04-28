loads=("0.8")
# loads=("0.05")
# algs=("ECMP" "Clove" "TianWu" "DRILL" "LetFlow")
algs=(  "TianWu")
# algs=( "DRILL" "LetFlow")
# algs=("TianWu")
# workloads = ("datamining", "ml", "websearch")
seeds=("100")
min_loads=( 0.5 0.6 0.7)
max_retoute=(0.2 0.3 0.4 0.5)

workloads=("hadoop")
for load in ${loads[@]}; do
    for alg in ${algs[@]}; do
        for seed in ${seeds[@]}; do
	        for workload in ${workloads[@]}; do
                for ml in ${min_loads[@]}; do
                    for mr in ${max_retoute[@]}; do
                    # (time ./waf --run "conga-simulation-large --ID=$workload --load=$load --runMode=$alg --transportProt=DcTcp --cdfFileName=mix/$workload.txt --randomSeed=$seed --FlowLaunchEndTime=0.15 --serverCount=32 --spineLeafCapacity=40 --spineCount=4 --leafCount=4";) &
                        (time ./waf --run "conga-simulation-large --ID=$ml-$mr-test --load=$load --runMode=$alg --transportProt=DcTcp --cdfFileName=mix/$workload.txt --randomSeed=$seed --FlowLaunchEndTime=0.005 --leafServerCapacity=100 --spineLeafCapacity=100  --tianWuFlowletTimeout=200 --tianWuSchedFreq=10 --tianWuMaxReroute=$mr --tianWuMin=$ml";) &
                        sleep 1
                    done
                done
            done
	    done
    done
done
