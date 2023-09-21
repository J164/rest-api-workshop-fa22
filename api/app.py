from http.client import BAD_REQUEST, OK
from flask import Flask, abort, request
from flask_cors import CORS

events = {
    # Here is an example event:
    0: {
        "name": "OSAI Social",
        "category": "food",
        "location": "CIF 1038",
        "date": "Oct 6th 2022 7PM",
    },
    1: {
        "name": "OSAI Event",
        "category": "stuff",
        "location": "CIF 1038",
        "date": "Oct 13th 2022 7PM",
    }
}

app = Flask(__name__)
CORS(app)


@ app.get("/")
def get_default():
    return {"message": "I <3 Open-Source at Illinois"}


@ app.get("/events")
def get_all():
    """
    Returns a map of all events to their event ID
    """

    return events


@ app.get("/events/<event_id>")
def get_event(event_id: int):
    """
    Returns the event object for the given event_id
    """

    event_id = int(event_id)
    return events[event_id]


@ app.post("/events")
def new():
    """
    Stores a new event object in the database
    """

    events[len(events)] = request.json
    return request.json


@ app.patch("/events/<event_id>")
def update(event_id: int):
    """
    Updates the event object for the given event_id
    """

    events[event_id] = request.json
    return request.json


@ app.delete("/events/<event_id>")
def delete(event_id: int):  # no error handling
    """
    Deletes the event object for the given event_id
    """

    event_id = int(event_id)
    return events.pop(event_id)

if __name__ == '__main__':
    app.run()
