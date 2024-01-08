#!/usr/bin/python3
def no_c(my_string):
    esra = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(esra))
