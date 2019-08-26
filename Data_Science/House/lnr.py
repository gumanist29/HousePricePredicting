from pydoc import help
from scipy.stats.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from pandas import DataFrame
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from sklearn.ensemble import RandomForestRegressor
class Data(object):

    @staticmethod
    def data_min(ar):

        print("here")
        filename = 'House/777S.csv'
        dataframe = pd.read_csv(filename)
        X = dataframe.iloc[:, 0:5]
        y = dataframe.iloc[:,-1]
        logReg = LinearRegression()
        logReg.fit(X, y)
        pred = logReg.predict(ar)
        forest_reg = RandomForestRegressor(random_state=55)
        forest_reg.fit(X, y)
        pred=forest_reg.predict(ar)
        return pred
