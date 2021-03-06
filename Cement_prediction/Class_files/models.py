#Defining the class


import operator
from .metrics import euclidean_distance

from .Mylogger import log

logger = log(path = "logs/", file = "workflow.log")

class MyLinearRegression:
    """
        Linear Regression is a simple supervised learning algorithm 
        used for regression analysis

    """



    def __init__(self, x , y):
        logger.info("Linear Regression obj created")
        self.data = x
        self.label = y
        self.m = 0
        self.b = 0
        self.n = len(x)
         
    def fit(self , epochs , lr):
        logger.info("Trying to fit Linear regression ")
        #Implementing Gradient Descent
        for i in range(epochs):
            y_pred = self.m * self.data + self.b
             
            #Calculating derivatives w.r.t Parameters
            D_m = (-2/self.n)*sum(self.data * (self.label - y_pred))
            D_b = (-1/self.n)*sum(self.label-y_pred)
             
            #Updating Parameters
            self.m = self.m - lr * D_m
            self.c = self.b - lr * D_c
             
    def predict(self , inp):
        y_pred = self.m * inp + self.b 
        return y_pred


class MyKNN:
    """
       KNN - K Nearest Neighbors algorithm is a simple supervised
       algorithm which can be used to solve both regression and 
       classification problem


    """


    def __init__(self,x,y):
        logger.info("KNN obj created")
    
    def knn(trainingSet, testInstance, k):
        """
        returns the nearest neighbour classification when a dataset
        and a datapoint is passed

        Parameters:

        trainingSet: List
                     Set of DataPoints on the KNN algorithm is to be
                     trained
        testInstance: List
                      DataPoints which is to be classified

        K : Int
            Number of neighbours to consider for the KNN algorithm


        Euclidean Distance is defined in metrics.py
        """
        logger.info("Training for KNN started")
        distances = {}
        sort = {}
        
        length = testInstance.shape[1]
        for x in range(len(trainingSet)):
            dist = euclidean_distance(testInstance, trainingSet.iloc[x], length) 
            distances[x] = dist
            sorted_d = sorted(distances.items(), key = operator.itemgetter(1))
        neighbors = []
            
        for x in range(k):
            neighbors.append(sorted_d[x][0])
        classVotes = {}
        for x in range(len(neighbors)):
            response = trainingSet.iloc[neighbors[x]][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
                
        sortedVotes = serted(classVotes.items(), key = operator.itemgetter(1))
        logger.info("Training done")
        return sortedVotes[0][0]



class MyLogisticRegression:

    """
    Logistic Regression is a statistical analysis method to predict a binary
    outcome


    """
    def __init__(self, learning_rate, iterations):
        self.learning_rate = learning_rate
        self.iterations = iterations
        logger.info("MyLogisticRegression obj created")

    def fit(self, X, Y):
        self.m, self.n = X.shape

        logger.info("Fitting for Logistic Regression")
        #weight initialization

        self.W = np.zeros(self.n)
        self.b = 0
        self.X = X 
        self.Y = Y 

        #gradient descent learning 

        for i in range(self.iterations):
            self.update_weights()
        return self

    def update_weights(self):
        """
            equation of logistic reg is given by:
             y = 1/(1 + e^(-(w.x + b)))
        
            where w is weights and bias


        """
        A = 1/ (1 + np.exp(- (self.X.dot(self.W) + self.b) ) )

        temp = (A - self.Y.T)
        temp = np.reshape(temp, self.m)

        dW = np.dot(self.X.T, temp) / self.m
        db = np.sum(temp) / self.m 

        #updating weights
        self.W = self.W - self.learning_rate * dW 
        self.b = self.b - self.learning_rate * db 

        return self

    def predict(self, X):
        Z = 1 / (1 + np.exp( - (X.dot(self.W) + self.b)))
        Y = np.where(Z > 0.5,1,0)
        return y_pred

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
            logger.info("Trained on "+name)
            logger.info("Score = "+str(round(score,4))+"|MSE = "+str(round(mse,4))+"|R2 score ="+str(round(r2,4))+"|MAE = "+str(round(mae,4)))
            logger.info("- - - - - - - - - - - - - - -")
    data = pd.DataFrame(results, columns = ['Model Name', 'Score','MSE','R2 Score', 'MAE'])
    return data 





