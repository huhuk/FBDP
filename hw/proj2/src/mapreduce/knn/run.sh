set -e -x

HADOOP="/opt/hadoop-2.7.4/"
HADOOP_BIN=${HADOOP}"bin/"
STREAM_JAR_PATH=${HADOOP}"share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar"

PROJ_PATH="/user/huhu/test/"
INPUT_PATH=${PROJ_PATH}"test"
OUTPUT_PATH=${PROJ_PATH}"predict_ans"
DATA_PATH="hdfs://localhost:9000/user/huhu/data/"

${HADOOP_BIN}"hdfs" dfs -rm -r -f  -skipTrash $OUTPUT_PATH

${HADOOP_BIN}"hadoop" jar $STREAM_JAR_PATH \
    -files './map.py','./red.py','./tfidf.model','./x_train.model','./y_train.model','./x_test.model' \
    -D mapreduce.job.name="predict" \
    -D mapreduce.job.reduces=0 \
    -input $INPUT_PATH \
    -output $OUTPUT_PATH \
    -mapper 'python3 map.py' \
    -reducer 'python3 red.py'

    # key fields: mapper output(default first tab) -> reducer key \t value
    #-D stream.map.output.field.separator=. \
    #-D stream.num.map.output.key.fields=4 \

    # KeyFieldBasedComparator
    # the Map/Reduce framework will sort the outputs by the second field of the keys 
    # -n specifies that the sorting is numerical sorting and -r specifies that the result should be reversed
    #-D mapreduce.map.output.key.field.separator=, \
    #-D mapreduce.partition.keycomparator.options=-k2,2nr \
    #-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \

    # KeyFieldBasedPartitioner
    # map.output.key.field.separator=. specifies the separator for the partition
    # the Map/Reduce framework will partition the map outputs by the first two fields of the keys
    #-D map.output.key.field.separator=. \
    #-D mapreduce.partition.keypartitioner.options=-k1,2 \
    #-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \

    # all sort: diy partitioner
    #-D num.key.fields.for.partition=1 \
    #-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \

    # reducer number or Map-Only Jobs
    #-D mapreduce.job.reduces=1 \
    # old
    #-D mapred.reduce.tasks=1 \

    # aggregate
    # -mapper ''
    # -combiner aggregate \
    # -reducer aggregate \

    # "$*"

