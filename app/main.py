import os

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import psycopg2

app = FastAPI()
sql_host = os.environ.get("SQL_HOST")
sql_port = os.environ.get("SQL_PORT")
sql_user = os.environ.get("SQL_USER")
sql_password = os.environ.get("SQL_PASSWORD")
sql_database = os.environ.get("SQL_DATABASE")


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/schedule", response_class=HTMLResponse)
async def schedule(request: Request):
    return templates.TemplateResponse("schedule.html", {"request": request})


@app.get("/code-of-conduct", response_class=HTMLResponse)
async def code_of_conduct(request: Request):
    return templates.TemplateResponse("code-of-conduct.html", {"request": request})

@app.get("/pg")
async def pg():
    conn = psycopg2.connect(f"dbname='{sql_database}' host='{sql_host}' port='{sql_port}' user='{sql_user}' password='{sql_password}'")
    with conn as c:
        cur = c.cursor()
        cur.execute("SELECT 'a' as test;")
        records = cur.fetchall()

    return {'message': "connected!"}
