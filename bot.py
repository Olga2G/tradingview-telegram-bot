from flask import Flask, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def send_message(text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, data=payload)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    signal = data.get('signal', '').upper()
    pair = data.get('pair', 'N/A')
    price = data.get('price', 'N/A')
    indicator = data.get('indicator', 'N/A')

    if signal == "BUY":
        send_message(f"📈 Сигнал BUY\n🔹 Пара: {pair}\n💵 Ціна: {price}\n📊 Індикатори: {indicator}")
    elif signal == "SELL":
        send_message(f"📉 Сигнал SELL\n🔹 Пара: {pair}\n💵 Ціна: {price}\n📊 Індикатори: {indicator}")
    else:
        send_message(f"⚠️ Незрозумілий сигнал: {signal} для {pair}")

    return '', 200
