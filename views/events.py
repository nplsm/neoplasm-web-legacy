from datetime import datetime, date
from pathlib import Path
from typing import Union

from operator import itemgetter
import aiohttp_jinja2
from aiohttp import web

from views.utilities import load_meta

PUBLIC_DIR = Path('public')
EVENTS_DIR = PUBLIC_DIR / 'events'


@aiohttp_jinja2.template('events.html.jinja2')
async def events(request: web.Request) -> dict:
    events = []

    for EVENT_DIR in EVENTS_DIR.glob('*/**'):
        meta = load_meta(EVENT_DIR)
        meta['date'] = datetime.strptime(meta['date'], '%Y-%m-%d')
        events.append(meta)

    events.sort(key=itemgetter('date'), reverse=True)

    return {'events': events}


@aiohttp_jinja2.template('event.html.jinja2')
async def event(request: web.Request) -> Union[dict, web.HTTPException]:
    event = request.match_info.get('event')
    EVENT_DIR = EVENTS_DIR / event

    if EVENT_DIR.exists():
        meta = load_meta(EVENT_DIR)
        meta['date'] = datetime.strptime(meta['date'], '%Y-%m-%d')
        return meta

    else:
        return web.HTTPBadRequest()
