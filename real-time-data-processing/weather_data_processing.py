from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, FloatType

# Crie a sessão Spark
spark = SparkSession.builder \
    .appName("WeatherDataProcessing") \
    .getOrCreate()

# Defina o esquema para os dados do Kafka
schema = StructType() \
    .add("name", StringType()) \
    .add("main", StructType()
         .add("temp", FloatType())
         .add("humidity", FloatType()))

# Leia os dados do Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "weather_data") \
    .load()

# Converta os dados do Kafka para JSON e selecione os campos relevantes
weather_data = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.name", "data.main.temp", "data.main.humidity")

# Escreva os dados no PostgreSQL
query = weather_data.writeStream \
    .outputMode("append") \
    .foreachBatch(lambda batch_df, batch_id: 
                  batch_df.write \
                      .format("jdbc") \
                      .option("url", "jdbc:postgresql://postgres:5432/airflow") \
                      .option("dbtable", "weather_data") \
                      .option("user", "airflow") \
                      .option("password", "airflow") \
                      .option("driver", "org.postgresql.Driver") \
                      .mode("append") \
                      .save()) \
    .start()

query.awaitTermination()
