files_path = "Files/"

def open_file(file_name, path=""):
    return open(path + file_name)


file = open_file("002.html", files_path)

print(file.read())

file.close()