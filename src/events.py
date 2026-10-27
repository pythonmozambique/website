import json
from datetime import date

from browser import ajax, html


def event_label(event):
    full_date = event.get("fullDate", "")
    location = event.get("location", "")
    if full_date and location:
        return f"{full_date} · {location}"
    return full_date or location


def make_card(name, label, image, url):
    if url:
        card = html.A(href=url, target="_blank", Class="event-card")
    else:
        card = html.DIV(Class="event-card")
    card <= html.IMG(src=image, alt=name, Class="event-image")
    card <= html.H3(name)
    card <= html.P(label or "")
    return card


def sort_events(events):
    today = date.today().isoformat()
    upcoming = [event for event in events if event["date"] >= today]
    past = [event for event in events if event["date"] < today]
    upcoming.sort(key=lambda event: event["date"])
    past.sort(key=lambda event: event["date"], reverse=True)
    return upcoming + past


def create():
    sec = html.DIV(Id="eventos", Class="section")
    sec.attrs["data-aos"] = "fade-up"

    sec <= html.H2("Eventos e Colaborações")
    ev_container = html.DIV(Class="events-container")
    sec <= ev_container

    sec <= html.H2("Nossas Comunidades")
    com_container = html.DIV(Class="events-container")
    sec <= com_container

    def fill_events(req):
        for event in sort_events(json.loads(req.text)):
            ev_container <= make_card(
                event["name"], event_label(event), event["image"], event.get("url", ""))

    def fill_communities(req):
        for community in json.loads(req.text):
            com_container <= make_card(
                community["name"], "", community["image"], community.get("url", ""))

    ajax.get("data/events.json", oncomplete=fill_events)
    ajax.get("data/communities.json", oncomplete=fill_communities)
    return sec


def bind(document):
    pass
