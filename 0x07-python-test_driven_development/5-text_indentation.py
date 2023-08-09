#!/usr/bin/python3
""" a function that prints a text with indentation """


def text_indentation(text):
    """ Prints a text with 2 new lines after each of the characters: . ? : """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_str = ""
    in_sentence = False

    for i in range(len(text)):
        new_str += text[i]
        if text[i] in ".?:" and i < len(text) - 1:
            new_str += "\n"

    lines = [line.strip() for line in new_str.split('\n')]
    new_text = "\n".join(lines)
    print(new_str)
