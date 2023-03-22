from nltk import word_tokenize
import nltk
nltk.download('punkt')
#!pip install zemberek-python
#!pip install zeyrek
import zeyrek #Türkçe kelimelerin lemmatization'ı için kütüphane
analyzer = zeyrek.MorphAnalyzer()
#Lemmatization için fonksiyon
hashTable = {}
def lemmetization(text):
    tokens = word_tokenize(text)
    words = []
    for word in tokens:
        if(word in hashTable):
            words.append(hashTable[word])
        else:
            new_word = analyzer.lemmatize(word); flag = False 
            for i in range(0,len(new_word[0][1])):
                if new_word[0][0] == new_word[0][1][i]:
                    words.append(new_word[0][1][i])
                    hashTable[word] = new_word[0][1][i]
                    flag = True
                    break
            if flag == True:
                pass
            else:
                hashTable[word] = new_word[0][1][0]
                words.append(new_word[0][1][0])
    return ' '.join(words)
#Lemmatization bittikten sonra
def to_lower(text):
    return text.lower()
