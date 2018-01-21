# -*- coding: utf-8 -*-
"""
Created on 2017/12/21 16:09

@author: Carl
"""
import os

def getOpenFilename(default = None):
    promot = "Enter your file name to load from"
    if default is not None:
        promot += (" (default: %s)"%default)
    promot += ":"

    filename = input(promot)
    if filename == "" and not (default is None):
        filename = default
    return filename

def getSaveFilename(default = None):
    promot = "Enter a file name to save to"
    if default is not None:
        promot += (" (default: %s)"%default)
    promot += ":"

    filename = input(promot)
    if filename == "" and not (default is None):
        filename =default

    if os.path.exists(filename):
        print("The file %s is already exits."% filename)
        promot = ("Overwrite(o), enter another name(e), or cancle(c)?")

        check = input(promot)
        while (check !='o' and check != 'e' and check != 'c'):
            check = input(promot)

        if check == "o":
            return filename
        elif check == "e":
            return getSaveFilename(default)
        elif check == "c":
            return None

    return filename
