import time;
from os import listdir
from os.path import isfile, join, abspath
from datetime import datetime
import re

TAG_RE = re.compile(r'<[^>]+>')

files_path = "Files/"

def open_file(file_name, path="", mode="r"):
    return open(path + file_name, mode, errors="ignore")

def remove_html_tags(file_name, path=""):
    f = open_file(file_name, path)
    text = f.read()
    f.close()
    return TAG_RE.sub("", text)

files = [f for f in listdir(files_path) if isfile(join(files_path, f))]

log_file = open_file("a2_al02859552_" + datetime.now().strftime("%d-%m-%Y_%H:%M:%S") + ".txt", mode="w+")

global_timer = 0
execution_time = time.time()

for file in files:
    file_timer = time.time()
    print(remove_html_tags(file, files_path))
    file_timer = time.time() - file_timer
    log_file.write(abspath(file) + " -> " + str(file_timer) + "\n")
    global_timer += file_timer

execution_time = time.time() - execution_time

log_file.write("Time to eliminate all HTML tags: " + str(global_timer) + " seconds.\n")
log_file.write("Time of execution: " + str(execution_time) + " seconds.\n")

log_file.close()