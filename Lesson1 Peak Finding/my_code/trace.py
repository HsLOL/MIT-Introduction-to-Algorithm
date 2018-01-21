# -*- coding: utf-8 -*-
"""
Created on 2017/12/21 16:23

@author: Carl
"""

import peak

class TraceRecord(object):
    def __init__(self):
        self.sequence = []

    def getMaximum(self, arguments, maximum):
        self.sequence.append({
            "type": "findingMaximum",
            "coords": arguments
        })
        self.sequence.append({
            "type":"foundMaximum",
            "coord": maximum
        })

    def getBetterNeighbor(self, neighbor, better):

        self.sequence.append({
            "type": "findingNeighbor",
            "coord": neighbor
        })

        if (neighbor != better):
            self.sequence.append({
                "type": "foundNeighbor",
                "coord": "better"
            })

    def setProblemDimensions(self, subproblem):

        self.sequence.append({
            "type": "subproblem",
            "startRow": subproblem.startRow,
            "numRows": subproblem.numRow,
            "startCol": subproblem.startCol,
            "numCol": subproblem.numCol
        })

    def setBestSeen(self, bestSeen):
        self.sequence.append({
            "type":"bestSeen",
            "coord": bestSeen
        })

    def foundPeak(self, peak):
        self.sequence.append({
            "type": "foundPeak",
            "coord": peak
        })