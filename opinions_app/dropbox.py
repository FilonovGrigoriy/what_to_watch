import json

import requests

from . import app


UPLOAD_LINK = 'https://content.dropboxapi.com/2/files/upload'
SHARING_LINK = (
    'https://api.dropboxapi.com/2/'
    'sharing/create_shared_link_with_settings'
)


def get_auth_header():
    return f'Bearer {app.config["DROPBOX_TOKEN"]}'


def upload_files_to_dropbox(images):
    urls = []

    if images is None:
        return urls

    for image in images:
        if not image or not image.filename:
            continue

        dropbox_args = json.dumps({
            'autorename': True,
            'path': f'/{image.filename}',
        })

        upload_response = requests.post(
            UPLOAD_LINK,
            headers={
                'Authorization': get_auth_header(),
                'Content-Type': 'application/octet-stream',
                'Dropbox-API-Arg': dropbox_args,
            },
            data=image.read(),
        )

        upload_data = upload_response.json()

        if 'path_lower' not in upload_data:
            print('DROPBOX UPLOAD STATUS:', upload_response.status_code)
            print('DROPBOX UPLOAD RESPONSE:', upload_response.text)
            raise RuntimeError('Не удалось загрузить файл в Dropbox')

        path = upload_data['path_lower']

        sharing_response = requests.post(
            SHARING_LINK,
            headers={
                'Authorization': get_auth_header(),
                'Content-Type': 'application/json',
            },
            json={'path': path},
        )

        sharing_data = sharing_response.json()

        if 'url' not in sharing_data:
            try:
                sharing_data = (
                    sharing_data['error']
                    ['shared_link_already_exists']
                    ['metadata']
                )
            except KeyError:
                print('DROPBOX SHARING STATUS:', sharing_response.status_code)
                print('DROPBOX SHARING RESPONSE:', sharing_response.text)
                raise RuntimeError('Не удалось создать ссылку Dropbox')

        url = sharing_data['url']
        url = url.replace('dl=0', 'raw=1')
        urls.append(url)

    return urls