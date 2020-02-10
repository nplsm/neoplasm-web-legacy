import weakref
from dataclasses import dataclass
from datetime import date, timedelta
from operator import itemgetter
from typing import Dict, List


@dataclass
class Link:
    name: str
    href: str


@dataclass
class Artist:
    name: str
    route: str
    links: List[Link]


@dataclass
class Track:
    name: str
    length: timedelta


@dataclass
class Release:
    name: str
    route: str
    artist: Artist
    release_date: date
    tralist: List[Track]
    links: List[Link]


PerfectHuman = Artist(
    'Perfect Human', '/perfect-human',
    [
        Link('vk', '#'),
        Link('fb', '#'),
        Link('tg', '#'),
        Link('bc', '#'),
        Link('sc', '#'),
    ]
)

MarbleBust = Artist(
    'Marble Bust', '/marble-bust',
    [
        Link('vk', '#'),
        Link('fb', '#'),
        Link('tg', '#'),
        Link('bc', '#'),
        Link('sc', '#'),
    ]
)

OurV = Artist(
    'Our.V', '/our-v',
    [
        Link('vk', '#'),
        Link('fb', '#'),
        Link('tg', '#'),
        Link('bc', '#'),
        Link('sc', '#'),
    ]
)

Omega = Release(
    'Omega', '/omega', PerfectHuman, date(2019, 9, 10),
    [
        Track('Omega (feat. Marble Bust)', timedelta(minutes=3, seconds=42))
    ],
    [
        Link('am', '#'),
        Link('sp', '#'),
        Link('vk', '#'),
        Link('bc', '#'),
        Link('sc', '#'),
    ]
)

Lifeoxetine = Release(
    'Lifeoxetine', '/lifeoxetine', MarbleBust, date(2019, 11, 4),
    [
        Track('THENEWERA', timedelta(minutes=3, seconds=4)),
        Track('TRANSGRESSION (feat. Увула)', timedelta(minutes=2, seconds=20)),
        Track('ANGELS', timedelta(minutes=3, seconds=55)),
        Track('HINDSIGHT', timedelta(minutes=3, seconds=4)),
        Track('SORRYAU', timedelta(minutes=3, seconds=42)),
        Track('TRANCEGRESSION', timedelta(minutes=2, seconds=33)),
        Track('THELIFTINGHAND', timedelta(minutes=6, seconds=31)),
    ],
    [
        Link('am', '#'),
        Link('sp', '#'),
        Link('vk', '#'),
        Link('bc', '#'),
        Link('sc', '#'),
    ]
)

AUK = Release(
    'A U K', '/a-u-k', OurV, date(2019, 9, 10),
    [
        Track('Wait for me here, I\'ll be right there',timedelta(minutes=2, seconds=14)),
        Track('Backstage', timedelta(minutes=3, seconds=46)),
        Track('A U 0K& What\'s wrong with you...', timedelta(minutes=4, seconds=20)),
        Track('Healthy Sleep', timedelta(minutes=3, seconds=40)),
        Track('Ice Cream ft. Jessie', timedelta(minutes=3, seconds=42)),
        Track('TRANCEGRESSION', timedelta(minutes=2, seconds=33)),
        Track('THELIFTINGHAND', timedelta(minutes=6, seconds=31)),
    ],
    [
        Link('am', '#'),
        Link('sp', '#'),
        Link('vk', '#'),
        Link('bc', '#'),
        Link('sc', '#'),
    ]
)

auk_tracklist = [
    {'name': 'Wait for me here, I\'ll be right there',
        'lenght': },
    {'name': 'Backstage', 'lenght': },
    {'name': ' ',
        'lenght': },
    {'name': '', 'lenght': },
    {'name': 'Ice Cream ft. Jessie',
        'lenght': timedelta(minutes=3, seconds=9)},
    {'name': 'League', 'lenght': timedelta(minutes=1, seconds=57)},
    {'name': 'Do not leave me', 'lenght': timedelta(minutes=1, seconds=25)},
    {'name': 'Justified Misunderstanding',
        'lenght': timedelta(minutes=2, seconds=40)},
    {'name': 'Soft Forms', 'lenght': timedelta(minutes=4, seconds=5)},
    {'name': 'Invenire Tentant', 'lenght': timedelta(minutes=1, seconds=25)},
]

auk_release = {
    'name': 'A U K',
    'route': '/a-u-k',
    'artist': ourv_artist,
    'tracklist': auk_tracklist,
    'links': auk_links,
    'release_date': date(2020, 2, 11),
}

artists = [marblebust_artist, perfecthuman_artist, ourv_artist]
releases = [lifeoxetine_release, omega_release, auk_release]

artists.sort(key=itemgetter('name'))
releases.sort(key=itemgetter('release_date'))
