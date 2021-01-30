from fastapi import FastAPI
from game.algorithm import play_game

app = FastAPI(title="Paper Rock and Scissors Game Algorithm in Python")

@app.post("/play/{option}", tags=['Play Game'])
async def play(option:str):
    return play_game(option)