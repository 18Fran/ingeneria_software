import time

timer = time.perf_counter

homeworkpast = open("words.txt","r")
order_data = open("ordenAlfabetico.txt","w+")
result = open("a4_matricula.txt","w+")

listwords = []

for l in homeworkpast:
    l = l.split()

    for w in l:
        listwords.append(w)

listwords.sort()

for r in listwords:
    order_data.write(r + "\n")

result.write("Tiempo total de la ejecución")
result(timer)


