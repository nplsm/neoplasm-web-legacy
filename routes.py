from views.artists import artist, artists, auk_release_vk_redirect
from views.events import event, events
from views.general import about, index
from views.items import (get_file, item, items,
                         legacy_lifeoxetine_item_redirect, registration)
from views.releases import release, releases


def setup_routes(app):
    app.router.add_static('/public', 'public')

    app.router.add_get('/', index, name='index')
    app.router.add_get('/about', about, name='about')

    app.router.add_get('/artists', artists, name='artists')
    app.router.add_get('/artists/{artist}', artist, name='artist')

    app.router.add_get('/releases', releases, name='releases')
    app.router.add_get('/releases/{release}', release, name='release')

    app.router.add_get('/events', events, name='events')
    app.router.add_get('/events/{event}', event, name='event')

    app.router.add_get('/items', items, name='items')
    app.router.add_get('/items/{item}', item, name='item')

    app.router.add_get(
        r'/items/{item}/{uuid:\b[0-9a-fA-F]{32}\b}',
        registration, name='unregistered_item'
    )

    app.router.add_get(
        r'/items/{item}/{uuid:\b[0-9a-fA-F]{32}\b}/{filename}',
        get_file, name='get_file'
    )

    # app.router.add_get(
    #     r'/items/{item}/{number:\d+}',
    #     page, name='registered_item'
    # )

    app.router.add_get(
        '/npl0002',
        legacy_lifeoxetine_item_redirect, name='legacy_lifeoxetine_id_item'
    )

    app.router.add_get(
        '/a-u-k', 
        auk_release_vk_redirect, name='auk_release_vk_redirect'
    )