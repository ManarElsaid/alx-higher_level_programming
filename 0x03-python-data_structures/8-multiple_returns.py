#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        multiple_returns = len(sentence), sentence[0]
    else:
        multiple_returns = len(sentence), None
    return multiple_returns
