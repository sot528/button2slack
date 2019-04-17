import os
import json
import logging
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    payload = create_payload()

    requests.post(os.environ['SLACK_NOTIFICATION_URL'], data=json.dumps({
        'username': payload['username'] if 'username' in payload is None else u'alis',
        'icon_emoji': payload['icon_emoji'] if 'icon_emoji' in payload is None else u':alischan:',
        'link_names': 1,  # メンションを有効にする
        'text': os.environ['MESSAGE']
    }))

    return True


def create_payload():
    payload = {}

    return payload
