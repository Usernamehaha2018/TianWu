loads=( "0.8")
# loads=("0.05")
# algs=("ECMP" "Clove" "TianWu" "DRILL" "LetFlow")
algs=( "ECMP" "Clove" "DRILL" "LetFlow" )
# algs=("TianWu")
# workloads = ("datamining", "ml", "websearch")
seeds=("7" "8")

workloads=("datamining")
for load in ${loads[@]}; do
    for alg in ${algs[@]}; do
        for seed in ${seeds[@]}; do
	        for workload in ${workloads[@]}; do
                (time ./waf --run "conga-simulation-large --ID=$workload --load=$load --runMode=$alg --transportProt=DcTcp --cdfFileName=mix/$workload.txt --randomSeed=$seed --FlowLaunchEndTime=0.5 --serverCount=8 --spineLeafCapacity=10 --spineCount=4 --leafCount=4";) &
                sleep 2
            done
	    done
    done
done