#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    leng = len(sentence)
    first_letter = sentence[0]
    return (leng, first_letter)
