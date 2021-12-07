import pandas as pd
import time

time_start = time.time()

token_to_find = input("Pon la palabra a buscar: ")

tokenized = pd.read_csv('tokenized.csv', sep=';')
posting = pd.read_csv('posting.csv', sep=';')

def main():
    """
    Por cada row en tokenized se busca el token_to_find
    y de ahi se hace un sort con nlargest para encontrar
    los 10 mas grandes
    """
    for token, row in tokenized.iterrows():
        if row['Token'] == token_to_find:
            start = row['Posting']
            end = row['Posting'] + row['Docs']
            top10_found = posting.loc[start:end].nlargest(10, 'Frec')
            print(posting.loc[start:end].nlargest(10, 'Frec'))
            break

    time_end = time.time()

    print("La ejecucion del programa fue: ", time_end - time_start)

    with open("a13_matricula.txt", 'a') as f:
        dfAsString = top10_found['Doc'].to_string(header=False, index=False)
        f.write("Busqueda realizada: ")
        f.write(token_to_find)
        f.write("\n")
        f.write(dfAsString)
        f.write("\n")
        f.write("La ejecucion del programa fue: ")
        f.write(str(time_end - time_start))
        f.write("\n")

if __name__ == "__main__":
    main()
