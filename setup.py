import requests

TOKEN = '1228052546:AAHijJi0TFuUJ-csaPU459-XNT3KY_fk28A'
API_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
requests_payload = {
    'chat_id': 380314062, #dfddfdfdfdfdfdfdf
    'text': 'Hello',
    'reply_to_message_id': 4
}

r = requests.get(API_URL, data=requests_payload)
print(r.json())
