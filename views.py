import aiohttp_jinja2
from aiohttp import web

from data import artists_list, releases_list, events_list, about

async def index(request):
    raise web.HTTPFound('/artists')

@aiohttp_jinja2.template('about.html.jinja2')
async def about_view(request):
    return {'about': about}

@aiohttp_jinja2.template('artists.html.jinja2')
async def artists_view(request):
    return {'artists': artists_list}


@aiohttp_jinja2.template('artist.html.jinja2')
async def artist_view(request):
    route = request.match_info.get('route')
    for artist in artists_list:
        if route == artist['route']:
            return artist
    raise web.HTTPFound('/artists')


@aiohttp_jinja2.template('releases.html.jinja2')
async def releases_view(request):
    return {'releases': releases_list}


@aiohttp_jinja2.template('release.html.jinja2')
async def release_view(request):
    route = request.match_info.get('route')
    for release in releases_list:
        if route == release['route']:
            return release
    raise web.HTTPFound('/releases')


@aiohttp_jinja2.template('events.html.jinja2')
async def events_view(request):
    return {'events': events_list}


@aiohttp_jinja2.template('event.html.jinja2')
async def event_view(request):
    route = request.match_info.get('route')
    for event in events_list:
        if route == event['route']:
            return event
    raise web.HTTPFound('/events')
