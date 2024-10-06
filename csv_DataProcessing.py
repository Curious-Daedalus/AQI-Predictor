import pandas as pd

def process_csv(input_file):
    headers="PM2.5	PM10	NO	NO2	NOx	NH3	CO	SO2	O3	Benzene	Toluene	Xylene	AQI	AQI_Bucket"
    columns=headers.split()
    
    df = pd.read_csv(input_file)

    df_selected = df[columns]

    df_cleaned = df_selected.dropna()

    return df_cleaned
