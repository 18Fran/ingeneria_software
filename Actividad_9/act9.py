
arreglo = []

#abre el archivo
with open("stoplist.txt", "r") as r:
    
    #lee cada linea de el documento
    lines = r.readlines()

    #empieza analizar linea por linea
    for line in range(len(lines)):
        #borra el caracter de mas
        lines[line] = lines[line].replace("\n", "")
        
        #si la longitud es igual a uno, no ponerlo en el nuevo arreglo
        if(len(lines[line]) == 1):
            continue
        else:
        #agregarlo al arreglo
            arreglo.append(lines[line].replace("\n", ""))

#crea un nuevo archivo pero sin los caracteres individual


#imprimir nuevo documento
with open("test.txt", "r") as f:
    words = [word.strip() for word in f.readlines()]
print(words)
