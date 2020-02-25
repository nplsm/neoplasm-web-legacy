from pathlib import Path

import aiohttp_jinja2
import markdown2
from aiohttp import web

PUBLIC_DIR = Path('public')
GENERAL_DIR = PUBLIC_DIR / 'general'


async def index(request: web.Request):
    location = request.app.router['artists'].url_for()
    return web.HTTPFound(location)


@aiohttp_jinja2.template('about.html.jinja2')
async def about(request: web.Request):
    DESCRIPTION_PATH = GENERAL_DIR / 'about' / 'about.md'
    about = markdown2.markdown_path(DESCRIPTION_PATH)
    return {'about': about}
