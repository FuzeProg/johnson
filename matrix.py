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

import random


class Graph:

    def __init__(self):
        self._node_dict = {}

    @property
    def node_dict(self):
        return self._node_dict

    def add_node(self, node_item):

        self._node_dict[node_item] = []

    def add_edge(self, src_node, targ_node):
        self._node_dict[src_node].append(targ_node)

    def init_list(self, nodes, edges):
        for i in range(1, nodes + 1):
            self.add_node(i)

        while edges > 0:
            src_node = random.randint(1, nodes)
            targ_node = random.randint(1, nodes)
            self.add_edge(src_node, targ_node)
            edges = edges - 1