loads=("0.8")
# loads=("0.05")
# algs=("ECMP" "Clove" "TianWu" "DRILL" "LetFlow")
algs=(  "TianWu")
# algs=( "DRILL" "LetFlow")
# algs=("TianWu")
# workloads = ("datamining", "ml", "websearch")
seeds=("100")
timeouts=(100 200 300)
freqs=(10 20)

workloads=("datamining")
for load in ${loads[@]}; do
    for alg in ${algs[@]}; do
        for seed in ${seeds[@]}; do
	        for workload in ${workloads[@]}; do
                for t in ${timeouts[@]}; do
                    for f in ${freqs[@]}; do
                    # (time ./waf --run "conga-simulation-large --ID=$workload --load=$load --runMode=$alg --transportProt=DcTcp --cdfFileName=mix/$workload.txt --randomSeed=$seed --FlowLaunchEndTime=0.15 --serverCount=32 --spineLeafCapacity=40 --spineCount=4 --leafCount=4";) &
                        (time ./waf --run "conga-simulation-large --ID=test-$workload --load=$load --runMode=$alg --transportProt=DcTcp --cdfFileName=mix/$workload.txt --randomSeed=$seed --FlowLaunchEndTime=0.01 --leafServerCapacity=100 --spineLeafCapacity=100  --tianWuFlowletTimeout=$t --tianWuSchedFreq=$f --tianWuMaxReroute=0.6 --tianWuMin=0.5";) &
                        sleep 1
                    done
                done
            done
	    done
    done
done
