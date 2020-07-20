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


def html_link(url):
    return f'<a href="{url}">LINK</a>'