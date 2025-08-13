import os
import requests
from dotenv import load_dotenv

load_dotenv()

INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
INSTANCE_TOKEN = os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

def enviar_mensagem(telefone: str, mensagem: str):
    url = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{INSTANCE_TOKEN}/send-text"
    headers = {
        "Client-Token": CLIENT_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {"phone": telefone, "message": mensagem}
    r = requests.post(url, headers=headers, json=payload)
    return r.status_code, r.text

