loads=( "0.05")
# loads=("0.05")
# algs=("ECMP" "Clove" "TianWu" "DRILL" "LetFlow")
algs=( "ECMP" "Clove" "DRILL" "LetFlow" )
# algs=( "DRILL" "LetFlow")
# algs=("TianWu")
# workloads = ("datamining", "ml", "websearch")
seeds=("9")

workloads=("datamining")
for load in ${loads[@]}; do
    for alg in ${algs[@]}; do
        for seed in ${seeds[@]}; do
	        for workload in ${workloads[@]}; do
                (time ./waf --run "conga-simulation-large --ID=$workload --load=$load --runMode=$alg --transportProt=DcTcp --cdfFileName=mix/$workload.txt --randomSeed=$seed --FlowLaunchEndTime=0.15 --serverCount=32 --spineLeafCapacity=40 --spineCount=4 --leafCount=4";) &
                sleep 2
            done
	    done
    done
done