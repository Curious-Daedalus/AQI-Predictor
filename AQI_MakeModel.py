import csv_DataProcessing

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib 
import os

class BoosterRegression:
    def __init__(self) -> None:
        pass
          
    def generateModel(self,CSV_FilePath,modelName="AQI_GradientBoosting"):
        self.CSV_FilePath = CSV_FilePath
        self.modelName = modelName
        self.modelPath = f"models\\{self.modelName}.pkl"

        df = csv_DataProcessing.process_csv(input_file=self.CSV_FilePath)

        x = df.drop(['AQI','AQI_Bucket'], axis=1)
        y = df['AQI']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        # GradientBoostingRegressor algo
        model = GradientBoostingRegressor(n_estimators=300, random_state=42)
        model.fit(x_train, y_train)

        # pickling the model
        if not os.path.exists("models"):
            os.makedirs("models")
        joblib.dump(model, self.modelPath)

        y_pred = model.predict(x_test)

        # R² score
        r2 = r2_score(y_test, y_pred)
        self.r2Value = f"{r2:.3f}"

        # Mean Squared Error
        mse = mean_squared_error(y_test, y_pred)
        self.mseValue = f"{mse:.2f}"


    def details(self):
        try : 
            details = {"Model Name": self.modelName, "CSV_FileTrainData" : self.CSV_FilePath, "R^2 Value" : self.r2Value, "Mean Square Value" : self.mseValue}
        except:
            print("Model doesn't exist")
            return None
        return details

class ForestRegressor:

    def __init__(self) -> None:
        pass
          
    def generateModel(self,CSV_FilePath,modelName="AQI_ForestRegressor"):
        self.CSV_FilePath = CSV_FilePath
        self.modelName = modelName
        self.modelPath = f"models\\{self.modelName}.pkl"

        df = csv_DataProcessing.process_csv(input_file=self.CSV_FilePath)

        x = df.drop(['AQI','AQI_Bucket'], axis=1)
        y = df['AQI']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        # GradientBoostingRegressor algo
        model = RandomForestRegressor(n_estimators=300, random_state=42)
        model.fit(x_train, y_train)

        # pickling the model
        if not os.path.exists("models"):
            os.makedirs("models")
        joblib.dump(model, self.modelPath)

        y_pred = model.predict(x_test)

        # R² score
        r2 = r2_score(y_test, y_pred)
        self.r2Value = f"{r2:.3f}"

        # Mean Squared Error
        mse = mean_squared_error(y_test, y_pred)
        self.mseValue = f"{mse:.2f}"


    def details(self):
        try : 
            details = {"Model Name": self.modelName, "CSV_FileTrainData" : self.CSV_FilePath, "R^2 Value" : self.r2Value, "Mean Square Value" : self.mseValue}
        except:
            print("Model doesn't exist")
            return None
        return details
    

if __name__ == "__main__" :

    address = "archive\\city_day.csv"

    BoosterModel = BoosterRegression()

    BoosterModel.generateModel(CSV_FilePath=address)
    print(BoosterModel.details())

    ForestModel = ForestRegressor()

    ForestModel.generateModel(CSV_FilePath=address)
    print(ForestModel.details())