from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#from fastapi.encoders import jsonable_encoder

# database Connection
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
mydb = client["NIRF"]
coll = mydb["Ranks"]
cursor = coll.find({}, {"Institute Name": 1})
colleges = []
for col in cursor:
    colleges.append(col["Institute Name"])
scores = {}

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

@app.post("/RP",response_class=HTMLResponse)
async def homepage(request : Request, SS : float = Form(...),FSR : float = Form(...),FQE : float = Form(...),FRU : float = Form(...)):
    scores["TLR"] = SS + FSR + FQE + FRU
    return templates.TemplateResponse("RP.html",{"request":request})

@app.post("/GO",response_class=HTMLResponse)
def homepage(request : Request,PU : float = Form(...),QP : float = Form(...),IPR : float = Form(...),FPPP : float = Form(...)):
    scores["RP"] = PU + QP + IPR + FPPP
    return templates.TemplateResponse("GO.html",{"request":request})

@app.post("/OI",response_class=HTMLResponse)
def homepage(request : Request,GPH : float = Form(...),GUE : float = Form(...),GMS : float = Form(...),GPHD : float = Form(...)):
    scores["GO"] = GPH + GUE + GMS + GPHD
    return templates.TemplateResponse("OI.html",{"request":request})

@app.post("/PR",response_class=HTMLResponse)
def homepage(request : Request,RD : float = Form(...),WD : float = Form(...),ESCS : float = Form(...),PCS : float = Form(...)):
    scores["OI"] = RD + WD + ESCS + PCS
    return templates.TemplateResponse("PR.html",{"request":request})

@app.post("/result",response_class=HTMLResponse)
def result(request : Request,PR : float = Form(...)):
    scores["PR"] =  PR
    scores["cum"] = 0.30 * scores["TLR"] + 0.20 * scores["GO"] + 0.10 * scores["PR"] + 0.30 *scores["RP"] + 0.10 * scores["OI"]
    return templates.TemplateResponse("result.html",{"request":request,"scores":scores})
@app.post("/clg",response_class=HTMLResponse)
async def result(request : Request, clg_name : str = Form(...)):
    clg_data = coll.find_one({"Institute Name" : clg_name})
    del clg_data['_id']
    clgid = clg_data['Institute Id']
    clgname = clg_data['Institute Name']
    clg_city = clg_data['City']
    clg_state = clg_data['State']
    
    Perception = {}
    OI = {}
    GO = {}
    RPC = {}
    TLR = {}
    for fie in clg_data.keys():
        
        if "Perception" in fie:
            
            Perception["20" + fie[-2:]] = clg_data[fie]
        elif "OI" in fie:
            OI["20" + fie[-2:]] = clg_data[fie]
        elif "RPC" in fie:
            RPC["20" + fie[-2:]] = clg_data[fie]
        elif "TLR" in fie:
            TLR["20" + fie[-2:]] = clg_data[fie]
        elif "GO" in fie:
            GO["20" + fie[-2:]] = clg_data[fie]
    dates = list(TLR.keys())
    dates.sort()

    return templates.TemplateResponse("output.html",{"request":request,"clgname":clgname,"clgid":clgid,"clg_city":clg_city,"clg_state":clg_state,"Perception":Perception,"OI":OI,"RPC":RPC,"TLR":TLR,"GO":GO,"dates":dates})

    