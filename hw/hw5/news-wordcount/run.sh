set -e -x

HADOOP="/opt/hadoop-2.7.4/"
HADOOP_BIN=${HADOOP}"bin/"
STREAM_JAR_PATH=${HADOOP}"share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar"

PROJ_PATH="/user/huhu/proj_wc/"
INPUT_PATH=${PROJ_PATH}"input"
OUTPUT_PATH_T=${PROJ_PATH}"outputwc"
OUTPUT_PATH=${PROJ_PATH}"outputsort"
DATA_PATH="hdfs://localhost:9000/user/huhu/data/"

${HADOOP_BIN}"hdfs" dfs -rm -r -f  -skipTrash $OUTPUT_PATH_T
${HADOOP_BIN}"hdfs" dfs -rm -r -f  -skipTrash $OUTPUT_PATH

${HADOOP_BIN}"hadoop" jar $STREAM_JAR_PATH \
    -files ${DATA_PATH}"stopwords.txt#STOP","map_word.py","combine_word.py","filter_word.py" \
    -D mapreduce.job.name="wordcount-mysum" \
    -input $INPUT_PATH \
    -output $OUTPUT_PATH_T \
    -mapper "python3 map_word.py STOP" \
    -combiner "python3 combine_word.py " \
    -reducer "python3 filter_word.py ""$*"  \

${HADOOP_BIN}"hadoop" jar $STREAM_JAR_PATH \
    -files "./t1map.py","./t1red.py" \
    -D mapreduce.job.name="wordcount-sort-reducer1" \
    -D stream.num.map.output.key.fields=2 \
    -D mapreduce.partition.keycomparator.options=-k1,2 \
    -D mapred.reduce.tasks=1 \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -input $OUTPUT_PATH_T \
    -output $OUTPUT_PATH \
    -mapper "python3 t1map.py" \
    -reducer "python3 t1red.py" \

