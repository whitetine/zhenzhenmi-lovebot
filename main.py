from flask import Flask, request, jsonify
import random
import requests
import json

app = Flask(__name__)

ACCESS_TOKEN = "f0F+oU0tjJOYCl8uZH6A6rGRpZbQ00Rb2rSqE7a8Jm67oCmvW2b9vcQGdvB677u44kP0Jd05+qQAhpu4PGgouae+1P6kww08Q504o3YkBuUiAaS74YB/UPJiUHGLGimqgySA8Q4Dl5KMqNJnjjcJyAdB04t89/1O/w1cDnyilFU="

LOVE_QUOTES = [
    "你是我的 primary key，沒有你我就無法連接任何關係。",
    "你像 Git 一樣掌控我的版本，我的心只想 commit 給你。",
    "你不是 HTML，但我一眼就被你的 <body> 吸引。",
    "愛你就像寫 while(true)，永無止盡。",
    "你是我 try 過最不想 catch 的人。",
    "你的笑讓我心跳像 thread 一樣 race condition。"
]

@app.route("/")
def home():
    return "Zhenzhen LoveBot 多人模式 💖"

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.get_json()
    print("接收到事件：", json.dumps(body, indent=2))

    for event in body["events"]:
        if event["type"] == "message":
            user_id = event["source"]["userId"]
            reply_token = event["replyToken"]
            send_reply(reply_token, random.choice(LOVE_QUOTES))

    return jsonify({"status": "ok"})

def send_reply(reply_token, text):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    body = {
        "replyToken": reply_token,
        "messages": [{
            "type": "text",
            "text": text
        }]
    }
    requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=body)

if __name__ == '__main__':
    app.run(debug=True)
