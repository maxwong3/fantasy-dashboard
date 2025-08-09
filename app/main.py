from fastapi import FastAPI,  Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from routes import health, players

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": "main"})

app.include_router(health.router, prefix=f"/health", tags=["Health"])
app.include_router(players.router, prefix=f"/players", tags=["Players"])