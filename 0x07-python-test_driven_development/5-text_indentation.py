#!/usr/bin/python3

def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_str = ""
    for i in range(len(text)):
        new_str += text[i]
        if text[i] in ".?:":
            new_str += "\n"
        elif text[i] == " " and (i == len(text) - 1 or text[i + 1] != " "):
            new_str += " "
    print(new_str)


