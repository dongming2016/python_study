#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/5/26 10:14
from __future__ import print_function
import math
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import  Dataset
from IPython import display

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:1f}'.format

californiua_housing_data = pd.read_csv('california_housing_train.csv')
californiua_housing_data = californiua_housing_data.reindex(np.random.permutation(californiua_housing_data.index))
californiua_housing_data['median_house_value'] /= 1000
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    '''
    Trains a linear regresssion model of one feature.
    :param features: :pandas DataFrame of features
    :param targets:  pandas DataFrame of targets
    :param batch_size:  Size of batches to be passed to the model
    :param shuffle:  Whether to shuffle the data.
    :param num_epochs: Number of epochs for which data  should be repeated. None = repeat indefinitetly
    :return:
        Tuple of (features, labels) for next data batch
    '''

    # convert pandas data into a dict of np arrays.
    features = {key: np.array(value) for key, value in dict(features).items()}

    # construct a dataset, and configure batching/repeating.
    ds = Dataset.from_tensor_slices((features, targets))
    ds = ds.batch(batch_size).repeat(num_epochs)

    # Shuffle the data, if specified
    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    # return the next batch of data
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels

def train_model(learing_rate, steps, batch_size, input_feature='total_rooms'):
    '''

    :param learing_rate: A 'float', the learning rate
    :param steps: A non-zero 'int', the total number of training steps. A training step consists of a forward pass using a single batch.
    :param batch_size:
    :param imput_feature:
    :return:
    '''
    periods = 10
    steps_per_period = steps / periods

    my_feature = input_feature
    my_feature_data = californiua_housing_data[[input_feature]]
    my_label = 'median_house_value'
    target = californiua_housing_data[my_feature]

    # create feature columns.
    feature_column = [tf.feature_column.numeric_column(my_feature)]

    # create input functions
    print(batch_size)
    training_input_fn = lambda : my_input_fn(my_feature_data, target, batch_size=batch_size)
    prediction_input_fn = lambda : my_input_fn(my_feature_data, target, num_epochs=1, shuffle=False)

    # createe a linear regressor object
    my_optimizer =  tf.train.GradientDescentOptimizer(learning_rate=learing_rate)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
    linear_regressor = tf.estimator.LinearRegressor(feature_columns=feature_column, optimizer = my_optimizer)

    # set up to plot the  state of our model's line each period.
    plt.figure(figsize=(15, 16))
    plt.subplot(1, 2, 1)
    plt.title('Learned Line by Period')
    plt.ylabel(my_label)
    plt.xlabel(my_feature)
    sample = californiua_housing_data.sample(n=300)
    plt.scatter(sample[my_feature], sample[my_label])
    colors = [cm.coolwarm(x) for x in np.linspace(-1, 1, periods)]

    # train the model, but do so inside a loop so that we can periodically assess loss metrics.
    print('training model...')
    print('RMSE (on training data')
    root_mean_squared_errors = []
    for period in range(0, periods):
        linear_regressor.train(
            input_fn = training_input_fn,
            steps = steps_per_period
        )
        # take a break and compute predictions
        predictions = linear_regressor.predict(input_fn=prediction_input_fn)
        print('predictions: %s' % predictions)
        predictions = np.array([item['predictions'][0] for item in predictions])
        print('predictions1: %s' % predictions)

        # compute loss.
        root_mean_squared_error = math.sqrt(metrics.mean_squared_error(predictions, target))
        print('period %02d: %0.2f' % (period, root_mean_squared_error))
        root_mean_squared_errors.append(root_mean_squared_error)
        # finally, track the weights and biases over time
        # apply some math to ensure that the data and line are plotted neatly.
        y_extents = np.array([0, sample[my_label].max()])

        weight = linear_regressor.get_variable_value('linear/linear_model/%s/weights' % input_feature)
        bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')

        x_extents = (y_extents - bias) / weight
        x_extents = np.maximum(np.minimum(x_extents, sample[my_feature].max()), sample[my_feature].min())

        y_extents = weight * x_extents + bias
        plt.plot(x_extents, y_extents, color=colors[period])
    print('model training finished.')

    # output a grapgh of loss metrics over periods
    plt.subplot(1, 2, 2)
    plt.ylabel('RMSE')
    plt.xlabel('Periods')
    plt.title('root mean squared error vs. periods')
    plt.tight_layout()
    plt.plot(root_mean_squared_error)

    # output a table with calibration data.
    calibration_data = pd.DataFrame()
    calibration_data['predictions'] = pd.Series(predictions)
    calibration_data['target'] = pd.Series(target)
    display.display(calibration_data.describe())

    print('Final RMSE (on training data): %0.2f' % root_mean_squared_error)

if __name__ == '__main__':
    train_model(
        learing_rate=0.00001,
        steps=100,
        batch_size=1
    )