#stock_price_prediction.py


import pandas as pd
import pandas_datareader.data as web
import datetime
import numpy as np
import scipy as sp
import csv
from pprint import pprint

TIME_HORIZON = 30

def loadFeatureMatrix():
    filename = 'feature_matrix.csv'
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    feature_matrix = []
    #dont need to include titles, schema above
    for line in lines[1:]:
        line = line.strip()
        # assuming date is not significant
        feature_matrix.append(line.split(',')[2:])
    return feature_matrix

def prepareFeatures(feature_matrix):
    #create a 30day-future price
    # pprint(features)
    #grab 30:n features and add as feature
    currentPrice =[float(x[0]) for x in feature_matrix[:-TIME_HORIZON]]
    futurePrice = [float(x[0]) for x in feature_matrix[TIME_HORIZON:]]
    features = feature_matrix[:-TIME_HORIZON+1]


    return currentPrice, futurePrice, features

def getInput(features):
    # don't want to cinlude playerID, sting, team, league year in predicition
    LENGTH = len(features)
    WIDTH = len(features[0])-1
    print LENGTH, WIDTH
    X = np.zeros((LENGTH, WIDTH))
    for i in range(0, LENGTH):
        for j in range(0, WIDTH-1):
                X[i, j] = float(features[i][j])
    print X[:5,:]
    return X


def create_output(features, delay):
    Y = numpy.zeros(len(features))
    for i in range(0, len(features)):
        player = features[i][0]
        year = features[i][1]
        if (player, year) in all_stars:
            Y[i] = 1
    print 'Number of all stars', sum(Y)
    return Y



#
#
# def truncateFeatures(features):
#     for i in range(len(features)):
#         features[i] = features[i][:-29]
#     X = features
#     return X
#
# def getOutput(features,delay):
#     Y = sp.zeros(len(features))
#     Y[0] = 0
#     for i in range(1,len(features)):
#         if features[2][i] < delay[i]:
#             Y[i] = 1
#     return Y
#
#
# features = loadFeatures()
# delay = getTimeDelay(features)
# X = truncateFeatures(features)
# Y = getOutput(X,delay)
#
# pprint(X)
# pprint(Y)




def main():
    feature_matrix = loadFeatureMatrix()

    # print (feature_matrix[0])
    # print (feature_matrix[0][0])
    #
    # print type(feature_matrix[0])
    # print type(feature_matrix[0][0])


    currentPrice, futurePrice, features = prepareFeatures(feature_matrix)
    X = getInput(features)

    # print currentPrice[0:5]
    # print futurePrice[0:5]
    # print type(features)
    # print type(features[0])
    # print type(features[0][0])


    # print features[0]
    # print features[0][0]

if __name__ == '__main__':
    main()
