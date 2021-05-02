#!/usr/bin/env python
# coding: utf-8
import sys
import logging
import config
import json
if sys.version_info[0] >= 3:
    import urllib.request as urllib
else:
    import urllib

env = 'prod'
config = config.get_config()[env]

region = config['aws']['region']
userpool_id = config['aws']['cognitio']['userPoolId']
app_client_id = config['aws']['cognitio']['userPoolClientId']
keys_url = 'https://cognito-idp.{}.amazonaws.com/{}/.well-known/jwks.json'.format(region, userpool_id)

def get_keys():
    response = urllib.urlopen(keys_url)
    return json.loads(response.read())['keys']
