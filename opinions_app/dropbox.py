import asyncio
import json

import aiohttp

from . import app


UPLOAD_LINK = 'https://content.dropboxapi.com/2/files/upload'
SHARING_LINK = (
    'https://api.dropboxapi.com/2/'
    'sharing/create_shared_link_with_settings'
)


def get_auth_header():
    return f'Bearer {app.config["DROPBOX_TOKEN"]}'


async def async_upload_files_to_dropbox(images):
    urls = []

    if images is None:
        return urls

    async with aiohttp.ClientSession() as session:
        tasks = []

        for image in images:
            if not image or not image.filename:
                continue

            tasks.append(
                asyncio.ensure_future(
                    upload_file_and_get_url(session, image)
                )
            )

        if tasks:
            urls = await asyncio.gather(*tasks)

    return urls


async def upload_file_and_get_url(session, image):
    dropbox_args = json.dumps({
        'autorename': True,
        'mode': 'add',
        'path': f'/{image.filename}',
    })

    async with session.post(
        UPLOAD_LINK,
        headers={
            'Authorization': get_auth_header(),
            'Content-Type': 'application/octet-stream',
            'Dropbox-API-Arg': dropbox_args,
        },
        data=image.read(),
    ) as response:
        data = await response.json()

        if 'path_lower' not in data:
            print('DROPBOX UPLOAD STATUS:', response.status)
            print('DROPBOX UPLOAD RESPONSE:', data)
            raise RuntimeError('Не удалось загрузить файл в Dropbox')

        path = data['path_lower']

    async with session.post(
        SHARING_LINK,
        headers={
            'Authorization': get_auth_header(),
            'Content-Type': 'application/json',
        },
        json={'path': path},
    ) as response:
        data = await response.json()

        if 'url' not in data:
            try:
                data = (
                    data['error']
                    ['shared_link_already_exists']
                    ['metadata']
                )
            except KeyError:
                print('DROPBOX SHARING STATUS:', response.status)
                print('DROPBOX SHARING RESPONSE:', data)
                raise RuntimeError('Не удалось создать ссылку Dropbox')

        url = data['url']
        url = url.replace('dl=0', 'raw=1')

    return url