#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_deleted = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_to_deleted:
        del a_dictionary[key]
    return a_dictionary
