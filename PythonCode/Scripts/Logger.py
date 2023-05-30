#!/usr/bin/python3

"""
Logger.py is a script used to log the time it takes the tool VVODKA to generate plots
"""


def logger(text, file):
    file_obj = open(file, "a")
    file_obj.write(text)
    file_obj.close()
