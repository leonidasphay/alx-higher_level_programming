#!/usr/bin/python3
'''Module for task 1'''


def write_file(filename="", text=""):
    '''Override the content of a file'''
    with open(filename, 'w') as f:
        return f.write(text)
