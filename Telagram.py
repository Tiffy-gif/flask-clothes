import requests
from flask import request

TOKEN = '8038833891:AAG9VYc75O05GOiyOrrKwRp45YIKBereIM0'
def SendMessage(chat_id: str, message: str) -> dict:
    """"
    """
    url = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML',
    }

    r = requests.post(url, data=payload)
    return r.json()
