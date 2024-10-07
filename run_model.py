import joblib 
import pandas as pd

def userInput(columns):
    data={}
    for column in columns :
        data[column] = [float(input(f"Enter {column} value : "))]
    return data


def  run_model(modelPath):
    model = joblib.load(modelPath)

    columns=['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene']
    
    data = pd.DataFrame(userInput(columns=columns))

    future_AQI = model.predict(data)

    print(data)
    print(f'Predicted AQI for the given values : {future_AQI[0]:.2f}')

if __name__ == "__main __":
    run_model("models\\AQI_GradientBoosting.pkl")