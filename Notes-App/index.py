from fastapi import FastAPI, Request
from routes.note import note
from fastapi.staticfiles import StaticFiles


app = FastAPI()

note.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(note)
