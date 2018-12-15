#!/usr/bin/env python3
# _*_ coding: utf8 _*_
#

__author__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__copyright__ = "Copyright 2018, FuzeProg, Liinoa"
__credits__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__version__ = "1.0.1"
__maintainer__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__email__ = ["anthony.marechal@etu.uphf.fr", "ombeline.mozdzierz@etu.uphf.fr"]
__status__ = "In product"

from adjacency_list import List
from bellman import Bellman
from dijkstra import Dijkstra

def main():
    nodes = 4
    edges = 12

    print('----------- Bellman -----------\n')
    g1 = List(nodes, edges, -5, 10)
    g1.init_list()
    g1.dict_to_list()
    g1_l = g1.graphL
    bell = Bellman(nodes, g1_l)
    bell.print()
    bell.bellman_ford(1)

    print('----------- Dijkstra -----------\n')
    src_node = 1
    targ_node = 2
    g2 = List(nodes, edges, 0, 1000)
    g2.init_list()
    dijk = Dijkstra(g2.node_dict)
    dijk.print()
    length, road = dijk.dij_rec(src_node, targ_node)
    print('\nPlus courts chemin entre ', src_node, ' et ', targ_node,' :', road, ' de longueur :', length)


if __name__ == '__main__':
    main()
