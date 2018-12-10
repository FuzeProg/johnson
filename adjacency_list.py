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


class List:

    def __init__(self):
        self._node_dict = {}

    @property
    def node_dict(self):
        return self._node_dict

    def add_node(self, node_item):

        self._node_dict[node_item] = []

    def add_edge(self, src_node, targ_node):
        self._node_dict[src_node].append(self.weigth_edge(targ_node))

    def edge_exist(self, src_node, targ_node):
        if targ_node in self._node_dict[src_node]:
            return True
        else:
            return False

    def weigth_edge(self, node_item):
        node = {}

        weigth = random.randint(-10, 10)

        while weigth == 0:
            weigth = random.randint(-10, 10)

        node[node_item] = weigth

        return node

    def init_list(self, nodes, edges):
        for i in range(1, nodes + 1):
            self.add_node(i)

        while edges > 0:
            src_node = random.randint(1, nodes)
            targ_node = random.randint(1, nodes)

            while self.edge_exist(src_node, targ_node):
                src_node = random.randint(1, nodes)
                targ_node = random.randint(1, nodes)

            self.add_edge(src_node, targ_node)

            edges = edges - 1

    def parcours(self):
        for src_node in self._node_dict.keys():
            for targ_node in self._node_dict.values():
                print("Node ", src_node, " linked to node ", targ_node)