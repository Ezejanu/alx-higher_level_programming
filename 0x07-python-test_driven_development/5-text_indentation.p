#!/usr/bin/python3

def text_indentation(text):

    if isinstance(text, str):
        raise TypeError("text must be a string")

    new_str = ""
    for i in range(len(text)):
        new_str += i
        if text[i] in ". ? :":
            print("\n")
        if text[i] + 1 = " ":
            continue
    print(new_str)


