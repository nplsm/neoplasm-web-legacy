import aiohttp_jinja2
from aiohttp import web

from data import *


# Artists
@aiohttp_jinja2.template('artists.html.jinja2')
async def artists_view(request):
    return {'artists': artists_list}


@aiohttp_jinja2.template('artist.html.jinja2')
async def perfecthuman_view(request):
    return perfecthuman_artist


@aiohttp_jinja2.template('artist.html.jinja2')
async def marblebust_view(request):
    return marblebust_artist


@aiohttp_jinja2.template('artist.html.jinja2')
async def ourv_view(request):
    return ourv_artist


# Releases
@aiohttp_jinja2.template('releases.html.jinja2')
async def releases_view(request):
    return {'releases': releases_list}


@aiohttp_jinja2.template('release.html.jinja2')
async def omega_view(requst):
    return omega_release


@aiohttp_jinja2.template('release.html.jinja2')
async def lifeoxetine_view(request):
    return lifeoxetine_release


@aiohttp_jinja2.template('release.html.jinja2')
async def auk_view(request):
    return auk_release

#Events

@aiohttp_jinja2.template('events.html.jinja2')
async def events_view(request):
    return {'events': events_list}

@aiohttp_jinja2.template('event.html.jinja2')
async def eartheater2019_view(request):
    return eartheater2019_event

@aiohttp_jinja2.template('event.html.jinja2')
async def hdmirror2020_view(request):
    return hdmirror2020_event

#About

@aiohttp_jinja2.template('about.html.jinja2')
async def about_view(request):
    return {'about': about}
