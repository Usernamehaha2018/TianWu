loads=("0.4" "0.5")
algs=("ECMP" "Clove" "TianWu" "DRILL" "LetFlow")
# workloads = ("datamining", "ml", "websearch")
workloads=("datamining")
for load in ${loads[@]}; do
    for alg in ${algs[@]}; do
	    for workload in ${workloads[@]}; do
            (time ./waf --run "conga-simulation-large --load=$load --runMode=$alg --cdfFileName=mix/$workload.txt --randomSeed=4";) &
            sleep 2
	    done
    done
done