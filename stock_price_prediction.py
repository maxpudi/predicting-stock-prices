#stock_price_prediction.py


import pandas as pd
import pandas_datareader.data as web
import datetime
import numpy as np
import scipy as sp
import csv
from pprint import pprint

TIME_HORIZON = 30

def loadData():

    data_df = pd.DataFrame.from_csv('feature_matrix.csv')
    print data_df[-5:]


    #load feature headers
    filename = 'features.csv'
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    FEATURES = []
    for line in lines[1:]:
        line = line.strip()
        FEATURES.append(line)

    #load label headers
    LABEL = 'label'

    #create input
    X = np.array(data_df[FEATURES].values)
    y = np.array(data_df[LABEL].values)

    print X[-5:]
    print y[-5:]





    # return feature_matrix


def main():
    loadData()
    # currentPrice, futurePrice, features = prepareFeatures(feature_matrix)
    # X = getInput(features)

    # print currentPrice[0:5]
    # print futurePrice[0:5]
    # print type(features)
    # print type(features[0])
    # print type(features[0][0])


    # print features[0]
    # print features[0][0]

if __name__ == '__main__':
    main()
