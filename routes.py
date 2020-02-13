from views import (about_view, artist_view, artists_view, event_view,
                   events_view, index_view, release_view, releases_view)
from pathlib import Path

STATIC_DIR = Path(__file__).parent / 'static'

def setup_routes(app):
    app.router.add_static('/static/', STATIC_DIR, name='static')
    
    app.router.add_get('/', index_view, name='index')
    app.router.add_get('/about', about_view, name='about')

    app.router.add_get('/artists', artists_view, name='artists')
    app.router.add_get('/artists/{route}', artist_view)

    app.router.add_get('/releases', releases_view, name='releases')
    app.router.add_get('/releases/{route}', release_view)

    app.router.add_get('/events', events_view, name='events')
    app.router.add_get('/events/{route}', event_view)

    # app.router.add_get('/items', items_view, name='items')
    # app.router.add_get('/items/{route}', item_view)
    # app.router.add_get('/items/{route}/{id}', item_view)
