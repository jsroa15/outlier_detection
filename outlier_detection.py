import pandas as pd
import numpy as np


def modify_outliers_mean(data, features):
    '''
    This function modifies outliers with mean.
    First, the function detects outliers with Z-score, then calculates the mean of
    the feature without outliers,and finally, replaces outliers with the calculated
    mean.
    Parameters:
    -------------------
    data: dataset to be analyzed
    features: List of numerical features in the dataset
    '''

    to_del = []
    for i in features:

        # Initialize null lists
        ind_upper = []
        ind_lower = []
        ind = []

        # Calculate Z score
        data['Z_score'] = (data[i]-data[i].mean())/data[i].std()
        print(data[(data['Z_score'] > 3) | (data['Z_score'] < -3)
                   ].shape[0], ' outliers detected for ', i)
        to_del.append(data[(data['Z_score'] > 3) |
                           (data['Z_score'] < -3)].shape[0])

        # Identified outliers
        ind = data[(data['Z_score'] > 3) | (data['Z_score'] < -3)].index

        # Calculate mean to replace outlier

        mean_to_replace = data[(data['Z_score'] < 3) &
                               (data['Z_score'] > -3)][i].mean()

        # Replacing outliers
        data.loc[ind, i] = mean_to_replace

    print('total outliers modified: ', sum(to_del))
    data.drop(columns='Z_score', inplace=True)

    return data
