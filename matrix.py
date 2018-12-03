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


def random_adjacency_matrix(n, m):
    matrix = []
    cpt = 0

    for i in range(m):
        node = []

    while cpt != m:
        for i in range(m):
            node = []
            for j in range(n):
                if random.randint(0, 1) == 0:
                    node.append({"node: ":j})
                    cpt += 1
                else:
                    matrix.append(node)

    return matrix
