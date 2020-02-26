# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC4cdfe2590338975f851894a2b21052fa'
auth_token = '60403af9fe6b9d275f154026db08bb15'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+41765974891',
                        from_='+12037936858'
                    )

print(call.sid)