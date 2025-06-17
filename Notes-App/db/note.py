import json

def database(note):
    with open("db/notes.json", "r") as f:
        notes = json.load(f)

    with open("db/notes.json", "w") as h:
        if len(notes) == 0:
            notes.append({"id":0, "note":note})
        else:
            notes.append({"id":(notes[len(notes)-1]["id"]+1), "note":note})
        json.dump(notes, h)
    
    return notes

def get_database():
    with open("db/notes.json", "r") as f:
        notes = json.load(f)
    
    return notes

def delete_note(id):
    with open("db/notes.json", "r") as f:
        notes = json.load(f)
    
    for i, note in enumerate(notes):
        if note["id"] == id:
            del notes[i]
    
    with open("db/notes.json", "w") as h:
        json.dump(notes, h)
