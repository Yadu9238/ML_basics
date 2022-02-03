import numpy as np 
import math
import sys 

from .Mylogger import log

logger = log(path = "logs/", file = "workflow.log")

def calculate_variance(X):
	"""
	Return the variances of the features in dataset X
	"""
	logger.info("Calculating variance")
	mean  = np.ones(np.shape(X)) * X.mean(0)
	n_samples = np.shape(X)[0]

	variance = (1 / n_samples) * np.diag((X - mean).T.dot(X - mean))
	logger.info("Variance is "+str(variance))
	return variance 


def std_deviation(X):
	"""
		Calculates the standard deviations of features 
		in the dataset

	"""
	logger.info("Calculating standard deviation")
	std_dev = np.sqrt(calculate_variance(X))
	logger.info("Standard deviation is "+str(std_dev))
	return std_dev