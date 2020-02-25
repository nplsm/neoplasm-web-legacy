from datetime import date, datetime
from operator import itemgetter
from pathlib import Path
from typing import Union

import aiohttp_jinja2
from aiohttp import web

from views.utilities import load_meta

PUBLIC_DIR = Path('public')
EVENTS_DIR = PUBLIC_DIR / 'events'


def load_event_meta(TARGET_DIR: Path) -> dict:
    meta = load_meta(TARGET_DIR)
    meta['date'] = datetime.strptime(meta['date'], '%Y-%m-%d')
    return meta


@aiohttp_jinja2.template('events.html.jinja2')
async def events(request: web.Request) -> dict:
    events = []
    for EVENT_DIR in EVENTS_DIR.glob('*/**'):
        events.append(load_event_meta(EVENT_DIR))
    events.sort(key=itemgetter('date'), reverse=True)
    return {'events': events}


@aiohttp_jinja2.template('event.html.jinja2')
async def event(request: web.Request) -> Union[dict, web.HTTPException]:
    event = request.match_info.get('event')
    EVENT_DIR = EVENTS_DIR / event
    if EVENT_DIR.exists():
        return load_event_meta(EVENT_DIR)
    else:
        return web.HTTPBadRequest()
