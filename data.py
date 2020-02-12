from datetime import date, timedelta
from operator import itemgetter
from pathlib import Path

import markdown2

THIS_DIR = Path(__file__).parent

MARKDOWN_DIR = THIS_DIR / 'markdown'
IMAGES_DIR = THIS_DIR / 'static' / 'images'

# Artists' links
perfecthuman_links = [
    {'name': 'Facebook', 'href': 'https://www.facebook.com/perfecthumanmusic/'},
    {'name': 'VK', 'href': 'https://vk.com/perfect.human'},
    {'name': 'Telegram', 'href': 'https://tele.click/perfect_human'},
    {'name': 'Bandcamp', 'href': 'http://perfecthuman.bandcamp.com'},
    # {'name': 'Soundcloud', 'href': '#'},
]

marblebust_links = [
    {'name': 'Facebook', 'href': 'https://www.facebook.com/marb1ebust'},
    {'name': 'VK', 'href': 'https://vk.com/marblebust'},
    {'name': 'Telegram', 'href': 'https://t.me/lovvlife'},
    {'name': 'Bandcamp', 'href': 'https://lovvlifer.bandcamp.com'},
    {'name': 'Soundcloud', 'href': 'https://soundcloud.com/djmarblebust'},
]

ourv_links = [
    # {'name': 'Facebook', 'href': '#'},
    {'name': 'VK', 'href': 'https://vk.com/our__v'},
    # {'name': 'Telegram', 'href': '#'},
    {'name': 'Bandcamp', 'href': 'https://ourdotv.bandcamp.com'},
    {'name': 'Soundcloud', 'href': 'https://soundcloud.com/our_v'},
]

# Releases' links
omega_links = [
    {'name': 'Apple Music',
        'href': 'https://music.apple.com/us/album/omega-feat-marble-bust-single/1497301767'},
    {'name': 'Boom', 'href': 'https://vk.cc/ajbQyb'},
    {'name': 'Spotify', 'href': 'https://open.spotify.com/album/11IfzV6wZxLslVsq2uh4gk?si=CXAho1f4QNCspqS22ZLguQ'},
    {'name': 'Bandcamp', 'href': 'https://perfecthuman.bandcamp.com/track/omega'},
    {'name': 'Soundcloud', 'href': 'https://soundcloud.com/ne-sm/omega'},
    {'name': 'Deezer', 'href': 'https://www.deezer.com/us/album/129654552'},
    {'name': 'YouTube Music',
        'href': 'https://music.youtube.com/playlist?list=OLAK5uy_nUO6DeeL51H6bl7P-HiIPoGOfsjYHfM5E'},
    {'name': 'Yandex Music', 'href': 'https://music.yandex.ru/artist/6740953'},
    {'name': 'Pandora', 'href': 'https://pandora.app.link/mkJ9E1SEZ3'},
    {'name': 'Google Play', 'href': 'https://play.google.com/store/music/album/Perfect_Human_Feat_Marble_Bust_Omega?id=Bowi6dy74doa3ghw3gqb225dlci'},
]

lifeoxetine_links = [
    # {'name': 'Apple Music', 'href': '#'},
    # {'name': 'Boom', 'href': '#'},
    # {'name': 'Spotify', 'href': '#'},
    # {'name': 'Bandcamp', 'href': '#'},
    # {'name': 'Soundcloud', 'href': '#'},
]

auk_links = [
    {'name': 'Apple Music', 'href': 'https://music.apple.com/ru/album/a-u-k/1498059256?l=en'},
    {'name': 'Boom', 'href': 'https://vk.cc/akEskF'},
    # {'name': 'Spotify', 'href': '#'},
    {'name': 'Bandcamp', 'href': 'https://ourdotv.bandcamp.com/album/a-u-k'},
    {'name': 'Soundcloud', 'href': 'https://soundcloud.com/ne-sm/sets/a-u-k'},
    {'name': 'Deezer', 'href': 'https://www.deezer.com/us/album/130533372'},
    # {'name': 'YouTube Music', 'href': ''},
    {'name': 'Yandex Music', 'href': 'https://music.yandex.ru/artist/5480823'},
    # {'name': 'Pandora', 'href': ''},
    {'name': 'Google Play', 'href': 'https://play.google.com/store/music/album/Our_v_A_U_K?id=Bllz54kie7ybyr5vodvomcwumy4'},
]

