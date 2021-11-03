# Librerias
import pandas as pd
import time

execution_time = time.time()

# Paths
posting_path = "files/posting.txt"
tokenized_path = "files/tokenized.txt"

# Se leen los archivos de posting y tokenized utilizando la libreria de pandas. Esta automaticamente lee los archivos
# y los convierte en un dataframe
posting_content = pd.read_csv(posting_path, sep="|", header=None)
tokenized_content = pd.read_csv(tokenized_path, sep="|", header=None)

# Se calculan cuantas veces se repiten los tokens en el archivo de posting
posting_dups = posting_content.pivot_table(columns=[0], aggfunc='size')

# Aqui se guardara el peso de cada token
peso_tokens = []

# For loop que calcula el peso de cada token y lo asigna a peso_tokens
contador = -1
for value in posting_content[0]:
    contador = contador + 1
    if value == "004.html ":
        peso_tokens.append(posting_content[1][contador] * 100 / posting_dups[0])
    elif value == "009.html ":
        peso_tokens.append(posting_content[1][contador] * 100 / posting_dups[1])
    elif value == "412.html ":
        peso_tokens.append(posting_content[1][contador] * 100 / posting_dups[2])
    elif value == "444.html ":
        peso_tokens.append(posting_content[1][contador] * 100 / posting_dups[3])

# Se remplaza la columna de frecuencia, con peso_tokens
posting_content[1] = peso_tokens

# Se imprime el dataframe posting_content en un archivo separado al posting original
with open('posting.txt', 'w') as file:
    dfAsString = posting_content.to_string(header=False, index=False)
    file.write(dfAsString)

# Se imprime el cronometro en un archivo nuevo
with open('a10matricula.txt', 'w') as file:
    file.write("Time of execution: " + str(execution_time) + " seconds. \n")

# Prints
print(peso_tokens)
print(posting_dups)
print(posting_content)
