import string

PATH = {}
UPPERCASE_L = string.ascii_uppercase
LOWERCASE_L = string.ascii_lowercase
DIGITS = string.digits
SPACE = " "


def text_Checker(text):  # let PI = 3.14;
    tmp = {}
    tmp.clear()
    for index in range(len(text)):
        if text[index] == SPACE:
            tmp[index] = "SPACE"
        elif text[index] in DIGITS:
            tmp[index] = "INT"
        else:
            tmp[index] = "OTHERS"
    return tmp


def path_Generator(text, tmp):
    if text[0:3] == "let":
        variable_name = ""
        variable_value = ""
        equal_index = 0
        for index in range(3, len(text[4:])):
            if text[index] in UPPERCASE_L or text[index] in LOWERCASE_L or text[index] == "_" and text[index] != "=":
                variable_name += text[index]
                if text[index] == "=":
                    equal_index = index
                    break
        for index in range(equal_index+1, len(text[equal_index+1:])):
            if tmp[index] == "INT":
                variable_value += text[index]
            PATH[variable_name] = variable_value
        print(PATH)


if __name__ == "__main__":
    while True:
        txt = input()
        if txt.lower == "e":
            break
        temp = text_Checker(txt)
        path_Generator(txt, temp)
