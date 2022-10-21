from twilio.rest import Client
import os
import creds

twilio_sid = creds.TWILIO_SID
twilio_token = creds.TWILIO_TOKEN
from_num = creds.FROM_NUM
to_num = creds.TO_NUM

print(twilio_sid)


class NotificationManager:
    def __init__(self):
        self.client = Client(twilio_sid, twilio_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=from_num,
            to=to_num,
        )
        print(message.sid)
