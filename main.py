from flask import Flask, request, jsonify
import random
import requests
import json

app = Flask(__name__)

ACCESS_TOKEN = "f0F+oU0tjJOYCl8uZH6A6rGRpZbQ00Rb2rSqE7a8Jm67oCmvW2b9vcQGdvB677u44kP0Jd05+qQAhpu4PGgouae+1P6kww08Q504o3YkBuUiAaS74YB/UPJiUHGLGimqgySA8Q4Dl5KMqNJnjjcJyAdB04t89/1O/w1cDnyilFU="

LOVE_QUOTES = [
    "你是我主程式裡的唯一參數。",
    "你就像 HTML 裡的 <title>，讓我一眼就知道重點是你。",
    "我不是 try-catch，但我想永遠包住你。",
    "你是我唯一不想 return 的感情。",
    "我寫不出遞迴的愛，但我會一直呼叫你。"
]

@app.route("/")
def home():
    return "Zhenzhen LoveBot 多人模式 💖"

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.get_json()
    print("📥 收到訊息：", json.dumps(body, indent=2, ensure_ascii=False))  # log
    for event in body["events"]:
        if event["type"] == "message":
            msg = event["message"]["text"]
            reply_token = event["replyToken"]
            if "Python" in msg:
                text = "我對你的感情就像 Python 的縮排，一旦對齊，就再也分不開。"
            elif "C++" in msg:
                text = "你不是指標，卻讓我指向你整顆心。"
            elif "JavaScript" in msg:
                text = "你不是 callback，但我總是在你之後才有反應。"
            else:
                text = random.choice(LOVE_QUOTES)
            reply(reply_token, text)
    return jsonify({"status": "ok"})



def reply(token, text):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    body = {
        "replyToken": token,
        "messages": [{
            "type": "text",
            "text": text
        }]
    }
    requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=body)

if __name__ == '__main__':
    app.run(debug=True)
