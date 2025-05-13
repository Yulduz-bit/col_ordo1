import requests

TELEGRAM_BOT_TOKEN = '7839999416:AAHSW97FQtDLMjsIBbBzrMPwUj4XMXfe_hc'  # ← Вставь свой токен
TELEGRAM_CHAT_ID = '5722653765'  # ← Вставь свой Telegram user ID

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML',
    }
    response = requests.post(url, data=data)
    return response.json()
