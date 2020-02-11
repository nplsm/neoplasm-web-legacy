from pathlib import Path

import aiohttp_jinja2
import jinja2
from aiohttp import web

from routes import setup_routes

THIS_DIR = Path(__file__).parent


async def create_app():
    app = web.Application()
    app.update(static_root_url=str('static'))

    jinja2_loader = jinja2.FileSystemLoader(str(THIS_DIR / 'templates'))
    aiohttp_jinja2.setup(app, loader=jinja2_loader)

    setup_routes(app)

    return app