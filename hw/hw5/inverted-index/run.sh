set -e -x

HADOOP="/opt/hadoop-2.7.4/"
HADOOP_BIN=${HADOOP}"bin/"
STREAM_JAR_PATH=${HADOOP}"share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar"

DATA_PATH="hdfs://localhost:9000/user/huhu/data/"
JOB_PATH="/user/huhu/proj_ii/"
INPUT_PATH=${JOB_PATH}"input"
OUTPUT_PATH=${JOB_PATH}"output"

${HADOOP_BIN}"hdfs" dfs -rm -r -f  -skipTrash $OUTPUT_PATH

${HADOOP_BIN}"hadoop" jar $STREAM_JAR_PATH \
    -files ${DATA_PATH}"stopwords.txt#SKIP","map.py","red.py" \
    -D stream.num.map.output.key.fields=2 \
    -D mapreduce.partition.keypartitioner.options=-k1 \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
    -input $INPUT_PATH \
    -output $OUTPUT_PATH \
    -mapper "python3 map.py SKIP" \
    -reducer "python3 red.py " \

