import os

file_name = "score_Save"

def create_file():
    if file_exit():
        f = open(file_name, "r+")
    else:
        f = open(file_name, "w+")
    return f


def file_exit():
    result = os.path.exists(file_name)
    return result


def read_score():
    f = create_file()
    score = f.read()
    f.close()
    return score


def write_score(score):
    f = create_file()
    f.write(score)
    f.close()
