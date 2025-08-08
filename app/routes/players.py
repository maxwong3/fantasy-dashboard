from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/", tags=["Players"])
def get_players():
    return {"status": "player list"}

@router.get("/{player_id}", tags=["Players"])
def get_player(player_id: int):
    return {"player": f"Got player with ID: {player_id}"}