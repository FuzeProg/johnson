#!/usr/bin/env python3
# _*_ coding: utf8 _*_
#
# johnson.py: johnson implementation
#

__author__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__copyright__ = "Copyright 2018, FuzeProg, Liinoa"
__credits__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__version__ = "1.0.1"
__maintainer__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__email__ = ["anthony.marechal@etu.uphf.fr", "ombeline.mozdzierz@etu.uphf.fr"]
__status__ = "In product"

from collections import defaultdict
from heapq import *

class Dijkstra:

    def __init__(self, edges):
        self.edges = edges

    def print(self):
        print('How to read the list used for Dijkstra :')
        print('(Total weight, (targ_node, (node, (..., (src_node, ())))))\n')

    def algorithm(self, f, t):
        g = defaultdict(list)
        for src, targ, weight in self.edges:
            g[src].append((weight, targ))

        q, visited, mins = [(0, f, ())], set(), {f: 0}
        while q:
            (weight, node, path) = heappop(q)
            if node not in visited:
                visited.add(node)
                path = (node, path)
                if node == t:
                    return (weight, path)

                for cost, node, in g.get(node, ()):
                    if node in visited:
                        continue
                    prev = mins.get(node, None)
                    next = weight + cost
                    if prev is None or next < prev:
                        mins[node] = next
                        heappush(q, (next, node, path))

        return float("Inf")