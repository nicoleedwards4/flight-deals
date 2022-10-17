import os
from twilio.rest import Client


class NotificationManager:

    def __int__(self):
        self.twilio_sid = "AC687a5e19a09a890258ee201b09c3dae2"
        self.twilio_token = "097be1f9f3b59fe73e859e4d0c5e73ec"
        self.from_num = "+13466393809"
        self.to_num = "+12535345385"
        self.client = Client(self.twilio_sid, self.twilio_token)
        self.body = ""
        self.message = self.client.messages \
            .create(
                body=self.body,
                from_=self.from_num,
                to=self.to_num
                )

    def send_message(self, ):
        print(self.message.sid)
