# -*- coding: utf-8 -*-
"""
Created on 2017/12/19 18:54

@author: Carl
"""
import sys
import peak
import trace
import algorithms
import json
import utils

def loadProblem(file = "problem.py", variable = "problemMatrix"):
    """
    Loads a matrix from a python file, and constructs a PeakProblem from it.
    """

    namespace = dict()
    with open(file) as handle:
        exec(handle.read(), namespace)
    return peak.createProblem(namespace[variable])

def main():
    if len(sys.argv) > 1:
        problem = loadProblem(sys.argv[1])
    else:
        problem = loadProblem(utils.getOpenFilename("problem.py"))

    peak = algorithms.algorithm3(problem, trace=None)

    print(str(peak))

if __name__ == "__main__":
    main()
