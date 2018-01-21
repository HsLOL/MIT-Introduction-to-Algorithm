# -*- coding: utf-8 -*-
"""
Created on 2017/12/21 16:23

@author: Carl
"""

import trace

class PeakProblem(object):

    def __init__(self,array,bounds):

        (startRow, startCol, numRow, numCol) = bounds

        self.array = array
        self.bounds = bounds
        self.startRow = startRow
        self.startCol = startCol
        self.numRow = numRow
        self.numCol = numCol


    def get(self,location):
        (r, c) = location
        if not(0 <= r and r < self.numRow):
            return 0
        if not(0 <= c and c < self.numCol):
            return 0
        return  self.array[self.startRow + r][self.startCol + c]

    def getBetterNeighbor(self, location, trace=None):

        (r, c) = location
        best = location

        if r-1 >=0 and self.get(best) < self.get((r-1, c)):
            best = (r-1, c)
        if r+1 < self.numRow and self.get(best) < self.get((r+1, c)):
            best = (r+1, c)
        if c-1 >=0 and self.get(best) < self.get((r, c-1)):
            best = (r, c-1)
        if c+1 <self.numCol and self.get(best) < self.get((r, c+1)):
            best = (r, c+1)
        if trace is not None : trace.getBetterNeighbor(location, best)

        return best

    def getMaximum(self, locations, trace = None):

        (bestLoc, bestVal) = (None, 0)

        for loc in locations:
            if bestLoc is None or self.get(loc) > bestVal:
                (bestLoc, bestVal) = (loc, self.get(loc))

        if trace is not None: trace.getMaximum(locations, bestLoc)

        return bestLoc

    def isPeak(self, location):

        return (self.getBetterNeighbor(location) == location)


    def getSubproblem(self,bounds):

        (sR, sC, numR, numC) = bounds
        newBounds = (self.startRow + sR, self.startCol + sC, numR, numC)

        return PeakProblem(self.array, newBounds)


    def getSubproblemContaining(self, boundList, location):
        (row, col) = location

        for (sRow, sCol, nRow, nCol) in boundList:
            if sRow <= row  and row < sRow + nRow:
                if sCol <= col and col < sCol + nCol:
                    return  self.getSubproblem((sRow, sCol, nRow, nCol))

        return self

    def getLocationInSelf(self, problem, location):

        (row, col) = location
        newRow = row - self.startRow + problem.startRow
        newCol = col - self.startCol + problem.startCol

        return  (newRow, newCol)


def getDimensions(array):
    rows = len(array)
    cols = 0
    for row in array:
        if len(row) > cols:
            cols = len(row)
    return (rows, cols)


def createProblem(array):
    (rows, cols) = getDimensions(array)
    return PeakProblem(array, (0, 0, rows, cols))
