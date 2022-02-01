import matplotlib.pyplot as plt
import seaborn as sns



def Boxplot(DataFrame, n):
    """
        Draws a box plot to show distributions

        Parameters:

        DataFrame: A Pandas DataFrame
                   Dataset for plotting

        n: Integer
           Max number of individual plots to be made in one row


        Returns: 

        Plots Individual box plots based on the number of 
        attributes of dataset

    """
    column = [i for i in DataFrame.columns]
    m = len(column) // n
    #print(m,n)
    plt.figure(figsize=(n*5,(m+1)*5))
    for i in enumerate(column):
        plt.subplot(m+1,n,i[0]+1)
        sns.boxplot(DataFrame[i[1]])
        plt.title("{} distribution".format(i[1]))



def pairplot(DataFrame, n):
    """
        Draws a pairplot between two attributes, generally
        one dependent and one independent variable

        Parameters:

        DataFrame: A Pandas DataFrame
                   Dataset for plotting

        n: Integer
           Max number of individual plots to be made in one row


        Returns: 

        Plots Individual pair plots based on the number of 
        attributes of dataset

    """
    column = [i for i in DataFrame.columns]
    Y = column[-1]
    column = column[:-1]
    m = len(column) // n
    #print(m,n)
    plt.figure(figsize=(n*5,(m+1)*5))
    for i in enumerate(column):
        plt.subplot(m+1,n,i[0]+1)
        sns.regplot(x = DataFrame[i[1]], y = DataFrame[Y],data = DataFrame)
        #plt.title("{} distribution".format(i[1]))

def Scatterplot(DataFrame, n):
    """
        Draws a scatter plot to show distributions

        Parameters:

        DataFrame: A Pandas DataFrame
                   Dataset for plotting

        n: Integer
           Max number of individual plots to be made in one row


        Returns: 

        Plots Individual scatter plots based on the number of 
        attributes of dataset

    """
    column = [i for i in DataFrame.columns]
    m = len(column) // n
    #print(m,n)
    plt.figure(figsize=(n*5,(m+1)*5))
    for i in enumerate(column):
        plt.subplot(m+1,n,i[0]+1)
        sns.scatterplot(DataFrame[i[1]])
        plt.title("{} distribution".format(i[1]))

def Violinplot(DataFrame, n):
    """
        Draws a Violin plot to show distributions, an alternative
        to box plots

        Parameters:

        DataFrame: A Pandas DataFrame
                   Dataset for plotting

        n: Integer
           Max number of individual plots to be made in one row


        Returns: 

        Plots Individual box plots based on the number of 
        attributes of dataset

    """
    column = [i for i in DataFrame.columns]
    m = len(column) // n
    #print(m,n)
    plt.figure(figsize=(n*5,(m+1)*5))
    for i in enumerate(column):
        plt.subplot(m+1,n,i[0]+1)
        sns.violinplot(x = DataFrame[i[1]])
        plt.title("{} distribution".format(i[1]))





