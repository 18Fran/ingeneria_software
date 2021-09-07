
import time

reloj = time.perf_counter()


# abre el documento para leer las palabras
archivo = "a2_matricula.txt"
archivo = open(archivo,'r')

list = [] # lista de palabras


# abre el documento individualmente y lo ordena


for l in archivo:
    l = l.split()    # separa las palabras

    for w in l:
        list.append(w) # pone las palabras en la lista

list.sort() # ordena alphabeticamente

dicc = {}   

# cuenta las palabras en la lista y las agrega a un diccionario
for w in list:
    dicc[w] = list.count(w)  


print('\n{:^8}{:^8}'.format('Word','Count')) # organiza en columnas
for w in dicc:
    print('{:^8}{:^8d}'.format(w,dicc[w]))     # imprime las columnas
    
print("tiempo total de ejecucion")
print (reloj)
