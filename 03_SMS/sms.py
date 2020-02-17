# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC4cdfe2590338975f851894a2b21052fa'
auth_token = '3a6154a2c5032d69808cb945479364a2'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Hello World',
         from_='+12037936858',
         to='+41793896108'
     )

print(message.sid)