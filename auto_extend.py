import datetime
import random
import subprocess

# 👉 1. 準備要新增的指令與內容
new_commands = [
    ('/晚安', '晚安寶貝，夢裡也是我 💫'),
    ('/早安', '早安小可愛，今天也是愛你的一天 ☀️'),
    ('/SQL', '你不是查詢語句，但你一出現我整個世界都 join 起來了。'),
    ('/C', '你的存在比 C 語言的指標還重要 💘')
]

# 👉 2. 選一個沒加過的新指令
command, response = random.choice(new_commands)

# 👉 3. 修改 main.py，把新的 if 判斷插進去
with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

insert_line = -1
for i, line in enumerate(lines):
    if "else:" in line:  # 找到 else: 前一行插入
        insert_line = i
        break

if insert_line != -1:
    new_code = f"""            elif "{command}" in msg:\n                text = "{response}"\n"""
    lines.insert(insert_line, new_code)

    with open("main.py", "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"✅ 已新增指令 {command}：{response}")
else:
    print("❌ 沒有找到插入點，請確認 main.py 結構")

# 👉 4. 自動 Git commit + push
today = datetime.date.today().isoformat()
commit_message = f"Add {command} 自動生成指令 {today}"

subprocess.run(["git", "add", "main.py"])
subprocess.run(["git", "commit", "-m", commit_message])
subprocess.run(["git", "push", "origin", "main"])
