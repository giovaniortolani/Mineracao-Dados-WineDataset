# README
# $ python3 corr.py

import pandas
import csv

dados = pandas.read_csv('dataset/winequality-white.csv', sep=';')

quality = dados['quality']

# quality_disc = pandas.cut(quality, bins=[0, 4, 7, 10], 
#                     right=True, 
#                     labels=['ruim', 'medio', 'bom'],
#                     retbins=False)
quality_disc = pandas.cut(quality, bins=[0, 6, 10], 
                    right=True, 
                    labels=['ruim', 'bom'],
                    retbins=False)

dados['quality'] = quality_disc

dados.to_csv('dataset/winequality-whitePREPROC.csv', sep=';',
            quoting=csv.QUOTE_NONNUMERIC, index=False)
