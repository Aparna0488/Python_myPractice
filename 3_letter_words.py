from spark_init import sc, spark
rdd=sc.textFile('3_letter_words.txt')
data = rdd.collect()
print(data)

word_list=[]
for row in data:
        three_letter_words =row.split('|')[0].lower().replace(' ','')
        if three_letter_words.startswith('y'):
                word_list.append(three_letter_words)

with open(r'filtered.txt','w') as fp:
    for item in word_list:
        fp.write("%s\n" % item)
    print('Done')