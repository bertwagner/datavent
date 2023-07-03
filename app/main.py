import os

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

import psycopg2
import psycopg2.extras

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
    conn = psycopg2.connect(f"dbname='{sql_database}' host='{sql_host}' port='{sql_port}' user='{sql_user}' password='{sql_password}'")
    with conn as c:
        cur = c.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = """
            SELECT
                id, 
                name,
                description,
                price,
                is_addon,
                is_coupon
            FROM
                product
            WHERE
                is_coupon=FALSE
            ORDER BY
                id;
            """
        cur.execute(query)
        records = cur.fetchall()

    return templates.TemplateResponse("register.html", {"request": request, "products": records})

class Coupon(BaseModel):
    coupon: str

@app.post("/coupon")
async def coupon(request: Coupon):

    response = {'is_valid': False}

    conn = psycopg2.connect(f"dbname='{sql_database}' host='{sql_host}' port='{sql_port}' user='{sql_user}' password='{sql_password}'")
    with conn as c:
        cur = c.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = """
            SELECT
                id, 
                name,
                description,
                price,
                is_addon,
                is_coupon
            FROM
                product
            WHERE
                description = %(coupon)s
            """
        cur.execute(query, {'coupon': request.coupon})
        records = cur.fetchall()

        if len(records) > 0:
            response['is_valid'] = True
            response['id'] = records[0]['id'] 
            response['name'] = records[0]['name'] 
            response['description'] = records[0]['description'] 
            response['price'] = records[0]['price'] 

    return response


@app.get("/schedule", response_class=HTMLResponse)
async def schedule(request: Request):
    return templates.TemplateResponse("schedule.html", {"request": request})


@app.get("/code-of-conduct", response_class=HTMLResponse)
async def code_of_conduct(request: Request):
    return templates.TemplateResponse("code-of-conduct.html", {"request": request})
