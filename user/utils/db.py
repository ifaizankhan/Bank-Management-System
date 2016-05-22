
def save(file_name, content):
    with open(file_name, 'w+') as f:
        f.write("\n".join(content))


def get(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = f.read()
        lines = lines.split("\n")

    return lines
