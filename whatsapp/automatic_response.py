import requests
import json


with open("credentials.json") as f:
    data = json.load(f)
    ACCESS_TOKEN = data["WHATSAPP_ACCESS_TOKEN"]
    PHONE_NUMBER_ID = data["WHATSAPP_PHONE_NUMBER_ID"]


def send_whatsapp_message(recipient_id, message):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": recipient_id,
        "type": "text",
        "text": {"body": message}
    }
    
    response = requests.post(url, headers=headers, json=payload)
    print(response.json())  # Debug response