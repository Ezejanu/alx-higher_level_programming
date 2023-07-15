#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_length = len(sentence)
    if sentence_length == 0:
        first_char = "None"
    else:
        first_char = sentence[0]
    new_tuple = (sentence_length, first_char)
    return new_tuple
