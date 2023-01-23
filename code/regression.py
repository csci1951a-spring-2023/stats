import numpy as np
import pandas as pd
import random
import statsmodels.api as sm
from statsmodels.tools import eval_measures
from sklearn.metrics import r2_score
import scipy.optimize as opt


def regression(X, Y):
    """
    Implement Linear Regression using StatsModel.

    inputs:
        - train_df: a Pandas DataFrame, containing all the training samples
        - test_df: a Pandas DataFrame, containing all the testing samples
    
    outpus:
        - mse_train: the mean-squared error of the model (trained on the training
                    data), evaluated on the training dataset (float)
        - mse_test: the mean-squared error of the model (trained on the training
                    data), evaluated on the testing dataset (float)
        - rsquared_val: the r-squared value of the model (trained on the training
                    data), evaluated on the testing dataset (float)
    """
    # TODO: Using statsmodel, fit a linear regression model to the training dataset
    

    # TODO: Using statsmodel's eval_measures, calculate the Mean-squared Error of the model above
    # (on the training dataset)

    # TODO: Calculate the *test* R-squared value (using sklearn's r2_score function)

    # TODO: Print out the summary to see more information as needed

    # return the values that we found! :)
    return 

X1 = []
Y1 = []

# TODO: Check you've implemented regression correctly using X1, Y1
regression(X1,Y1)

# TODO: Complete linear_fit_func
def linear_fit_func(x,m,b):
    return 

# TODO: Conduct a linear regression with curve_fit


# TODO: Complete exp_fit_func()
def exp_fit_func(x,A,B,c):
    return 

# TODO: Test curve_fit with exponential function
X2 = []
Y2 = []


# TODO: Implement MSE function
def mse(Y,Y_pred):
    return

