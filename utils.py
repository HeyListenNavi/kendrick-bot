import time 
import base64
import json
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

def update_token(start_time):
    current_time = time.time()

    if current_time - start_time >= 3600:
        url = "https://accounts.spotify.com/api/token"

        client_id = config["CLIENT_ID"]
        client_secret = config["CLIENT_SECRET"]
        authorization_keys = base64.b64encode(bytes(f"{client_id}:{client_secret}", "utf-8")).decode()

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {authorization_keys}",
        }
        payload = {
            "grant_type": "client_credentials"
        }

        response = requests.post(url, data=payload, headers=headers)

        auth_token = response.json()["access_token"]
        return auth_token