#!/usr/bin/python3

"""
CreateDotPlot: Is used to create a dot plot of the found kmer overlap
"""

import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd


def create_combined_plots(positions, title):
    mpl.use('TkAgg')
    fig, axs = plt.subplots(len(positions))
    fig.suptitle(title)
    for index, pos in enumerate(positions):
        axs[index].plot(pos[0], pos[1])
    fig = plt.gcf()
    return fig


def create_dot_plot(positions_x, positions_y, name_one, name_two):
    """
    Creates a dot plot showing the k-mers present in both sequences. The first nucleotide of the duplicate k-mers are
        marked with a dot
    :param name_one:
    :param name_two:
    :param positions_x: A list containing all x positions
    :param positions_y: A list containing all y positions
    :return: a dot plot of the given points
    """
    mpl.use('TkAgg')
    # s is size
    plt.scatter(positions_x, positions_y, s=25)
    plt.ylabel(name_one)
    plt.xlabel(name_two)
    plt.title(f"Genome dot plot {name_one} against {name_two}")

    fig = plt.gcf()
    file = f"../Results/{name_one}-{name_two}.png"
    plt.close()

    return [fig, file]
