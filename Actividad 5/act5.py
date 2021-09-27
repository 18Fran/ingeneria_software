#Librerias
import json
from datetime import datetime, time
import nltk.data
import time
import re
from nltk.tokenize import word_tokenize
from collections import Counter

execution_time = time.time()

#directorios de archivos HTML

simple_path = "Files/simple.html"
medium_path = "Files/medium.html"
hard_path = "Files/hard.html"
fortynine_path = "Files/049.html"

#Descarga punkt
nltk.download('punkt')

#Se leen los archivos html
simple_content = open(simple_path).read()
medium_content = open(medium_path).read()
hard_content = open(hard_path).read()
fortynine_content = open(fortynine_path).read()

#Se guardan los tokens en una lista
simple_tokens = nltk.word_tokenize(simple_content)
medium_tokens = nltk.word_tokenize(medium_content)
hard_tokens = nltk.word_tokenize(hard_content)
fortynine_tokens = nltk.word_tokenize(fortynine_content)

#Se eliminan las tags de HTML
simple_content = re.sub('<[^>]+?>', '', simple_content)
medium_content = re.sub('<[^>]+?>', '', medium_content)
hard_content = re.sub('<[^>]+?>', '', hard_content)
fortynine_content = re.sub('<[^>]+?>', '', fortynine_content)

#Se guardan los tokens en una lista
simple_tokens = nltk.word_tokenize(simple_content)
medium_tokens = nltk.word_tokenize(medium_content)
hard_tokens = nltk.word_tokenize(hard_content)
fortynine_tokens = nltk.word_tokenize(fortynine_content)

#Se pasan las listas con tokens a diccionarios para poder contar los tokens repetidos
a = dict(Counter(simple_tokens))
b = dict(Counter(medium_tokens))
c = dict(Counter(hard_tokens))
d = dict(Counter(fortynine_tokens))


#Se escriben los diccionarios en el archivo a5matricula.txt
with open('a5matricula.txt', 'w') as file:
    file.write(json.dumps(a) + "\n")
    file.write(json.dumps(b) + "\n")
    file.write(json.dumps(c) + "\n")
    file.write(json.dumps(d) + "\n")
    file.write("Time of execution: " + str(execution_time) + " seconds. \n")

#Prints
print("Simple.html")
print(a)
print("Medium.html")
print(b)
print("Hard.html")
print(c)
print("049.html")
print(d)
