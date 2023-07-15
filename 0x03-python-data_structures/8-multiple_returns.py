#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = ()
    sentence_length = len(sentence)
    first_char = sentence[0]
    if sentence_length == 0:
        first_char = "None"
    new_tuple = (sentence_length, first_char)
    return new_tuple
