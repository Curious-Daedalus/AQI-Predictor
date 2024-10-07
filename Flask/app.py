from flask import Flask, render_template

app = Flask(__name__)

# Routing (Can be used twice)
@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')

# Dynamic Route 
@app.route("/about")
def about_page():
    return render_template('about.html')


if __name__ == "__main__" :
    app.run(debug=True)

# from flask import Flask, render_template
# import plotly.express as px
# import pandas as pd
# import plotly
# import json

# app = Flask(__name__)

# # Route for the home page
# @app.route('/')
# def home():
#     # Load the CSV file into a pandas DataFrame
#     df = pd.read_csv('amravati.csv')  # Make sure to replace 'data.csv' with your actual CSV file path

#     # Plot using Plotly (assuming your CSV has columns 'x_column' and 'y_column')
#     fig = px.line(df, x='Date', y='AQI', title='AQI value',
#                   labels={'x_column': 'X Axis', 'y_column': 'Y Axis'})
    
#     # Convert the plotly figure to JSON
#     graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
#     # Pass the JSON graph to the template
#     return render_template('plotly.html', graphJSON=graphJSON)

# if __name__ == '__main__':
#     app.run(debug=True)
