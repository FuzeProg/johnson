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
        self.graphL = []

    @property
    def node_dict(self):
        return self._node_dict

    def add_node(self, node_item):

        self._node_dict[node_item] = {}

    def add_edge(self, src_node, targ_node):
        self._node_dict[src_node].update({targ_node:random.randint(-2, 10)})

    def edge_exist(self, src_node, targ_node):
        if targ_node in self._node_dict[src_node]:
            return True
        else:
            return False


    def weigth_edge(self):
        weigth = random.randint(-2, 10)

        while weigth == 0:
            weigth = random.randint(-2, 10)

        return weigth

    def init_list(self, nodes, edges):
        for i in range(1, nodes + 1):
            self.add_node(i)

        while edges > 0 :
            src_node = random.randint(1, nodes)
            targ_node = random.randint(1, nodes)

            while self.edge_exist(src_node, targ_node):
                src_node = random.randint(1, nodes)
                targ_node = random.randint(1, nodes)

            self.add_edge(src_node, targ_node)

            edges = edges - 1

    def display(self):

        i = 1
        for src_node, targ_node in self._node_dict.items():
            if targ_node in self._node_dict.values():
                for node, weigth in targ_node.items():
                    if weigth in targ_node.values():
                       # print(i, ". Node", src_node, "linked with node", node, "have a weigth of", weigth, ".")
                        i = i + 1
                        self.graphL.append([src_node, node, weigth])
