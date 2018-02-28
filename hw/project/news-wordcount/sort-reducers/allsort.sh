set -e -x

HADOOP="/opt/hadoop-2.7.4/"
HADOOP_BIN=${HADOOP}"bin/"
STREAM_JAR_PATH=${HADOOP}"share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar"

HDFS_PATH="hdfs://localhost:9000"
JOB_PATH="/user/huhu/test/"
INPUT_PATH=${JOB_PATH}"output_1"
OUTPUT_PATH_1=${JOB_PATH}"outputsort"

${HADOOP_BIN}"hdfs" dfs -rm -r -f  -skipTrash $OUTPUT_PATH_1

${HADOOP_BIN}"hadoop" jar $STREAM_JAR_PATH \
    -files './allmap.py','./allred.py' \
    -D stream.num.map.output.key.fields=2 \
    -D num.key.fields.for.partition=1 \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.partition.keycomparator.options=-k2nr \
    -D mapred.reduce.tasks=4 \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
    -input $INPUT_PATH \
    -output $OUTPUT_PATH_1 \
    -mapper "python3 allmap.py" \
    -reducer "python3 allred.py" 

