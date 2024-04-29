## For PySpark processing, we have to submit the spark job command manually as below:-
```spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 pyspark_consumer.py```
Where, 
    scala_version = '2.12'
    spark_version = '3.5.1'

Some important resources:-
 - https://rmoff.net/2018/08/02/kafka-listeners-explained/
 - https://www.confluent.io/blog/kafka-client-cannot-connect-to-broker-on-aws-on-docker-etc/
 - https://medium.com/@aman.parmar17/handling-real-time-kafka-data-streams-using-pyspark-8b6616a3a084 (JOSS/MUST)
 - https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html
 - https://stackoverflow.com/questions/77622514/cannot-submit-spark-application-to-docker-compose (MUST)
 - https://stackoverflow.com/questions/46430106/worker-failed-to-connect-to-master-in-spark-apache
 - https://community.microstrategy.com/s/question/0D54W0000A9Yy8YSQS/we-got-a-new-error-message-after-making-the-change-on-socketrequestmaxbytes-value-in-serverproperties-to-2147483647-the-cpu-utilization-on-the-kafkaexe-process-keeps-increasing-over-time-12-hours-until-all-the-cpu-resources-are-at-100?language=en_US (Same issue...)




2147483647
104857600