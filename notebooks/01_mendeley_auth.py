from flask import Flask, request
import requests
import webbrowser
import urllib.parse

CLIENT_ID = "21483"
CLIENT_SECRET = "n3cjVHdeWVvPttvO"


REDIRECT_URI = "http://localhost:8080/callback"
AUTH_URL = "https://api.mendeley.com/oauth/authorize"
TOKEN_URL = "https://api.mendeley.com/oauth/token"

app = Flask(__name__)

@app.route("/")
def home():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": "all"
    }
    url = AUTH_URL + "?" + urllib.parse.urlencode(params)
    webbrowser.open(url)
    return "Opening browser for Mendeley login..."

@app.route("/callback")
def callback():
    code = request.args.get("code")
    print("Authorization code:", code)

    # Exchange the code for a token
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI
    }

    r = requests.post(
        TOKEN_URL,
        data=data,
        auth=(CLIENT_ID, CLIENT_SECRET)
    )
    print("\nToken response:")
    print(r.json())
    return "Token printed in console. You can close this window."

if __name__ == "__main__":
    print("Go to: http://localhost:8080")
    app.run(port=8080)