from twilio.rest import Client
import os

twilio_sid = os.environ.get("TWILIO_SID")
twilio_token = os.environ.get("TWILIO_TOKEN")
from_num = "+13466393809"
to_num = "+12535345385"

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
