#!/bin/bash

set -e -x

K="3"
if [ ! -z $1 ]; then
    K=$1
fi

TMP_DIR='./tmp/'
ALL_DATA=${TMP_DIR}'samples.txt'
CENTER='raw_clusters.txt'
TMP_CENTER=${TMP_DIR}${CENTER}

rm -rf ${TMP_DIR}
mkdir ${TMP_DIR}
hdfs dfs -get kmeans/samples.txt ${TMP_DIR}
./get_raw_cluster.py $K ${ALL_DATA} >> ${TMP_CENTER}
hdfs dfs -rm -r -f  -skipTrash 'kmeans/'${CENTER}
hdfs dfs -put ${TMP_CENTER} kmeans

