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

from adjacency_list import List
from bellman import Bellman

def main():
    nodes = 4
    edges = 12
    graph = List()
    bell = Bellman(nodes, graph)
    graph.init_list(nodes, edges)
    print(graph.node_dict)
    graph.display()

if __name__ == '__main__':
    main()
