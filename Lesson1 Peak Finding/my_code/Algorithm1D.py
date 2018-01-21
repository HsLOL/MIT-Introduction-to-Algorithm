# -*- coding: utf-8 -*-
"""
Created on 2017/12/21 16:22

@author: Carl
"""

import utils
import json
import peak1
import trace
import sys

def algorithm1(problem, trace= None):
    if problem.numRow <=0 or problem.numCol <=0:
        return None

    if problem.numCol != 1:
        return None

    mid = problem.numRow //2

    (subStartR1, subNumR1) = (0, mid)
    (subStartR2, subNumR2) = (mid+1, problem.numRow - (mid + 1))

    subproblems = []
    subproblems.append((subStartR1, 0, subNumR1, 1))
    subproblems.append((subStartR2, 0, subNumR2, 1))

    center = (mid, 0)
    neighbor = problem.getBetterNeighbor(center, trace)

    if neighbor == center:
        if trace is not None: trace.foundPeak(center)
        return center

    sub = problem.getSubproblemContaining(subproblems, neighbor)
    if trace is not None : trace.setProblemDimensions(sub)
    result = algorithm1(sub, trace)
    return  problem.getLocationInSelf(sub, result)

def loadProblem(file, variable = "problemList"):
    namespace = dict()
    with open(file) as handle:
        exec (handle.read(), namespace)

    matrix = convertFrom1D(namespace[variable])
    return peak1.createproblem(matrix)

def convertFrom1D(list):

    return [[x] for x in list]

def main():
    if len(sys.argv)> 1:
        problem = loadProblem(sys.argv[1])
    else:
        problem = loadProblem(utils.getOpenFilename("problem1D.py"))


    algorithmList = [("Algorithm 1", algorithm1)]

    steps = []

    for (name, function) in algorithmList:
        tracer = trace.TraceRecord()
        peak = function(problem, trace = tracer)
        steps.append(tracer.sequence)

        status = "is not a peak(INCORRECT!)"
        if problem.isPeak(peak):
            status = "is a peak"

        print(name + ":" + str(peak) + "==>" + status)

    with open("trace.json","w") as traceFile:
        traceFile.write("parsre(")

        json.dump({
            "input": problem.array,
            "steps": steps,
            }, traceFile)

        traceFile.write(")")

if __name__ == "__main__":
    main()