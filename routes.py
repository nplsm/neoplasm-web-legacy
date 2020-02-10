from views import *


def setup_routes(app):
    app.router.add_get('/', artists_view)

    app.router.add_get('/artists', artists_view)

    app.router.add_get('/perfect-human', perfecthuman_view)
    app.router.add_get('/marble-bust', marblebust_view)
    app.router.add_get('/our-v', ourv_view)

    app.router.add_get('/releases', releases_view)

    app.router.add_get('/omega', omega_view)
    app.router.add_get('/lifeoxetine', lifeoxetine_view)
    app.router.add_get('/a-u-k', auk_view)

    app.router.add_get('/events', events_view)

    app.router.add_get('/2019/eartheater', eartheater2019_view)
    app.router.add_get('/2020/hdmirror', hdmirror2020_view)

    app.router.add_get('/about', about_view)
