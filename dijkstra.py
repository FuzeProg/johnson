#!/usr/bin/env python
# _*_ coding: utf8 _*_
#
# dijkstra.py: dijkstra implementation
#

__author__ = "Anthony MARECHAL"
__copyright__ = "Copyright 2018, FuzeProg"
__credits__ = ["Anthony MARECHAL"]
__version__ = "1.0.1"
__maintainer__ = "Anthony MARECHAL"
__email__ = "anthony.marechal@etu.uphf.fr"
__status__ = "In product"

class Dijkstra:

    def __init__(self, graph):
        self.graph = graph

    def print(self):
        print('How to read the list used for Dijkstra :')
        print('{source: {target: weigth}, source: {target: weigth, ...}, ...}\n')
        print(self.graph)

    def fathers(self, father, src_node, targ_node, edge):
        if targ_node == src_node:
            return [src_node] + edge
        else:
            return self.fathers(father, src_node, father[targ_node], [targ_node] + edge)

    def shortest_path(self, graph, step, targ_node, visits, dist, father, src_node):
        if step == targ_node:
            return dist[targ_node], self.fathers(father, src_node, targ_node, [])
        if len(visits) == 0:
            dist[step] = 0
        for neighbor in graph[step]:
            if neighbor not in visits:
                neighbor_dist = dist.get(neighbor, float('Inf'))
                new_dist = dist[step] = graph[step][neighbor]
                if new_dist < neighbor_dist:
                    dist[neighbor] = new_dist
                    father[neighbor] = step
        visits.append(step)
        unvisits = dict((s, dist.get(s, float('Inf'))) for s in graph if s not in visits)
        nearest_node = min(unvisits, key=unvisits.get)

        return self.shortest_path(graph, nearest_node, targ_node, visits, dist, father, src_node)

    def dij_rec(self, src_node, targ_node):
        return self.shortest_path(self.graph, src_node, targ_node, [], {}, {}, src_node)