# Events' links
eartheater2019_links = [
    # {'name': 'Facebook', 'href': '#'},
    # {'name': 'VK', 'href': '#'},
]

hdmirror2020_links = [
    {'name': 'Resident Advisor', 'href': 'https://www.residentadvisor.net/events/1380297'},
    {'name': 'Facebook', 'href': 'https://www.facebook.com/events/637503077020666/'},
    {'name': 'VK', 'href': 'https://vk.com/hdmirrorneoplasm'},
]

# Artists
perfecthuman_artist = {
    'name': 'Perfect Human',
    'route': 'perfect-human',
    'links': perfecthuman_links,
    'image': '/images/perfect-human/perfect-human_image.jpg'
}

marblebust_artist = {
    'name': 'Marble Bust',
    'route': 'marble-bust',
    'links': marblebust_links,
    'image': 'images/marble-bust/marble-bust_image.jpg'
}

ourv_artist = {
    'name': 'Our.V',
    'route': 'our-v',
    'links': ourv_links,
    'image': '/images/our-v/our-v_image.jpg',
}

# Releases

# Releases' tracklists

omega_tracklist = [
    {'name': 'Omega (feat. Marble Bust)',
     'length': timedelta(minutes=3, seconds=42)},
]

lifeoxetine_tracklist = [
    {'name': 'THENEWERA', 'length': timedelta(minutes=3, seconds=4)},
    {'name': 'TRANSGRESSION (feat. Увула)',
     'length': timedelta(minutes=2, seconds=20)},
    {'name': 'ANGELS', 'length': timedelta(minutes=3, seconds=55)},
    {'name': 'HINDSIGHT', 'featured': 'Sparrow',
        'length': timedelta(minutes=3, seconds=4)},
    {'name': 'SORRYAU', 'length': timedelta(minutes=3, seconds=42)},
    {'name': 'TRANCEGRESSION', 'length': timedelta(minutes=3, seconds=42)},
    {'name': 'SORRYAU', 'length': timedelta(minutes=2, seconds=33)},
    {'name': 'THELIFTINGHAND', 'length': timedelta(minutes=6, seconds=31)},
]

auk_tracklist = [
    {'name': 'Wait for me here, I\'ll be right there',
        'length': timedelta(minutes=2, seconds=14)},
    {'name': 'Backstage', 'length': timedelta(minutes=3, seconds=46)},
    {'name': 'Ice Cream (feat. Jessie)',
        'length': timedelta(minutes=3, seconds=9)},
    {'name': 'League', 'length': timedelta(minutes=1, seconds=57)},
    {'name': 'Do not leave me', 'length': timedelta(minutes=1, seconds=25)},
    {'name': 'Justified Misunderstanding',
        'length': timedelta(minutes=2, seconds=40)},
    {'name': 'Soft Forms', 'length': timedelta(minutes=4, seconds=5)},
    {'name': 'Invenire Tentant', 'length': timedelta(minutes=1, seconds=25)},
    {'name': 'A U 0K& What\'s wrong with you... ',
        'length': timedelta(minutes=4, seconds=20)},
]

# Releases
omega_release = {
    'name': 'Omega',
    'route': 'omega',
    'artist': perfecthuman_artist,
    'tracklist': omega_tracklist,
    'links': omega_links,
    'release_date': date(2019, 9, 10),
    'cover': '/images/omega/omega_cover.jpeg',
}

