import uuid
from operator import itemgetter
from pathlib import Path
from typing import Union
import secrets


import aiohttp_jinja2
import aioredis
from aiohttp import web

from views.utilities import load_meta

PUBLIC_DIR = Path('public')
ITEMS_DIR = PUBLIC_DIR / 'items'
RELEASES_DIR = PUBLIC_DIR / 'releases'
ARTISTS_DIR = PUBLIC_DIR / 'artists'

def load_item_meta(TARGET_DIR: Path) -> dict:
    meta = load_meta(TARGET_DIR)
    meta['release'] = load_meta(RELEASES_DIR / meta['release'])
    meta['release']['artist'] = load_meta(ARTISTS_DIR / meta['release']['artist'])
    return meta


@aiohttp_jinja2.template('items.html.jinja2')
async def items(request: web.Request) -> dict:
    items = []
    for ITEM_DIR in ITEMS_DIR.glob('*/**'):
        items.append(load_item_meta(ITEM_DIR))
    items.sort(key=itemgetter('date'), reverse=True)
    return {'items': items}


@aiohttp_jinja2.template('item.html.jinja2')
async def item(request: web.Request) -> Union[dict, web.HTTPException]:
    item = request.match_info.get('item')
    ITEM_DIR = ITEMS_DIR / item
    if ITEM_DIR.exists():
        return load_item_meta(ITEM_DIR)
    else:
        return web.HTTPBadRequest()

# @aiohttp_jinja2.template('item.html.jinja2')
# async def page(request):
#     item = request.match_info.get('item')
#     number = request.match_info.get('number')
#     return web.Response(text=f'item: {item}\nnumber: {number}')


@aiohttp_jinja2.template('item.html.jinja2')
async def registration(request: web.Request):
    item = request.match_info.get('item')
    uuid = request.match_info.get('uuid')
    ITEM_DIR = ITEMS_DIR / item
    meta = load_item_meta(ITEM_DIR)
    if ITEM_DIR.exists():
        redis = await aioredis.create_redis_pool('redis://localhost')
        if await redis.sismember(f'{item}-item:uuids', uuid):
            meta['pipi'] = 'pipi'
            meta['uuid'] = uuid
            meta['stems'] = ITEM_DIR / f'{item}_stems.zip'
            if not await redis.sismember(f'{item}-item:activated-uuids', uuid):
                secret = secrets.token_urlsafe(8)
                await redis.hmset_dict(secret,
                        item=item,
                        uuid=uuid,
                    )
                await redis.expire(secret, 500)
                meta['secret'] = secret
            response = meta
        else:
            meta['pipi'] = 'popo'
            response = web.HTTPBadRequest()
        redis.close()
        await redis.wait_closed()
    else:
        response = web.HTTPBadRequest()
    return response


async def get_file(request: web.Request):
    item = request.match_info.get('item')
    uuid = request.match_info.get('uuid')
    filename = request.match_info.get('filename')
    FILE_PATH = ITEMS_DIR / item / filename

    if FILE_PATH.exists():
        redis = await aioredis.create_redis_pool('redis://localhost')
        if await redis.sismember(f'{item}-item:uuids', uuid):
            response = web.FileResponse(FILE_PATH)
        else:
            response = web.HTTPBadRequest()
        redis.close()
        await redis.wait_closed()
    else:
        response = web.HTTPBadRequest()
    return response


async def legacy_lifeoxetine_item_redirect(request: web.Request):
    query = request.rel_url.query
    if 'id' in query:
        uuid = query['id']
        location = request.app.router['unregistered_item'].url_for(
            name='lifeoxetine', uuid=uuid
        )
        return web.HTTPFound(location)
    else:
        return web.HTTPNotFound()
