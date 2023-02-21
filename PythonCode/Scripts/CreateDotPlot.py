#!/usr/bin/python3

"""
CreateDotPlot: Is used to create a dot plot of the found kmer overlap
"""

import pandas as pd
import matplotlib.pyplot as plt


def create_dot_plot(positions_x, positions_y):
    """
    :param positions_x: A list containing all x positions
    :param positions_y: A list containing all y positions
    :return: a dot plot of the given points
    """
    print(positions_x)
    print(positions_y)
    plt.scatter(positions_x, positions_y)
    plt.show()

