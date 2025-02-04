from flask import Flask, request

from whatsapp.automatic_response import send_whatsapp_message

app = Flask(__name__)

VERIFY_TOKEN = "Happy"
AUTOMATIC_MESSAGE = "Hello, I am a bot. How can I help you?"

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    print(f'REQUEST: {request.args}')
    if request.method == 'POST':
        data = request.json
        if data.get('entry'):
            try:
                sender = data.get('entry')[-1].get('changes')[-1].get('value').get('messages')[0].get('from') 
                print(f'Received From: {sender}')
                print(f'Responsed With: {AUTOMATIC_MESSAGE}')
                send_whatsapp_message(sender, AUTOMATIC_MESSAGE)
            except:
                print('Not Incoming Message')
        return 'Webhook received successfully', 200
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("Webhook verified successfully!")
        return challenge
    else:
        return "Verification failed", 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

