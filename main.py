
from flask import Flask, request, jsonify
import random
import requests

app = Flask(__name__)

ACCESS_TOKEN = "你的 Channel Access Token"
USER_ID = "acesking.tw"  # 或使用者 LINE ID

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
    return "Zhenzhen LoveBot 運作中 💖"

@app.route("/push", methods=["GET"])
def push():
    headers = {
        "Authorization": f"Bearer {f0F+oU0tjJOYCl8uZH6A6rGRpZbQ00Rb2rSqE7a8Jm67oCmvW2b9vcQGdvB677u44kP0Jd05+qQAhpu4PGgouae+1P6kww08Q504o3YkBuUiAaS74YB/UPJiUHGLGimqgySA8Q4Dl5KMqNJnjjcJyAdB04t89/1O/w1cDnyilFU=}",
        "Content-Type": "application/json"
    }
    data = {
        "to": USER_ID,
        "messages": [
            {
                "type": "text",
                "text": random.choice(LOVE_QUOTES)
            }
        ]
    }
    r = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=data)
    return jsonify({"status": r.status_code})

if __name__ == '__main__':
    app.run(debug=True)
