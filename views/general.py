import aiohttp_jinja2
from aiohttp import web


async def index(request):
    location = request.app.router['artists'].url_for()
    return web.HTTPFound(location)


@aiohttp_jinja2.template('about.html.jinja2')
async def about(request):
    pass
