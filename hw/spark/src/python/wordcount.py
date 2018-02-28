
import pyspark
import jieba
jieba.initialize()

HOME = '/home/huhu/workspace/test/'
stop_file = HOME + 'stopwords.txt'
stop_words = set(' ')
with open(stop_file, 'r') as f:
    for line in f:
        stop_words.add(line.strip())

sc = pyspark.SparkContext(appName='wordcount')
full_data = sc.textFile('file:///home/huhu/data/FBDP/proj1/fulldata.txt')

ans = full_data.flatMap( 
        lambda x: jieba.cut(' '.join(x.split()[4:-1]))
    ).filter(
        lambda x: x not in stop_words 
    ).map( 
        lambda x: (x, 1)
    ).reduceByKey( 
        lambda x, y: x + y
    ).map( 
        lambda x: (x[1], x[0])
    ).sortByKey(False)

data = ans.collect()
ans.saveAsTextFile('file:///home/huhu/output')

# Spark SQL

from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, IntegerType

spark = SparkSession \
          .builder \
          .appName("Python Spark SQL basic example") \
          .config("spark.some.config.option", "some-value") \
          .getOrCreate()

fields = [StructField('count', IntegerType(), True), StructField('word', StringType(), True)]
schema = StructType(fields)
schemaWord = spark.createDataFrame(ans, schema)
schemaWord.createOrReplaceTempView("news")
results = spark.sql("SELECT * FROM news where count >= 900 and count < 1010")
results.show()
sc.stop()
