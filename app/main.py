from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import health, players

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("static/index.html")

app.include_router(health.router, prefix=f"/health", tags=["Health"])
app.include_router(players.router, prefix=f"/players", tags=["Players"])