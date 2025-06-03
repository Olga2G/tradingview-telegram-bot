from flask import Flask, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

def send_message(text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, data=payload)
@app.route('/', methods=['GET'])
def index():
    return 'Bot is running', 200

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
