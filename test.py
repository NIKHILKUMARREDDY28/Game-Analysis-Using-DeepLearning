from fastapi import FastAPI
from dash import Dash
from dash import dash_table
from dash import  dcc
from dash import html
import pandas as pd
from fastapi.staticfiles import StaticFiles
   

    # Serve the Dash app at /
    
app = FastAPI()
dash_app = Dash(__name__)



df = pd.read_csv('D:\PROJECTS\\NIRFRankPredictor\datasets\EngineeringRanking.csv')

dash_app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("rows"),
)

@app.get("/dash")
def show_dash():
    return dash_app.index()


if __name__ == '__main__':
    from fastapi.responses import HTMLResponse
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.mount("/static", dash_app.server)
    app.run(debug=True, port=8000)
