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
        'attachments': payload['attachments']
    }))

    return self.event


def create_payload():
    attachment = {
        "fallback": "トークン配布通知",

        "text": "トークン配布結果",
        "pretext": "",

        "color": "#36a64f",

        "fields": [
            {
                "title": ":alis: トークン配布が完了しました :alis:",
                "value":
                    "配布記事数: "
                    + "`\n 配布ユーザ数(いいね): ",
                "short": False
            }
        ]
    }

    payload = {
        'attachments': [attachment]
    }

    return payload
