import os
import sys
import time

user_input = input('copia y pega el enlace de directorio')
#copiar y pegar archivo de texto ejemplo C:\Users\atch9\Documents\act12\texto
#asegurate de que en la carpeta que se encuentra el texto no esten archivos que no pueda leer el programa
directory = os.listdir(user_input)

ss = input('Que palabra buscas?')
print("Tus resultados estan listos en a12_matricula.txt")
sys.stdout = open("a12_matricula.txt", "w")
for fname in directory:
    if os.path.isfile(user_input + os.sep + fname):
        
        f = open(user_input + os.sep + fname, 'r')

        

        if ss in f.read():
            print('tu palabra fue encontrado en %s' % fname)
           
        else:
            print('no encontramos la palabra')


execution_time = time.time()

sys.stdout.close()




