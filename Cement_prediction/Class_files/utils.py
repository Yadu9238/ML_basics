import numpy as np
import pandas as pd


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
    if FileName not in os.listdir():
        print("Error file not in directory")
    
    ext = FileName.split('.')
    
    if 'xls' in ext[1]:
        df = pd.read_excel(FileName)
        return df
    if 'txt' in ext[1]:
        df = pd.read_csv(FileName, sep = ' ',header = None)
        return df
    if 'csv' in ext[1]:
        df = pd.read_csv(FileName)
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
    X = MyDataFrame.iloc[:,:-1]
    y = MyDataFrame.iloc[:,-1].values
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    #print(X,y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = split, random_state=2) 
    sc = StandardScaler() 
    X_train = sc.fit_transform(X_train) 
    X_test = sc.transform(X_test)

    return X_train, X_test, y_train, y_test
    