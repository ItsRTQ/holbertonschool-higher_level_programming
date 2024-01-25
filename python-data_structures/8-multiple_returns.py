#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght > 0:
        firstChar = sentence[0]
    else:
        firstChar = None
    data = (lenght, firstChar)
    return data
