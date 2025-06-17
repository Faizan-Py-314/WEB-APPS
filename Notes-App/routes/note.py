from fastapi import APIRouter, FastAPI, Request
from models.note import Note
from schemas.note import noteEntity, notesEntity
from fastapi.responses import HTMLResponse, RedirectResponse
from db.note import database, get_database, delete_note
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):

    notes = get_database()
    return templates.TemplateResponse("index.html", {"request":request, "notes":notes})

@note.post("/")
async def add_note(request: Request):
    form = await request.form()
    notes = database(dict(form))
    return RedirectResponse(url="/", status_code=303)

@note.post("/{id}/delete")
def note_delete(id: int):
    delete_note(id)
    return RedirectResponse(url="/", status_code=303)
