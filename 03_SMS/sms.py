import os
from twillo.rest import Client

Account_sid = os.environ["AC4cdfe2590338975f851894a2b21052fa"]
auth_token = os.environ["3a6154a2c5032d69808cb945479364a2"]

client = Client(Account_sid, auth_token)

client.messages.create(
    to=os.environ["+41765974891"],
    from_="+12037936858",
    body="Hallo Welt"
)