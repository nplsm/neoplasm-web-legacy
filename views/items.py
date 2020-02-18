import aiohttp_jinja2
from aiohttp import web


@aiohttp_jinja2.template('items.html.jinja2')
async def items(request):
    pass


@aiohttp_jinja2.template('item.html.jinja2')
async def item(request):
    pass


@aiohttp_jinja2.template('registered_item.html.jinja2')
async def page(request):
    pass


@aiohttp_jinja2.template('unregistered_item.html.jinja2')
async def registration(request):
    pass


async def get_release(request):
    await web.FileResponse()


async def get_stems(request):
    await web.FileResponse()


async def legacy_lifeoxetine_item_redirect(request):
    query = request.rel_url.query
    if 'id' in query:
        uuid = query['id']
        location = request.app.router['unregistered_item'].url_for(
            name='lifeoxetine', uuid=uuid
        )
        return web.HTTPFound(location)
    else:
        raise web.HTTPNotFound()
