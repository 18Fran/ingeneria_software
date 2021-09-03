import time;
from os import listdir
from os.path import isfile, join, abspath
from datetime import datetime

files_path = "Files/"

def open_file(file_name, path="", mode="r"):
    return open(path + file_name, mode, errors="ignore")

files = [f for f in listdir(files_path) if isfile(join(files_path, f))]

log_file = open_file("al02859552_" + datetime.now().strftime("%d-%m-%Y_%H:%M:%S"), mode="w+")

global_timer = 0
execution_time = time.time()

for file in files:
    file_timer = time.time()
    f = open_file(file, files_path)
    print(f.read())
    file_timer = time.time() - file_timer
    log_file.write(abspath(file) + " -> " + str(file_timer) + "\n")
    global_timer += file_timer
    f.close()

execution_time = time.time() - execution_time

log_file.write("Time to open all files: " + str(global_timer) + " seconds.\n")
log_file.write("Time of execution: " + str(execution_time) + " seconds.\n")

log_file.close()