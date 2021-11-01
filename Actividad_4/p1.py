import re

TAG_RE = re.compile(r'<[^>]+>')

CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

FILES_PATH = "Files/"

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

def write_text_list_file(string_list: list[str], file_name):
    f = open_file(file_name + ".txt", mode="w+")
    f.writelines(string_list)
    f.close()

def word_list_from_file(file):
    words = []
    for f in file:
        word = ""
        for character in f:
            if CHARACTERS.find(character) != -1:
                word += character
            elif word != "":
                words.append(word)
                word = ""
    return words

def word_list_from_string(string):
    words = []
    word = ""
    for character in string:
        if CHARACTERS.find(character) != -1:
            word += character
        elif word != "":
            words.append(word)
            word = ""
    return words

def sort_and_uncase_strings(strings: list[str]):
    lowercase = [string.lower() for string in strings]
    return sorted(lowercase, key=str.casefold)

text_list = sort_and_uncase_strings(word_list_from_string(remove_html_tags("002.html", FILES_PATH)))

for text in text_list:
    print(text)