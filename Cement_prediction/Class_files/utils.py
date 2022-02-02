import numpy as np
import pandas as pd
from .Mylogger import log

logger = log(path = "logs/", file = "workflow.log")
def read_data(FileName):
    """
        Reading dataset from local files such as csv, txt or xls

        Parameters:

        FileName: Path to the dataset or if file is in local directory,
                  filename is enough
    
        Returns:

        A Pandas DataFrame with the dataset loaded in

    """
    import os
    logger.info("Trying to load data from {}".format(FileName))
    if FileName not in os.listdir():
        logger.warning("file not in directory")
        logger.info("File not found, couldnt load")
        return 
    
    ext = FileName.split('.')
    
    if 'xls' in ext[1]:
        df = pd.read_excel(FileName)
        logger.info("Provided file contains "+str(df.shape[0])+" rows and "+str(df.shape[1])+" columns")
        logger.info("Successfully loaded {}".format(FileName))
        return df
    if 'txt' in ext[1]:
        df = pd.read_csv(FileName, sep = ' ',header = None)
        logger.info("Provided file contains "+str(df.shape[0])+" rows and "+str(df.shape[1])+" columns")
        logger.info("Successfully loaded {}".format(FileName))
        return df
    if 'csv' in ext[1]:
        df = pd.read_csv(FileName)
        logger.info("Provided file contains "+str(df.shape[0])+" rows and "+str(df.shape[1])+" columns")
        logger.info("Successfully loaded {}".format(FileName))
        return df

def split_data(MyDataFrame,split = 0.2):
    """
        Splits Data in X_train, X_test,y_train,y_test

        Default is 80% training and 20% testing

        Parameters:
        MyDataFrame: Pandas DataFrame,
                     Assumes the last attribute is the target 
                     attribute and rest are independent attributes

        test_size : splitting value of data,
                    default is set as 80:20 ratio


        Returns:
        X_train : List of all the training data

        X_test : List of all testing data

        y_train : Corresponding target values for training data

        y_test : Corresponding target values for testing data

    """
    #DataFrame = DataFrame.copy()
    logger.info("Splitting DataSet into train and test")
    logger.info(str((1-split)*100 )+"% considered for Training, "+str(split*100)+"% for Testing")
    X = MyDataFrame.iloc[:,:-1]
    y = MyDataFrame.iloc[:,-1].values
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    #print(X,y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = split, random_state=2) 
    sc = StandardScaler() 
    X_train = sc.fit_transform(X_train) 
    X_test = sc.transform(X_test)
    logger.info("Splitting DataSet done")
    return X_train, X_test, y_train, y_test
    