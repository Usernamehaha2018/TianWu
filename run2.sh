loads=("0.8")
# loads=("0.05")
# algs=("ECMP" "Clove" "TianWu" "DRILL" "LetFlow")
algs=(  "TianWu")
# algs=( "DRILL" "LetFlow")
# algs=("TianWu")
# workloads = ("datamining", "ml", "websearch")
seeds=("12")
timeouts=(200 250 300)
freqs=(5 10 15 20)

workloads=("hadoop")
for load in ${loads[@]}; do
    for alg in ${algs[@]}; do
        for seed in ${seeds[@]}; do
	        for workload in ${workloads[@]}; do
                for freq in ${freqs[@]}; do
                    for timeout in ${timeouts[@]}; do
                    # (time ./waf --run "conga-simulation-large --ID=$workload --load=$load --runMode=$alg --transportProt=DcTcp --cdfFileName=mix/$workload.txt --randomSeed=$seed --FlowLaunchEndTime=0.15 --serverCount=32 --spineLeafCapacity=40 --spineCount=4 --leafCount=4";) &
                        (time ./waf --run "conga-simulation-large --ID=$freq-$timeout-$workload --load=$load --runMode=$alg --transportProt=DcTcp --cdfFileName=mix/$workload.txt --randomSeed=$seed --FlowLaunchEndTime=0.0005 --leafServerCapacity=100 --spineLeafCapacity=100  --tianWuFlowletTimeout=$timeout --tianWuSchedFreq=$freq";) &
                        sleep 1
                    done
                done
            done
	    done
    done
done
