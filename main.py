from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder

# database Connection
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
mydb = client["NIRF"]
coll = mydb["Ranks"]
cursor = coll.find({}, {"Institute Name": 1})
colleges = []
for col in cursor:
    colleges.append(col["Institute Name"])

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
def homepage(request : Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.get("/analyze",response_class=HTMLResponse)
def analyze(request : Request):
    return templates.TemplateResponse("analyze.html",{"request":request,"colleges":colleges})
@app.get("/pred")
def homepage(request : Request):
    return templates.TemplateResponse("TLR.html",{"request":request})

@app.get("/RP")
def homepage(request : Request):
    return templates.TemplateResponse("RP.html",{"request":request})

@app.get("/GO",response_class=HTMLResponse)
def homepage(request : Request):
    return templates.TemplateResponse("GO.html",{"request":request})

@app.get("/OI",response_class=HTMLResponse)
def homepage(request : Request):
    return templates.TemplateResponse("OI.html",{"request":request})

@app.get("/PR",response_class=HTMLResponse)
def homepage(request : Request):
    return templates.TemplateResponse("PR.html",{"request":request})