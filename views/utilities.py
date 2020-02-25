from pathlib import Path

import aiohttp_jinja2
import markdown2
import ujson
from aiohttp import web


def load_meta(TARGET_DIR: Path) -> dict:
    META_PATH = TARGET_DIR / 'meta.json'
    DESCRIPTION_PATH = TARGET_DIR / 'description.md'
    IMAGE_PATH = '/' / TARGET_DIR / 'image.jpg'
    LINK = TARGET_DIR.parts[-1]

    with open(str(META_PATH)) as json_file:
        meta = ujson.load(json_file)
    description = markdown2.markdown_path(DESCRIPTION_PATH)

    meta['description'] = description
    meta['image_path'] = str(IMAGE_PATH)
    meta['link'] = LINK

    return meta
