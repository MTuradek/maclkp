#!/usr/bin/env python3

import requests, sys
from os import environ


url = 'https://api.macaddress.io/v1?output=json&search='


def get_env():
    if len(sys.argv) < 2:
        sys.exit(f'usage: {sys.argv[0]} <MAC address>')
    else:
        return sys.argv[1]


def get_token():
    if environ.get('TOKEN') is None:
        sys.exit('No API token available in ENV')
    else:
        return environ.get('TOKEN')


def main():
    mac = get_env()
    token = get_token()
    try:
        resp = requests.get(f'{url}{mac}', headers = {'X-Authentication-Token': token})
        print(f"{mac}: {resp.json()['vendorDetails']['companyName']}")
    except:
        print(f'Something went wrong {resp.status_code}')


if __name__ == '__main__':
    main()

