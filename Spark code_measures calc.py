from spark_init import spark
from pyspark.sql.functions import substring, min, max, avg

df = spark.read.csv('Milwaukee_weather.tsv', header=True, sep='\t',\
                    schema='dt string, lo float, hi float, mean float, precip float, snow float')

month_df = df.withColumn('month', substring('dt', 0, 2))
result_df = month_df.groupby('month').agg(min('lo').alias('min_temp'), max('hi').alias('max_temp'), avg('mean')\
                                                                        .alias('mean_temp')).orderBy('month')
result_df.show()