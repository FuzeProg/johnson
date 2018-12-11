#!/usr/bin/env python3
# _*_ coding: utf8 _*_
#
# Foobar.py: Description of what foobar does.
#

__author__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__copyright__ = "Copyright 2018, FuzeProg, Liinoa"
__credits__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__version__ = "1.0.1"
__maintainer__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__email__ = ["anthony.marechal@etu.uphf.fr", "ombeline.mozdzierz@etu.uphf.fr"]
__status__ = "In product"

class Bellman:

    def __init__(self, nodes, g, graph):
        self.nodes = nodes
        self.graph = g

    def printArr(self, dist):
        print("vertex    Distance from source")
        for i in range(self.nodes):
            print("%d \t\t %d" % (i+1, dist[i]+1))



    def bellman_ford(self, src_node):

    def is_state_equal_to(self, graph, node, state=''):
        return graph.node[node]['state'] == state

        for i in range(self.nodes):
            for u, v, w in self.graph:
                # print("\n",u, v, w)
                # print(u-1, v-1, w-1, "\n")
                if dist[u-1] != float("Inf") and dist[u-1] + w < dist[v-1]:
                    dist[v-1] = dist[u-1] + w

        for u, v, w in self.graph:
            if dist[u-1] != float("Inf") and dist[u-1] + w < dist[v-1]:
                print("graph contains negative weight cycle")
                return

        self.printArr(dist)


