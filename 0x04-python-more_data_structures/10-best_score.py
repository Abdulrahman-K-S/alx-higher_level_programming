#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    score = 0
    for k, v in a_dictionary.items():
        if score < v:
            score = v
            score_key = k

    return score_key
