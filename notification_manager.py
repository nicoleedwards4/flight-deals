from twilio.rest import Client

twilio_sid = "AC687a5e19a09a890258ee201b09c3dae2"
twilio_token = "097be1f9f3b59fe73e859e4d0c5e73ec"
from_num = "+13466393809"
to_num = "+12535345385"


class NotificationManager:

    def __int__(self):
        self.client = Client(twilio_sid, twilio_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=from_num,
            to=to_num,
        )
        print(message.sid)
