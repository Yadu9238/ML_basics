from .Mylogger import log
logger = log(path = "logs/", file = "workflow.log")

def save_results(df, name):
	"""
		Save the DataFrame to a text file

		Parameters:
		df: Pandas Dataframe,
		    Data to be saved
		
		name: Name of file for the data
		      be stored in
		Returns:
		Saves the data in the file in the 
		current working directory

	"""
	logger.info("Opening {}".format(name))
	myFile = open(name, mode = 'w')
	myFile.write(df.to_string(index = False))
	myFile.close()
	logger.info("Results saved in " + name+" file")


