#!/usr/bin/python3

"""
CreateDotPlot: Is used to create a dot plot of the found kmer overlap
"""

import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def create_dot_plot(positions_x, positions_y, sequenceOne, sequenceTwo):
    """
    :param positions_x: A list containing all x positions
    :param positions_y: A list containing all y positions
    :return: a dot plot of the given points
    """
    # TODO axis should depect the nucleotides instead of numbers
    df = pd.DataFrame(dict(GenomeOne=positions_x, GenomeTwo=positions_y))
    fig = px.scatter(df, x="GenomeOne", y="GenomeTwo")
    fig.update_traces(marker_size=10)
    fig.update_xaxes(range=[0, len(sequenceOne)-1], fixedrange=True)
    fig.update_yaxes(range=[0, len(sequenceTwo)-1], fixedrange=True)
    fig.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=[*range(len(sequenceOne))],
            ticktext=list(sequenceOne.strip(" "))
        ),
        yaxis=dict(
            tickmode='array',
            tickvals=[*range(len(sequenceTwo))],
            ticktext=list(sequenceTwo.strip(" "))
        )
    )
    fig.show()
