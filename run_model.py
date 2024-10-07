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
    
    # future_X = pd.DataFrame({'PM2.5' : [25.58],'PM10' : [91.73],'NO': [17.5],'NO2': [39.32], 'NOx': [20.13], 'NH3': [5.7], 'CO': [0.02], 'SO2': [10.14], 'O3': [2.3], 'Benzene': [5.97], 'Toluene': [15.23], 'Xylene': [4.13]})
    data = pd.DataFrame(userInput(columns=columns))

    future_AQI = model.predict(data)

    print(data)
    print(f'Predicted AQI for the given values : {future_AQI[0]:.2f}')

if __name__ == "__main __":
    run_model("models\\AQI_GradientBoosting.pkl")