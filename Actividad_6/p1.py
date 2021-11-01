import re
from datetime import datetime
import time;
from os import listdir
from os.path import isfile, join, abspath

TAG_RE = re.compile(r'<[^>]+>')

CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

FILES_PATH = "Files/"

TOKENIZED_FILES_PATH = "Tokenized/"

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

def token_exists(token, dictionary: dict):
    for key in dictionary.keys():
        if key == token:
            return True
    return False

def tokenize_string_list(strings: list):
    tokens = {}
    for string in strings:
        if token_exists(string, tokens):
            tokens[string] += 1
        else:
            tokens[string] = 1
    return tokens

def compare_and_append_dictionaries(token_list: list[dict]):
    full_tokens = {}
    for tokens in token_list:
        for token in tokens.keys():
            if token_exists(token, full_tokens):
                full_tokens[token][0] += tokens[token]
                full_tokens[token][1] += 1
            else:
                full_tokens[token] = []
                full_tokens[token].append(tokens[token])
                full_tokens[token].append(1)
    return full_tokens

files = ["simple.html", "medium.html", "hard.html", "049.html"]

log_file = open_file("a6_al02859552_" + datetime.now().strftime("%d-%m-%Y_%H:%M:%S") + ".txt", mode="w+")

global_timer = 0
execution_time = time.time()

tokenized_list_of_dicts = []

for file in files:
    file_timer = time.time()
    tokens = tokenize_string_list(sort_and_uncase_strings(word_list_from_string(remove_html_tags(file, FILES_PATH))))
    tokenized = open_file(file, TOKENIZED_FILES_PATH, "w+")
    for token in tokens.keys():
        tokenized.write(token + " " + str(tokens[token]) + "\n")
    tokenized.close()
    tokenized_list_of_dicts.append(tokens)
    file_timer = time.time() - file_timer
    log_file.write(abspath(file) + " -> " + str(file_timer) + "\n")
    global_timer += file_timer

processed_tokens = compare_and_append_dictionaries(tokenized_list_of_dicts)

tokenized_file = open_file("tokenized.txt", mode="w+")

for token in processed_tokens.keys():
    tokenized_file.write(token + " | " + str(processed_tokens[token][0]) + " | " + str(processed_tokens[token][1]) + "\n")

tokenized_file.close()

execution_time = time.time() - execution_time

log_file.write("Time to eliminate all HTML tags and order words: " + str(global_timer) + " seconds.\n")
log_file.write("Time of execution: " + str(execution_time) + " seconds.\n")

log_file.close()