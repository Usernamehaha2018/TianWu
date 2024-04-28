loads=("0.8")
# loads=("0.05")
# algs=("ECMP" "Clove" "TianWu" "DRILL" "LetFlow")
algs=("ECMP" "LetFlow")
# algs=( "DRILL" "LetFlow")
# algs=("TianWu")
# workloads = ("datamining", "ml", "websearch")
seeds=("12")

workloads=("hadoop")
for load in ${loads[@]}; do
    for alg in ${algs[@]}; do
        for seed in ${seeds[@]}; do
	        for workload in ${workloads[@]}; do
                (time ./waf --run "conga-simulation-large --ID=test-$workload --load=$load --runMode=$alg --transportProt=DcTcp --cdfFileName=mix/$workload.txt --randomSeed=$seed --FlowLaunchEndTime=0.0005 --leafServerCapacity=100 --spineLeafCapacity=100 ";) &
                sleep 1
            done
	    done
    done
done
