set -e -x

# set K
K="3"
if [ ! -z "$1" ]; then
    K=$1
fi

# set T
T="9"
if [ ! -z "$2" ]; then
    T=$2
fi

#set path
HADOOP="/opt/hadoop-2.7.4/"
HADOOP_BIN=${HADOOP}"bin/"
STREAM_JAR_PATH=${HADOOP}"share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar"

INPUT_FILE='samples.txt'
CENTER_FILE='raw_clusters.txt'
HDFS_PATH="hdfs://localhost:9000"
PROJ_PATH="/user/huhu/kmeans/"
INPUT_PATH=${PROJ_PATH}${INPUT_FILE}
OUTPUT_PATH_0=${PROJ_PATH}"output-"
CENTER_PATH=${PROJ_PATH}${CENTER_FILE}

TMP_DIR='./tmp/'
TMP_DATA=${TMP_DIR}${INPUT_FILE}
TMP_CENTER=${TMP_DIR}${CENTER_FILE}

# initial and random select centers
rm -rf ${TMP_DIR}
mkdir ${TMP_DIR}
hdfs dfs -get ${INPUT_PATH} ${TMP_DIR}
python3 get_raw_cluster.py $K ${TMP_DATA} >> ${TMP_CENTER}
hdfs dfs -rm -r -f  -skipTrash ${CENTER_PATH}
hdfs dfs -put ${TMP_CENTER} kmeans

# mapreduce
for t in `seq 1 $T`
do
    if [ $t -eq "1" ]; then 
        OLD_OUTPUT_PATH=${HDFS_PATH}${CENTER_PATH}
        old_path=${TMP_CENTER}
    else
        OLD_OUTPUT_PATH=${HDFS_PATH}${OUTPUT_PATH}"/part-00000"
        old_path='tmp/output-'$[t-1]'/part-00000'
    fi
    OUTPUT_PATH=$OUTPUT_PATH_0$t

    ${HADOOP_BIN}"hdfs" dfs -rm -r -f  -skipTrash $OUTPUT_PATH

    ${HADOOP_BIN}"hadoop" jar $STREAM_JAR_PATH \
        -files ${OLD_OUTPUT_PATH}"#CENTER","map.py","com.py","red.py" \
        -D mapreduce.job.name="kmeans-"$t"-"$T \
        -input $INPUT_PATH \
        -output $OUTPUT_PATH \
        -mapper "python3 map.py CENTER " \
        -combiner "python3 com.py" \
        -reducer "python3 red.py" 

    hdfs dfs -get $OUTPUT_PATH './tmp'

    ./diff.py ${old_path} 'tmp/output-'$t'/part-00000'
    if [ -f 'tmp/123' ]; then
        echo 'T='$T', t='$t' ok!'
        break
    fi
done

