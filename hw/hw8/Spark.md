[TOC]

# 作业8 Spark

- @author huhu

---

## 1. 简述为什么会有Spark

- 大数据时代

  ​	时下，我们正处在一个“大数据”的时代，每时每刻，都有各种类型的数据被生产，需要更好的技术从从海量数据中提取有用的信息。

- Hadoop计算框架的局限和不足

  ​	MapReduce 的数据处理流程中，中间结果会借助**磁盘传递**，因此对比计算，大量的Map-Reduced作业受限于IO。对于ETL、数据整合和清理这样的用例来说，IO约束并不会产生很大的影响，因为这些场景对数据处理时间往往不会有较高的需求。

  ​	然而，在现实世界中，同样存在许多**对延时要求较为苛刻的用例**，例如：对流数据进行处理来做近实时分析、在大型数据集上进行交互式分析。

  ​	因此人们开始关注大数据处理所需要的其他各种计算模式和系统，其中，**以内存计算为核心、集诸多计算模式之大成的Spark生态系统**应运而生。

- Spark 的出现

  ​	Spark 是加州大学伯克利分校AMP实验室2009年开发的通用内存并行计算框架，开源后成为Apache项目，围绕Spark推出了Spark SQL、Spark Streaming、MLlib 和 GraphX 等组件，逐渐形成大数据处理一站式解决平台。

- Spark 的特点： 

  - 快速高效

    数据被加载到集群主机的分布式内存中，可以被快速的转换迭代，并缓存用以后续的频繁访问需求。

    > Run programs up to 100x faster than Hadoop MapReduce in memory, or 10x faster on disk.
    >
    > Apache Spark has an advanced DAG execution engine that supports acyclic data flow and in-memory computing.

  - 易用

    通过建立在 Java、Scala、Python、SQL（应对交互式查询）的标准API以方便各行各业使用，，同时还含有大量开箱即用的机器学习库。

    > Write applications quickly in Java, Scala, Python, R.
    >
    > Spark offers over 80 high-level operators that make it easy to build parallel apps. And you can use it *interactively* from the Scala, Python and R shells.s

  - 生态系统

    > Combine SQL, streaming, and complex analytics.
    >
    > Spark powers a stack of libraries including [SQL and DataFrames](http://spark.apache.org/sql/), [MLlib](http://spark.apache.org/mllib/) for machine learning, [GraphX](http://spark.apache.org/graphx/), and [Spark Streaming](http://spark.apache.org/streaming/). You can combine these libraries seamlessly in the same application.

  - 随处可运行

    > Spark runs on Hadoop, Mesos, standalone, or in the cloud. It can access diverse data sources including HDFS, Cassandra, HBase, and S3.

---

## 2. 对比Hadoop和Spark

- I/O
  - Hadoop MapReduce 将计算结果输出到磁盘上，下一个任务再从磁盘上读取
  - Spark 把中间数据放在内存中，迭代运算效率高
- 计算模型
  - Spark 支持 DAG 图的分布式并行计算，减少了迭代过程中的数据落地，提高了处理效率
- 容错性
  - Spark 引入 RDD 抽象，通过 Lineage 计算时通过 CheckPoint （CheckPoint Data 和 Logging The Updates）来实现容错。
- 通用性
  - Hadoop 只提供 Map 和 Reduce 两种操作
  - Spark 提供的数据集操作类型很多。各个处理节点之间的通信模型不再像 Hadoop 只有 Shuffle 一种，用户可以命名、物化、控制中间结果的存储、分区等。

---

## 3. 简述Spark的技术特点

- RDD

  分布式数据集**Resilient Distributed Dataset**是Apache Spark的核心理念，它是由数据组成的不可变分布式集合，其主要进行两个操作： **transformation** 和 **action**。

  Spark Master/Driver会保存RDD上的Transformations。这样一来，如果某个RDD丢失（也就是salves宕掉），它可以快速和便捷地转换到集群中存活的主机上。这也就是RDD的弹性所在。

  - Transformation

    Transformation是在RDD上做 filter()、map()或union() 等以生成另一个RDD的操作，一般都是lazy的，直到action执行后才会被执行。

  - Action

    Action是count()、first()、take(n)、collect() 等触发一个计算并返回值到Master或者稳定存储系统的操作

  - Lineage

    为了保证RDD中数据的鲁棒性，Spark系统通过血统关系(lineage)来记录一个RDD是如何通过其他一个或者多个父类RDD转变过来的，当这个RDD的数据丢失时，Spark可以通过它父类的RDD重新计算。


  - CheckPoint

- Spark 调度

  Spark采用了事件驱动的 Scala 库类 Akka 来完成任务的启动，通过复用线程池的方式来取代MapReduce进程或者线程启动和切换的开销。

- API

  Spark使用Scala语言进行开发，并且默认Scala作为其编程语言。因此，编写Spark程序比MapReduce程序要简洁得多。同时，Spark系统也支持Java、Python语言进行开发

- Spark 生态

  Spark SQL、Spark Streaming、GraphX等为Spark的应用提供了丰富的场景和模型，适合应用于不同的计算模式和计算任务

- Spar 部署

  Spark拥有Standalone、Mesos、YARN等多种部署方式，可以部署在多种底层平台上


Spark 是一种**基于内存**的迭代式分布式**计算框架**，适合于完成一些迭代式、关系查询、流式处理等**计算密集型**任务。

---