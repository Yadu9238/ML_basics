import numpy as np 
import math
import sys 

from .Mylogger import log

logger = log(path = "logs/", file = "workflow.log")

def mean_squared_error(y_true, y_pred):
	"""
		Returns the mean squared error between y_true 
		and y_pred

	"""
	logger.info("MSE function called")
	mse = np.mean(np.power(y_true - y_pred,2))
	return mse 


def euclidean_distance(x1,x2):
	"""
		Calculates the euclidean distance between two
		sets of points.

		Parameters:
		x1,x2 : lists
				Array of points which represent the dataset

		Returns:

		Euclidean distance between those points

	"""
	logger.info("Euclidean distance here")
	distance = 0 
	for i in range(len(x1)):
		distance += pow((x1[i] - x2[i]),2)

	logger.info("distance calculated")
	return math.sqrt(distance)


def accuracy_score(y_true,y_pred):
	"""
		Compares actual Y value and predicted Y value
		and returns the accuracy

	"""
	logger.info("Calculating Accuracy")
	accuracy = np.sum(y_true == y_pred, axis = 0) / len(y_true)
	logger.info("Accuracy calculated")
	return accuracy 


def calculate_variance(X):
	"""
	Return the variances of the features in dataset X
	"""

	mean  = np.ones(np.shape(X)) * X.mean(0)
	n_samples = np.shape(X)[0]

	variance = (1 / n_samples) * np.diag((X - mean).T.dot(X - mean))

	return variance 



def std_deviation(X):
	"""
		Calculates the standard deviations of features 
		in the dataset

	"""
	std_dev = np.sqrt(calculate_variance(X))
	return std_dev

