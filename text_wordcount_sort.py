def read_file_as_words(filepath):
    speech_file=open(filepath,encoding="utf-8")
    list_of_words=speech_file.read().split()
    speech_file.close()
    return list_of_words 

def clean_up(list_of_words):
    common_word_file=open("common_words.txt",encoding="utf-8")
    common_words=common_word_file.read().lower().split()
    common_word_file.close()

    list_of_cleaned_words =[]
    for word in list_of_words:       
        word=word.lower().strip() 
        alpha = ""
        for ch in word:
            if ch.isalpha():
                alpha+=ch
        if alpha!='' and alpha not in common_words:
            list_of_cleaned_words.append(alpha)
    return list_of_cleaned_words
    
def count_words(list_of_cleaned_words):
    word_count = dict()
    for everyword in list_of_cleaned_words:
        if everyword in word_count:
            word_count[everyword]+=1
        else:
            word_count[everyword]=1  
    return word_count

def sort_by_count_word(word_count):
    sorted_count_word=sorted((-count,word) for (word,count) in word_count.items()) 
    list_of_sorted_wordcount=[]
    for count, word in sorted_count_word:
        list_of_sorted_wordcount.append(f'{word} - {-count}')    
    return list_of_sorted_wordcount

def write_out(filename, list_of_sorted_wordcount):
    new_file = open(filename,'w')
    for item in list_of_sorted_wordcount:
        new_file.writelines(item+'\n')
    new_file.close()
    pass

list_of_words=read_file_as_words("speech.txt") #step 1 - read speech.txt
list_of_cleaned_words = clean_up(list_of_words) #step 2 - clean up words in speech.txt by comparing with common_words.txt
word_count = count_words(list_of_cleaned_words)  #step 3 - count the words and their occurrences
list_of_sorted_wordcount=sort_by_count_word(word_count) #step 4 - sort the word list in descending order
write_out("top_twenty_words.txt",list_of_sorted_wordcount[:20]) # step 5 - write the top 20 occurrences to a new file => this generates a new file in the same path as the python script