lifeoxetine_release = {
    'name': 'Lifeoxetine',
    'route': 'lifeoxetine',
    'artist': marblebust_artist,
    'tracklist': lifeoxetine_tracklist,
    'links': lifeoxetine_links,
    'release_date': date(2019, 11, 4),
    'cover': '/images/lifeoxetine/lifeoxetine_cover.jpeg',
}

auk_release = {
    'name': 'A\u00A0U\u00A0K',
    'route': 'a-u-k',
    'artist': ourv_artist,
    'tracklist': auk_tracklist,
    'links': auk_links,
    'release_date': date(2020, 2, 11),
    'cover': '/images/a-u-k/a-u-k_cover.jpg',
}

# Events

# Events' locations
live8club_location = {
    'name': 'Live8Club',
    'city': 'Moscow',
    'href': 'https://vk.com/live8club',
}

# Events
eartheater2019_event = {
    'name': 'Eartheater x NEOPLASM',
    'route': 'eartheater2019',
    'soldout': True,
    'past': True,
    'date': date(2019, 11, 8),
    'tickets_href': 'https://neoplasm.timepad.ru/event/1096795/',
    'location': live8club_location,
    'links': eartheater2019_links,
    'poster': '/images/eartheater2019/eartheater2019_poster.jpg',
    'lineup': [
        'Eartheater (USA) Live',
        'Marble Bust Live',
        'Lovozero',
        'Lisa Smirnova',
        'p3rf x',
        'ALEXA1312',
        'Rouborgen',
    ],
}

hdmirror2020_event = {
    'name': 'HDMIRROR x NEOPLASM',
    'route': 'hdmirror2020',
    'soldout': False,
    'past': False,
    'date': date(2020, 2, 29),
    'tickets_href': 'https://neoplasm.timepad.ru/event/1235549/',
    'location': live8club_location,
    'links': hdmirror2020_links,
    'poster': '/images/hdmirror2020/hdmirror2020_poster.jpg',
    'lineup': [
        'HDMIRROR (Berlin/Cape Town)',
        'Our.v',
        'p3rf x',
        'ALEXA1312',
        'ducttape',
    ],
}


artists_list = [marblebust_artist, perfecthuman_artist, ourv_artist, ]
releases_list = [lifeoxetine_release, omega_release, auk_release, ]
events_list = [eartheater2019_event, hdmirror2020_event, ] 

for release in releases_list:
    route = release['route']
    release['description'] = markdown2.markdown_path(
        f'./markdown/{route}_description.md')

    tracklist = release['tracklist']
    total_lenght = timedelta(0)

    for track in tracklist:
        length = track['length']
        total_lenght += length
        minutes = str(length).split(':')[1]
        seconds = str(length).split(':')[2]
        track['lenght_string'] = ':'.join([minutes, seconds])
        minutes_int = int(minutes)
        seconds_int = int(seconds)
        track['lenght_string_html'] = f'PTM{str(minutes_int)}S{str(seconds_int)}'

    total_lenght_minutes = str(total_lenght).split(':')[1]
    total_lenght_seconds = str(total_lenght).split(':')[2]
    release['total_lenght'] = ':'.join(
        [total_lenght_minutes, total_lenght_seconds])
    total_lenght_minutes_int = int(total_lenght_minutes)
    total_lenght_seconds_int = int(total_lenght_seconds)
    track['total_lenght_html'] = f'PTM{str(total_lenght_minutes_int)}S{str(total_lenght_seconds_int)}'

for artist in artists_list:
    route = artist['route']
    artist['description'] = markdown2.markdown_path(
        f'./markdown/{route}_description.md')

for event in events_list:
    route = event['route']
    event['description'] = markdown2.markdown_path(
        f'./markdown/{route}_description.md')

about = markdown2.markdown_path(f'./markdown/about.md')

artists_list.sort(key=itemgetter('name'))
releases_list.sort(key=itemgetter('release_date'), reverse=True)
events_list.sort(key=itemgetter('date'), reverse=True)
