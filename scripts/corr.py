# README
# $ python3 corr.py

import pandas
import numpy
import matplotlib.pyplot as plt

def plot_correlation_matrix(df):
    names = df.columns
    correlations = df.corr()
    # plot correlation matrix
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(correlations, vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = list(range(len(df.columns)))
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(names, rotation=20, horizontalalignment='left')
    ax.set_yticklabels(names)
    plt.tight_layout()
    plt.show()

dados = pandas.read_csv('dataset/winequality-whitePREPROC.csv', sep=';')

plot_correlation_matrix(dados)
