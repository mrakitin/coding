# -*- coding: utf-8 -*-
import json
import os
import re

import requests
from lxml import html

_STATIC_DIR = 'static'
_JSON_DIR = 'json'
_CONFIG_BASENAME = 'config.json'
_CONFIG_FILE = os.path.join(_STATIC_DIR, _JSON_DIR, _CONFIG_BASENAME)

# Initialize the variables. They will be populated from config file.
DOWNLOAD_URL = None
FILE_EXTENSION = None
FILE_DOWNLOAD_FIELD = None
FILE_TITLE_FIELD = None

TIMEOUT = 60
NUM_OF_ATTEMPTS = 10

with open(_CONFIG_FILE, 'r') as f:
    data = json.load(f)

for key in data.keys():
    globals()[key] = data[key]


def get_files_list(url=DOWNLOAD_URL, name=''):
    files_list = []
    raw_files_list = []

    r = requests.get('{}/{}'.format(url, name))
    content = r.text.split('\n')

    for i in range(len(content)):
        if re.search(name.split()[0].lower(), content[i].lower()) and \
                re.search('.{}'.format(FILE_EXTENSION), content[i].lower()):
            raw_files_list.append(content[i])

    for i in range(len(raw_files_list)):
        tree = html.fromstring(raw_files_list[i])
        file_prop = dict(tree.attrib)
        if FILE_DOWNLOAD_FIELD in file_prop and FILE_TITLE_FIELD in file_prop:
            files_list.append((file_prop[FILE_DOWNLOAD_FIELD], file_prop[FILE_TITLE_FIELD]))

    return files_list


def download_file(url, name, save_dir=''):
    file_name = os.path.join(save_dir, name)

    def _get():
        r = requests.get(
            url,
            timeout=TIMEOUT,
            allow_redirects=True
        )
        content = r.content
        file_size = len(content)
        status = r.status_code
        return content, file_size, status

    content, file_size, status = _get()
    for i in range(NUM_OF_ATTEMPTS):
        if file_size == 0:
            print('      File size: {} ==> Download attempt #{}...'.format(file_size, i + 1))
            content, file_size, status = _get()
        else:
            break

    if file_size > 0:
        with open(file_name, 'wb') as f:
            f.write(content)
    else:
        file_name = 'None'

    return file_name, file_size, status


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Find list of files.')
    parser.add_argument('-n', '--name', dest='name', help='name of the file to search.')
    parser.add_argument('-s', '--save-dir', dest='save_dir', help='dir to save the files.')

    args = parser.parse_args()
    name = args.name.lower()
    save_dir = args.save_dir
    if not save_dir:
        save_dir = '{}_{}'.format(FILE_EXTENSION, name.replace(' ', '_'))
        if not os.path.isdir(save_dir):
            os.mkdir(save_dir)

    files_list = get_files_list(DOWNLOAD_URL, name)
    cut = 100
    print('Number of files: {}'.format(len(files_list)))
    for i in range(len(files_list)):
        try:
            print('  #{:>3} - {:100} - {:100}'.format(
                i + 1,
                files_list[i][0][:cut],
                files_list[i][1][:cut]
            ))
            file_name, file_size, status = download_file(
                url=files_list[i][0],
                name='{:03d}_{}.{}'.format(i + 1, files_list[i][1], FILE_EXTENSION),
                save_dir=save_dir
            )
            print('    File <{}> ({:.2f} KB, status {})'.format(
                file_name,
                float(file_size) / (1024 ** 1),
                status
            ))
        except Exception as e:
            print('    File {} cannot be downloaded.'.format(files_list[i][0]))
