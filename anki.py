import json
import requests

def add_note(front, back):
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "Programming",
                "modelName": "Basic",
                "fields": {
                    "Front": "front content",
                    "Back": "back content"
                }
            }
        }
    }

    payload['params']['note']['fields']['Front'] = front
    payload['params']['note']['fields']['Back'] = back

    json.dumps(payload)

    requests.post('http://localhost:8765', json.dumps(payload))


def update_note(note_id, front, back):
    payload = {
        "action": "updateNoteFields",
        "version": 6,
        "params": {
            "note": {
                "id": 1,
                "fields": {
                    "Front": "front content",
                    "Back": "back content"
                }
            }
        }
    }

    payload['params']['note']['id'] = note_id
    payload['params']['note']['fields']['Front'] = front
    payload['params']['note']['fields']['Back'] = back

    json.dumps(payload)

    requests.post('http://localhost:8765', json.dumps(payload))


def find_notes():
    payload = {
        "action": "findNotes",
        "version": 6,
        "params": {
            "query": "deck:Programming"
        }
    }
    json.dumps(payload)

    response = requests.post('http://localhost:8765', json.dumps(payload))
    return json.loads(response.content)['result']


def notes_info(note_id):
    payload = {
        "action": "notesInfo",
        "version": 6,
        "params": {
            "notes": [note_id]
        }
    }
    json.dumps(payload)

    response = requests.post('http://localhost:8765', json.dumps(payload))
    return json.loads(response.content)['result']

def html_link(url):
    return f'<a href="{url}">LINK</a>'


def embed_url(url):
    return f'<embed height="800px" src="{url}" type="text/html" width="100%">'