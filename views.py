import aiohttp_jinja2
from aiohttp import web

from data import (about_text, artists_list, events_list, items_list,
                  releases_list)


async def index_view(request):
    raise request.app.router['artists'].url_for()


@aiohttp_jinja2.template('about.html.jinja2')
async def about_view(request):
    return {'about': about_text}


@aiohttp_jinja2.template('artists.html.jinja2')
async def artists_view(request):
    return {'artists': artists_list}


@aiohttp_jinja2.template('artist.html.jinja2')
async def artist_view(request):
    route = request.match_info.get('route')
    for artist in artists_list:
        if route == artist['route']:
            return artist
    raise web.HTTPNotFound()


@aiohttp_jinja2.template('releases.html.jinja2')
async def releases_view(request):
    return {'releases': releases_list}


@aiohttp_jinja2.template('release.html.jinja2')
async def release_view(request):
    route = request.match_info.get('route')
    for release in releases_list:
        if route == release['route']:
            return release
    raise web.HTTPNotFound()


@aiohttp_jinja2.template('events.html.jinja2')
async def events_view(request):
    return {'events': events_list}


@aiohttp_jinja2.template('event.html.jinja2')
async def event_view(request):
    route = request.match_info.get('route')
    for event in events_list:
        if route == event['route']:
            return event
    raise web.HTTPNotFound()


async def items_view(request):
    return {'events': events_list}


async def item_view(request):
    route = request.match_info.get('route')
    return web.Response(text=f'{route}')


async def id_item_view(request):
    route = request.match_info.get('route')
    id = request.match_info.get('id')
    return web.Response(text=f'{id}')


async def legacy_lifeoxetine_item_redirect(request):
    query = request.rel_url.query
    if 'id' in query:
        id = query['id']
        return web.HTTPFound(request.app.router['id_item'].url_for(route='lifeoxetine', id=id))
    else:
        raise web.HTTPNotFound()
