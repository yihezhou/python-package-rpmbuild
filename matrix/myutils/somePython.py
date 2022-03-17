# -*- coding: utf-8 -*-
"""
@Time    : 2022/3/17 14:51
@Author  : zhou_yihe
@File    : somePython.py
@Software: PyCharm
@Describe:
"""
import numpy


def showMatrix(item, rows, columns):
    matrix = item * numpy.ones((rows, columns))
    return matrix


if __name__ == "__main__":
    print(showMatrix(10, 3, 3))
