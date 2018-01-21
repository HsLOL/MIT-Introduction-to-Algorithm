# -*- coding: utf-8 -*-
"""
Created on 2017/12/21 20:14

@author: Carl
"""

def algorithm1(problem, trace = None):
    if problem.numRow <=0 or problem.numCol<=0:
        return None

    mid = problem.numCol//2

    (subStartR, subnumRow) = (0, problem.numRow)
    (subStartC1, subnumC1) = (0, mid)
    (subStartC2, subnumC2) = (mid+1, problem.numCol-mid-1)

    subproblems = []
    subproblems.append((subStartR,subStartC1 , subnumRow, subnumC1))
    subproblems.append((subStartR,subStartC2 , subnumRow, subnumC2))

    divider = crossProduct(range(problem.numRow), [mid])

    bestLoc = problem.getMaximum(divider, trace)

    neighbor = problem.getBetterNeighbor(bestLoc, trace)

    if neighbor == bestLoc:
        if trace is not None : trace.foundPeak(neighbor)
        return bestLoc

    sub = problem.getSubproblemContaining(subproblems, neighbor)
    if trace is not None: trace.setProblemDimensions(sub)
    result = algorithm1(sub, trace)
    return problem.getLocationInSelf(sub, result)

def algorithm2(problem, location = (0, 0), trace = None):
    if problem.numRow <=0 or problem.numCol<=0:
        return None

    nextLocation = problem.getBetterNeighbor(location, trace)

    if nextLocation == location:
        if trace is not None: trace.foundPeak(location)
        return location
    else:
        return algorithm2(problem, nextLocation, trace)

def algorithm3(problem, bestSeen = None, Row_split = True, trace = None):
    if problem.numRow <=0 or problem.numCol<=0:
        return None

    subproblems = []
    divider = []

    if Row_split:
        mid = problem.numRow//2

        (subRow1, subnumR1) = (0, mid)
        (subRow2, subnumR2) = (mid+1, problem.numRow-mid-1)
        (subCol, subnumC) = (0, problem.numCol)

        subproblems.append((subRow1, subCol, subnumR1,  subnumC))
        subproblems.append((subRow2, subCol, subnumR2,  subnumC))

        divider = crossProduct([mid], range(problem.numCol))
    else:
        mid = problem.numCol//2

        (subRow, subnumR) = (0, problem.numRow)
        (subCol1, subnumC1) = (0, mid)
        (subCol2, subnumC2) = (mid+1, problem.numCol-mid-1)

        subproblems.append((subRow, subCol1,subnumR,  subnumC1))
        subproblems.append((subRow, subCol2,subnumR,  subnumC2))

        divider = crossProduct(range(problem.numRow), [mid])

    bestLocation = problem.getMaximum(divider, trace)
    neighbor = problem.getBetterNeighbor(bestLocation, trace)

    if bestSeen is None or problem.get(neighbor) > problem.get(bestSeen) :
        if trace is not None: trace.setBestSeen(bestSeen)
        bestSeen = neighbor

    if bestLocation == neighbor and problem.get(bestLocation) >= problem.get(bestSeen) :
        if trace is not None: trace.foundPeak(bestLocation)
        return bestLocation

    sub = problem.getSubproblemContaining(subproblems, bestSeen)
    newBest = sub.getLocationInSelf(problem, bestSeen)
    if trace is not None: trace.setProblemDimensions(sub)
    result = algorithm3(sub, newBest, not Row_split, trace)
    return problem.getLocationInSelf(sub, result)

def algorithm4(problem, bestSeen = None, trace = None):
    if problem.numRow <= 0 and problem.numCol <= 0:
        return None

    midR = problem.numRow//2
    midC = problem.numCol//2

    subproblems = []

    (subR1, subnumR1) = (0, midR)
    (subR2, subnumR2) = (midR + 1, problem.numRow - midR - 1)
    (subC1, subnumC1) = (0, midC)
    (subC2, subnumC2) = (midC + 1, problem.numCol - midC - 1)
    subproblems.append((subR1, subC1, subnumR1, subnumC1))
    subproblems.append((subR1, subC2, subnumR1, subnumC2))
    subproblems.append((subR2, subC1, subnumR2, subnumC1))
    subproblems.append((subR2, subC2, subnumR2, subnumC2))

    divider = []
    divider.append(crossProduct([midR], range(problem.numCol)))
    divider.append(crossProduct(range(problem.numRow), [midC]))

    bestLoc = problem.getMaximum(divider, trace)
    neighbor = problem.getBetterNeighbor(bestLoc, trace)

    if bestSeen == None or problem.get(neighbor) > problem.get(bestSeen):
        if trace is not None : trace.setBestSeen(bestSeen)
        bestSeen = neighbor

    if neighbor == bestLoc and problem.get(bestLoc) >= problem.get(bestSeen):
        if trace is not None: trace.foundPeak(bestLoc)
        return bestLoc

    sub = problem.getSubproblemContaining(subproblems, bestSeen)
    newBest = sub.getLocationInSelf(problem, bestSeen)
    if trace is not None : trace.setProblemDimensions(sub)
    result = algorithm4(sub, newBest, trace)
    return problem.getLocationInSelf(sub, result)

def crossProduct(list1, list2):
    answer = []
    for a in list1:
        for b in list2:
            answer.append((a, b))

    return  answer