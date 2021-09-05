import re, glob
import time

files = glob.glob('./files/*.html')

def deleteTags(content):
    exp = re.compile((r'<[^>]+>'))
    return exp.sub('', content)

def pathFile(file):
    result = file.split('\\')
    return result

def main():
    programTime = time.time()

    archivo = open("a2_matricula.txt", "w")

    for file in files:

        path = pathFile(file)[-1]
        print(path)

        with open(file, "r+", encoding='ISO-8859-1') as f:
            tagTime = time.time()
            content = f.read()
            result = deleteTags(content)
            f.close()
        
        with open(file, "w", encoding='ISO-8859-1') as w:
            w.write(result)
            w.close()

        archivo.write(str(path) + " -- " + str(time.time() - tagTime))
        archivo.write("\n")
    
    archivo.write("Tiempo total en eliminar etiquetas HTML: " + str(time.time() - programTime))
    archivo.write("\n")
    archivo.write("Tiempo total de ejecucion " + str(time.time() - programTime))
    archivo.close()

main()
    