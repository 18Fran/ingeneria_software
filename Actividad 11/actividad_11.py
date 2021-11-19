import pandas as pd
import time

execution_time = time.time()

# Paths
posting_path = "files/posting.txt"

# Se leen los archivos de posting y tokenized utilizando la libreria de pandas. Esta automaticamente lee los archivos
# y los convierte en un dataframe
posting_content = pd.read_csv(posting_path, sep="|", header=None)

posting_content[1] = posting_content[0]
# Aqui se guardara el peso de cada token
id_posting = []

# For loop que calcula el peso de cada token y lo asigna a peso_tokens
contador = 0
for value in posting_content[0]:
    contador += 1
    id_posting.append(contador)

# Se remplaza la columna de frecuencia, con peso_tokens
posting_content[0] = id_posting

# Se imprime el dataframe posting_content en un archivo separado al posting original
with open('a11matricula.txt', 'w') as file:
    dfAsString = posting_content.to_string(header=False, index=False)
    file.write(dfAsString)
    file.write("\nTime of execution: " + str(execution_time) + " seconds. \n")


