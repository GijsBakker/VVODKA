#!/usr/bin/python3

"""
CreateDotPlot: Is used to create a dot plot of the found kmer overlap
"""

import plotly.express as px
import pandas as pd


def create_dot_plot(positions_x, positions_y, sequenceOne, sequenceTwo):
    """
    Creates a dot plot showing the k-mers present in both sequences. The first nucleotide of the duplicate k-mers are
        marked with a dot
    :param positions_x: A list containing all x positions
    :param positions_y: A list containing all y positions
    :return: a dot plot of the given points
    """
    df = pd.DataFrame(dict(GenomeOne=positions_x, GenomeTwo=positions_y))
    fig = px.scatter(df, x="GenomeOne", y="GenomeTwo")
    fig.update_traces(marker_size=10)
    fig.update_xaxes(range=[0, len(sequenceOne)-1], fixedrange=True)
    fig.update_yaxes(range=[0, len(sequenceTwo)-1], fixedrange=True)
    # if under 50 length replace numbers with the nucleotides
    if len(sequenceOne) <= 50 and len(sequenceTwo) <= 50:
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
