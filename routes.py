from views import (about_view, artist_view, artists_view, event_view,
                   events_view, id_item_view, index_view, item_view,
                   items_view, legacy_lifeoxetine_item_redirect, release_view,
                   releases_view)


def setup_routes(app):
    app.router.add_get('/', index_view, name='index')
    app.router.add_get('/about', about_view, name='about')

    app.router.add_get('/artists', artists_view, name='artists')
    app.router.add_get('/artists/{route}', artist_view, name='artist')

    app.router.add_get('/releases', releases_view, name='releases')
    app.router.add_get('/releases/{route}', release_view, name='release')

    app.router.add_get('/events', events_view, name='events')
    app.router.add_get('/events/{route}', event_view, name='event')

    app.router.add_get('/items', items_view, name='items')
    app.router.add_get('/items/{route}', item_view, name='item')
    app.router.add_get('/items/{route}/{id}', id_item_view, name='id_item')
    app.router.add_get('/npl0002', legacy_lifeoxetine_item_redirect,
                       name='legacy_lifeoxetine_id_item')
