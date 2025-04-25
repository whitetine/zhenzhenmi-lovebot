from flask import Flask, request, jsonify
import random
import requests
import json

app = Flask(__name__)

ACCESS_TOKEN = "bvTZoZD3HMh3j42DDVp4NSemu3E+U689U3pnAR2xLVuYpWsLSflX+SoYtY2YBpu24kP0Jd05+qQAhpu4PGgoua e+1P6kww08Q504o3YkBuUpcjR02qdjEU6Evv4f64LIuQABO7o7R1SUPTwcX/I4bAdB04t89/1O/w1cDnyilFU="

LOVE_QUOTES = [
    "你是我主程式裡的唯一參數。",
    "你就像 HTML 裡的 <title>，讓我一眼就知道重點是你。",
    "我不是 try-catch，但我想永遠包住你。",
    "你是我唯一不想 return 的感情。",
    "我寫不出遞迴的愛，但我會一直呼叫你。"
]

@app.route("/")
def home():
    return "Zhenzhen LoveBot 多人撩語模式啟動 💖"

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.get_json()
    print("📥 收到訊息：", json.dumps(body, indent=2, ensure_ascii=False))
    for event in body.get("events", []):
        if event.get("type") == "message":
            msg = event["message"].get("text", "")
            reply_token = event["replyToken"]
            print("📝 使用者說了：", msg)
            if "Python" in msg:
                text = "我對你的感情就像 Python 的縮排，一旦對齊，就再也分不開。"
            elif "C++" in msg:
                text = "你不是指標，卻讓我指向你整顆心。"
            elif "JavaScript" in msg:
                text = "你不是 callback，但我總是在你之後才有反應。"
            elif "SQL" in msg:
                text = "你不是查詢語句，但你一出現我整個世界都 join 起來了。"
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
