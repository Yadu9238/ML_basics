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



    