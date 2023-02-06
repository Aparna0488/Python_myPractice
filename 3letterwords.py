from spark_init import sc, pyspark

data = sc.textFile('3_letter_words.txt')
parsed_data = data.map(lambda line: line.split("|")[0].lower()).filter(lambda line: line.startswith('y'))
# parsed_data.saveAsTextFile("/home/aparna/bigdata/pythonProject/coalesce")
parsed_data.coalesce(1).saveAsTextFile("result.txt")
