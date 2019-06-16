#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/5/25 23:53

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

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:1f}'.format

californiua_housing_data = pd.read_csv('california_housing_train.csv')
californiua_housing_data = californiua_housing_data.reindex(np.random.permutation(californiua_housing_data.index))
californiua_housing_data['median_house_value'] /= 1000
print(californiua_housing_data)

# 1.定义特征并配置特征列
# 分类数据：一种文字数据。在本练习中，我们的住房数据集不包含任何分类特征，但您可能会看到的示例包括家居风格以及房地产广告词
# 数值数据：一种数字（整数或浮点数）数据以及您希望视为数字的数据。有时您可能会希望将数值数据（例如邮政编码）视为分类数据
# （我们将在稍后的部分对此进行详细说明）
# 特征列”的结构来表示特征的数据类型。特征列仅存储对特征数据的描述；不包含特征数据本身

# define the input feature: total_rooms
my_feature = californiua_housing_data[['total_rooms']]

# configure a numeric feature column for total_rooms
feature_columns = [tf.feature_column.numeric_column('total_rooms')]

# define the label
target = californiua_housing_data['median_house_value']

# 配置LinearRegressor
# use gradient descent as the optimizer for training the model
# learing_rate控制梯度步长大小。
# clip_gradients_by_norm 将梯度裁剪应用到优化器，避免梯度变得过大。
my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0000001)
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

linear_regressor = tf.estimator.LinearRegressor(
    feature_columns=feature_columns,
    optimizer = my_optimizer
)

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

# 训练模型
_ = linear_regressor.train(input_fn=lambda : my_input_fn(my_feature, target), steps=100)

# 评估模型
# create an input function for predictions.
# note: since we're making just one prediction for each example, we don't
# need to repeat or shuffle the data here.
prediction_input_fn = lambda : my_input_fn(my_feature, target, num_epochs=1, shuffle=False)

# calll predict() on the linear_regressor to make predictions.
predictions = linear_regressor.predict(input_fn=prediction_input_fn)

# format predictions as a NumPy array, so we can calculate error metrics.
predictions = np.array([item['predictions'][0] for item in predictions])

# mean swuared error and root mean sqarued error
mean_squared_error = metrics.mean_squared_error(predictions, target)
root_mean_squared_error = math.sqrt(mean_squared_error)
print('Mean squared error: %0.3f' % mean_squared_error)
print('Root Mean squared error: %0.3f' % root_mean_squared_error)

sample = californiua_housing_data.sample(n=300)
# Get the min and max total_rooms value
x_0 = sample['total_rooms'].min()
x_1 = sample['total_rooms'].max()

# retrieve the final weight and bias generated during training.
weight = linear_regressor.get_variable_value('linear/linear_model/total_rooms/weights')[0]
bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')
print('weight, bias: %s, %s' % (weight, bias) )

# Get the predicted median_house_value for the min and max total_rooms values.
y_0 = weight * x_0 + bias
y_1 = weight * x_1 + bias

print('y0, y1: %s, %s' %(y_0, y_1))
print('x0, x1: %s, %s' %(x_0, x_1))

# Plot our regression line from (x_0, y_0) to (x_1, y_1)
plt.plot([x_0, x_1], [y_0, y_1], c='r')

# Label the graph axes.
plt.ylabel('median_house_value')
plt.xlabel('total_rooms')

#plot a scatter plot fromo our data sample.
plt.scatter(sample['total_rooms'], sample['median_house_value'])

plt.show()



