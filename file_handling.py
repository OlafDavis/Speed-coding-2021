def read_json(filename):

    import json
    file = open(filename, )
    data = json.load(file)
    file.close()
    return data


def read_text(filename):
    file = open(filename, )
    text = file.read()
    file.close()
    return text


def read_lines(filename):
    file = open(filename, )
    lines = file.readlines()
    file.close()
    return lines
