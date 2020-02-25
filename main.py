import asyncio
from pathlib import Path

import aiohttp_jinja2
import jinja2
import uvloop
from aiohttp import web

from routes import setup_routes

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

THIS_DIR = Path(__file__).parent

async def create_app():
    app = web.Application()
    app['static_root_url'] = 'public'

    jinja2_loader = jinja2.FileSystemLoader(str(THIS_DIR / 'templates'))
    aiohttp_jinja2.setup(app, loader=jinja2_loader)

    setup_routes(app)

    return app
