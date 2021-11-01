import re

TAG_RE = re.compile(r'<[^>]+>')

CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

files_path = "Files/"

def open_file(file_name, path="", mode="r"):
    return open(path + file_name, mode, errors="ignore")

def remove_html_tags(file_name, path=""):
    f = open_file(file_name, path)
    text = f.read()
    f.close()
    return TAG_RE.sub("", text)

def write_text_file(text, file_name):
    f = open_file(file_name + ".txt", mode="w+")
    f.write(text)
    f.close()

write_text_file(remove_html_tags("003.html", files_path), "NoHTML")

file = open_file("NoHTML.txt")

words = []

for f in file:
    word = ""
    for character in f:
        if CHARACTERS.find(character) != -1:
            word += character
        elif word != "":
            words.append(word)
            word = ""

words.sort(key=str.casefold)

for i in words:
    print(i)