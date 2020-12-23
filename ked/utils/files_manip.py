def get_file_content(file_name):
    f = open(file_name)
    content = f.read()
    f.close()
    return content
