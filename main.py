from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/news")
def get_news():
    conn = sqlite3.connect("nba_news.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, url FROM news")
    rows = cursor.fetchall()
    conn.close()
    return [{"title": row[0], "url": row[1]} for row in rows]

#檢查網站的網址是: http://127.0.0.1:8000