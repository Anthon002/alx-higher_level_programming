#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        lead = max(a_dictionary, key=lambda i: a_dictionary[i])
        return (lead)
