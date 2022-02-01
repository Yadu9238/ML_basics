
import pandas as pd 
class DataHandling:
    def __init__(self):
        print("obj created")

    def _get_missing_values(self, data):
        """Find missing values of given data
        :param data: checked its missing value
        :return: Pandas Series object"""
        # Getting sum of missing values for each feature
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
        for column, strategy in fill_strategies.items():
            if strategy == 'None':
                data[column] = data[column].fillna('None')
            elif strategy == 'Zero':
                data[column] = data[column].fillna(0)
            elif strategy == 'Mode':
                data[column] = data[column].fillna(data[column].mode()[0])
            elif strategy == 'Mean':
                data[column] = data[column].fillna(data[column].mean())
            elif strategy == 'Median':
                data[column] = data[column].fillna(data[column].median())
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
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
    
        result_df = pd.DataFrame(((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).sum())
        # print(result_df[0].index)
        result_df = pd.DataFrame({'Attributes': result_df[0].index, 'Number of outliers': result_df[0].values})
        return result_df


def train_on_models(X_train,X_test,y_train,y_test):
    """
       This is a user-defined function that trains 
       the following models with default parameters:

       1. Linear Regression
       2. Decision Tree regressor
       3. K neighbors regressor
       4. Support Vector Machine (RBF Kernel)
       5. Gradient Boosting

       Parameters:

       X_train, X_test, y_train, y_test:

       These are the split data on which model are to be
       trained and tested

       Returns:
       data: Pandas DataFrame
                A Dataframe containing model name, their scores and 
                respective metrics such as Mean-squared-error, 
                R2 score and Mean-Absolute-error


    """
    from sklearn.linear_model import LinearRegression
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.neighbors import KNeighborsRegressor
    from sklearn.svm import SVR
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score 
    import pandas as pd
    models = {
        " Linear Regression"      : LinearRegression(),
        " Decision Trees   "      : DecisionTreeRegressor(),
        " KNN              "      : KNeighborsRegressor(),
        " Support Vector Machine" : SVR(),
        " Gradient Boosting     " : GradientBoostingRegressor()
        }
    results = []
    for name, model in models.items():
            model.fit(X_train,y_train)
            score = model.score(X_test,y_test)
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test,y_pred)
            r2 = r2_score(y_test,y_pred)
            mae = mean_absolute_error(y_test,y_pred)
            results.append([name,score,mse,r2,mae])
            print("Trained on "+name+" with default parameters")
    data = pd.DataFrame(results, columns = ['Model Name', 'Score','MSE','R2 Score', 'MAE'])
    return data 