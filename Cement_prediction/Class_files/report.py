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
	myFile = open(name, mode = 'w')
	myFile.write(df.to_string(index = False))
	myFile.close()
	print("Results saved in " + name+" file")


