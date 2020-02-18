from datetime import datetime, timedelta
from pathlib import Path
from typing import Union

from operator import itemgetter

import aiohttp_jinja2
from aiohttp import web

from views.utilities import load_meta

PUBLIC_DIR = Path('public')
RELEASES_DIR = PUBLIC_DIR / 'releases'
ARTISTS_DIR = PUBLIC_DIR / 'artists'


@aiohttp_jinja2.template('releases.html.jinja2')
async def releases(request: web.Request) -> dict:
    releases = []

    for RELEASE_DIR in RELEASES_DIR.glob('*/**'):
        meta = load_meta(RELEASE_DIR)
        meta['artist'] = load_meta(ARTISTS_DIR / meta['artist'])
        releases.append(meta)

    releases.sort(key=itemgetter('date'), reverse=True)
    
    return {'releases': releases}


@aiohttp_jinja2.template('release.html.jinja2')
async def release(request: web.Request) -> Union[dict, web.HTTPException]:
    release = request.match_info.get('release')
    RELEASE_DIR = RELEASES_DIR / release

    if RELEASE_DIR.exists():
        meta = load_meta(RELEASE_DIR)
        meta['artist'] = load_meta(ARTISTS_DIR / meta['artist'])

        total_length = timedelta(0)
        for track in meta['tracklist']:
            track_minutes = int(track['length'].split(':')[0])
            track_seconds = int(track['length'].split(':')[1])
            track_length = timedelta(minutes=track_minutes, seconds=track_seconds)
            total_length += track_length

        meta['total_length'] = ':'.join(str(total_length).split(':')[1:])

        return meta

    else:
        return web.HTTPBadRequest()
