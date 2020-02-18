from pathlib import Path
from typing import Union

import aiohttp_jinja2
from operator import itemgetter
from aiohttp import web

from views.utilities import load_meta

PUBLIC_DIR = Path('public')
ARTISTS_DIR = PUBLIC_DIR / 'artists'


@aiohttp_jinja2.template('artists.html.jinja2')
async def artists(request: web.Request) -> dict:
    artists = []

    for ARTIST_DIR in ARTISTS_DIR.glob('*/**'):
        meta = load_meta(ARTIST_DIR)
        artists.append(meta)

    artists.sort(key=itemgetter('display_name'))

    return {'artists': artists}


@aiohttp_jinja2.template('artist.html.jinja2')
async def artist(request: web.Request) -> Union[dict, web.HTTPException]:
    artist = request.match_info.get('artist')
    ARTIST_DIR = ARTISTS_DIR / artist

    if ARTIST_DIR.exists():
        meta = load_meta(ARTIST_DIR)
        return meta

    else:
        return web.HTTPBadRequest()
