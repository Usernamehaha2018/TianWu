# loads=("0.6" "0.7" "0.8")
loads=("0.7")
# algs=("ECMP" "Clove" "TianWu" "DRILL" "LetFlow")
algs=("ECMP" "Clove" "TianWu" "DRILL" "LetFlow")
# workloads = ("datamining", "ml", "websearch")
workloads=("datamining")
for load in ${loads[@]}; do
    for alg in ${algs[@]}; do
	    for workload in ${workloads[@]}; do
            (time ./waf --run "conga-simulation-large --load=$load --runMode=$alg --transportProt=DcTcp --cdfFileName=mix/$workload.txt --randomSeed=1";) &
            sleep 2
	    done
    done
done