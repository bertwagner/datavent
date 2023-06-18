from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/schedule", response_class=HTMLResponse)
async def schedule(request: Request):
    return templates.TemplateResponse("schedule.html",{"request":request})