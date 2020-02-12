from views import (about_view, artist_view, artists_view, event_view,
                   events_view, index_view, release_view, releases_view)


def setup_routes(app):
    app.router.add_get('/', index_view, 'index')
    app.router.add_get('/about', about_view, 'about')

    app.router.add_get('/artists', artists_view, 'artists')
    app.router.add_get('/artists/{route}', artist_view)

    app.router.add_get('/releases', releases_view, 'releases')
    app.router.add_get('/releases/{route}', release_view)

    app.router.add_get('/events', events_view, 'events')
    app.router.add_get('/events/{route}', event_view)
