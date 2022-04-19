#! /usr/bin/env python

import requests
from twilio.rest import Client
from typing import TypedDict, Optional


class TwilioConfig(TypedDict):
    sid: Optional[str]
    token: Optional[str]
    sender: Optional[str]
    to: Optional[str]


class WebHooksConfig(TypedDict):
    discord: Optional[str]


class NotificationManager(object):
    WEBHOOKS: WebHooksConfig = None
    twilio: Client = None
    SMS_FROM: str = None
    SMS_TO: str = None

    def __init__(self, twilio_config: TwilioConfig = None, webhooks: WebHooksConfig = None):
        self.WEBHOOKS = webhooks

        if twilio_config is not None and twilio_config['sid'] is not None and twilio_config['token'] is not None:
            self.twilio = Client(twilio_config['sid'], twilio_config['token'])
            self.SMS_TO = twilio_config['to']
            self.SMS_FROM = twilio_config['sender']

    def notify_discord(self, message: str) -> bool:
        if self.WEBHOOKS['discord'] is None:
            return False

        return requests.post(self.WEBHOOKS['discord'], {
            "content": message
        }).status_code == 200

    def notify_sms(self, message: str):
        if self.twilio is None:
            return None

        return self.twilio.messages.create(
            self.SMS_TO,
            body=message,
            from_=self.SMS_FROM,
        )
