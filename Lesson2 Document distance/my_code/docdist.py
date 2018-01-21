# -*- coding: utf-8 -*-
"""
Created on 2017/12/28 9:32

@author: Carl
"""

import  sys

import math

import string

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except IOError :
        print("Error opening or reading input file: ",filename)
        sys.exit()

translation_table = str.maketrans(string.punctuation + string.ascii_uppercase, " "*len(string.punctuation) + \
                                  string.ascii_lowercase)


def get_words_from_text(text):
    text = text.translate(translation_table)
    words_list = text.split(" ")
    return  words_list

def count_frequency(words_list):
    D = {}
    for word in words_list:
        if word in D:
            D[word] += 1
        else:
            D[word] = 1
    return D

def word_frequency_for_file(filename):
    text = read_file(filename)
    words_list = get_words_from_text(text)
    word_frequency = count_frequency(words_list)

    return word_frequency

def inner_product(D1, D2):
    sum = 0.0
    for word in D1:
        if word in D2:
            sum += D1[word] * D2[word]
    return sum

def vector_angle(D1, D2):
    numerator = inner_product(D1, D2)
    denominator = math.sqrt(inner_product(D1, D1) * inner_product(D2, D2))

    return math.acos(numerator/denominator)

def main():
    if len(sys.argv) != 3:
        print("Usage docdict.py filename1 filename2")
    else:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
        sorted_words_list1 = word_frequency_for_file(filename1)
        sorted_words_list2 = word_frequency_for_file(filename2)
        distance = vector_angle(sorted_words_list1, sorted_words_list2)

        print("The distance between the documents is : %0.6f (radians)"%distance)

if __name__ == '__main__':
    import cProfile
    cProfile.run("main()")
