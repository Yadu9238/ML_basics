from .Mylogger import log

logger = log(path = "logs/", file = "workflow.log")
import pandas as pd 
class DataHandling:
    def __init__(self):
        logger.info("DataHandling obj created")
        print("obj created")

    def _get_missing_values(self, data):
        """Find missing values of given data
        :param data: checked its missing value
        :return: Pandas Series object"""
        # Getting sum of missing values for each feature
        logger.info("Checking for missing values")
        missing_values = data.isnull().sum()
        # Feature missing values are sorted from few to many
        missing_values.sort_values(ascending=False, inplace=True)
        # Returning missing values
        return missing_values


    def fillna(self, data, fill_strategies):
        """Fills missing values with provided mode of fill_strategies

        Parameters:
        Data: Given dataset

        Fill_strategies:
        Strategies include 
              1. None
              2. Value '0'
              3. Mode of the data
              4. Mean of the data
              5. Median of the data

        """
        logger.info("Missing values found in Dataset")
        for column, strategy in fill_strategies.items():
            if strategy == 'None':
                data[column] = data[column].fillna('None')
                logger.info("NA values filled with None")
            elif strategy == 'Zero':
                data[column] = data[column].fillna(0)
                logger.info("NA values filled with 0")
            elif strategy == 'Mode':
                data[column] = data[column].fillna(data[column].mode()[0])
                logger.info("NA values filled with Mode of Data")
            elif strategy == 'Mean':
                data[column] = data[column].fillna(data[column].mean())
                logger.info("NA values filled with Mean of Data")
            elif strategy == 'Median':
                data[column] = data[column].fillna(data[column].median())
                logger.info("NA values filled with Median of data")
            else:
                print("{}: There is no such thing as preprocess strategy".format(strategy))
        return data
        
    def get_outliers(df):
        """
        Used to find the number of outliers in a specific 
        dataset

        Parameters:
        DataFrame: Pandas DataFrame
                   Dataset to be checked for outliers


        Returns:
        Result_df : A Pandas DataFrame
                    DataFrame containing the Attributes of 
                    the dataset along with the number of 
                    outliers in each of them

        """
        logger.info("Trying to find outliers")
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
    
        result_df = pd.DataFrame(((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).sum())
        # print(result_df[0].index)
        logger.info(str(result_df.sum()[0]) + " Outliers Found")
        result_df = pd.DataFrame({'Attributes': result_df[0].index, 'Number of outliers': result_df[0].values})
        
        return result_df


