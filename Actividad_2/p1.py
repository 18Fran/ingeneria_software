import re

TAG_RE = re.compile(r'<[^>]+>')

files_path = "Files/"

def open_file(file_name, path=""):
    return open(path + file_name)

def remove_html_tags(file_name, path=""):
    f = open_file(file_name, path)
    print(TAG_RE.sub("", f.read()))

remove_html_tags("002.html", files_path)