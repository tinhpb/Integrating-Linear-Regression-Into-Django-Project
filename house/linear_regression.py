import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

def getData():
    # Get home data from CSV file
    dataFile = pd.read_csv('house/data/mydata.csv')
    return dataFile

def linearRegressionModel(X_train, Y_train, X_test, Y_test):
    linear = linear_model.LinearRegression()
    # Training process
    linear.fit(X_train, Y_train)
    # Evaluating the model
    score_trained = linear.score(X_test, Y_test)
    # y_pre = linear.predict(X_test)
    # print('--------------------------------------------------------')
    # print('Gia du doan: '+ repr(int(y_pre[0])) + ', gia thuc te: ' + repr(int(Y_test[0])))
    # print('--------------------------------------------------------')
    # print('He so:', linear.coef_)
    # print('--------------------------------------------------------')
    return score_trained

def heso(X_train, Y_train, X_test, Y_test):
    linear = linear_model.LinearRegression()
    # Training process
    linear.fit(X_train, Y_train)
    return linear.coef_

def test():
    print('hello')
    return

def main():
    data = getData()
    if data is not None:
        # Selection few attributes
        attributes = list(
            [
            'distance_to_citycenter',
            'distance_to_airport',
            'distance_to_station',
            'year_built',
            'num_room',
            'num_bed',
            'num_bath',
            'living_area'
            ]
        )
        # Vector attributes of house
        X = data[attributes]
        # Vector price of house
        Y = data['askprice']
        
        # Split data to training test and testing test
        X_train, X_test, Y_train, Y_test = train_test_split(np.array(X), np.array(Y), test_size=0.2)
        
        # Linear Regression Model
        linearScore = linearRegressionModel(X_train, Y_train, X_test, Y_test)
        # print ('Linear Score = ' , linearScore)
        a=heso(X_train, Y_train, X_test, Y_test)
        return a, linearScore
