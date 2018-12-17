#!/usr/bin/env python3
# _*_ coding: utf8 _*_
#
# bellman.py: bellman implementation
#

__author__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__copyright__ = "Copyright 2018, FuzeProg, Liinoa"
__credits__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__version__ = "1.0.1"
__maintainer__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__email__ = ["anthony.marechal@etu.uphf.fr", "ombeline.mozdzierz@etu.uphf.fr"]
__status__ = "In product"

class Bellman:

    def __init__(self, nodes, g):
        self.nodes = nodes
        self.graph = g

    def print(self):
        print('How to read the list used for Bellman :')
        print('[[source, target, weigth], [source, target, weigth], ...]\n')
        print(self.graph)

    def bellman_ford(self, src_node):

        dist = [float("Inf")] * self.nodes
        dist[src_node] = 0

        for i in range(self.nodes):
            for u, v, w in self.graph:
                if dist[u-1] != float('Inf') and dist[u-1] + w < dist[v-1]:
                    dist[v-1] = dist[u-1] + w

        for u, v, w in self.graph:
            if dist[u-1] != float("Inf") and dist[u-1] + w < dist[v-1]:
                print('\nGraph has negative cycle\n')
                return True
            else:
                print('\nGraph is ok\n')
                return False

