from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", tags=["Players"])
def get_players(request: Request):
    return templates.TemplateResponse("player_stats.html", {"request": request})

@router.get("/{player_id}", tags=["Players"])
def get_player(player_id: int):
    return {"player": f"Got player with ID: {player_id}"}