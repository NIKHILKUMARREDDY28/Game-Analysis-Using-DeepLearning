from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")



@app.get("/",response_class=HTMLResponse)
def homepage(request : Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.route("/pred")
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