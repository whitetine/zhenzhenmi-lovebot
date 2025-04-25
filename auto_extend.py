import datetime
import random
import subprocess

撩語庫 = [('React', '你的出現就像 React 的 useEffect，我的心跳總是跟著你更新。'), ('Git', '你不是 commit，但我只想把我的心 push 給你。'), ('HTML', '你就像 HTML 裡的 <title>，我的世界一開始就為你命名。'), ('CSS', '你的美，是我寫不出來的 style。'), ('Java', '你不是 JVM，卻總讓我感覺一切都 run 得很穩。'), ('Go', '我不是 Golang，但我只想跟你一起 goroutine。'), ('Rust', '你是我人生的 ownership，不能 move 也不能 clone。')]

command, response = random.choice(撩語庫)

with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

insert_line = -1
for i, line in enumerate(lines):
    if "else:" in line:
        insert_line = i
        break

if insert_line != -1:
    new_code = f'''            elif "{command}" in msg:\n                text = "{response}"\n'''
    lines.insert(insert_line, new_code)

    with open("main.py", "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"✅ 已新增指令 {command}：{response}")
else:
    print("❌ 沒有找到插入點，請確認 main.py 結構")

today = datetime.date.today().isoformat()
commit_message = f"🤖 自動加入新撩語 {command} @ {today}"

subprocess.run(["git", "add", "main.py"])
subprocess.run(["git", "commit", "-m", commit_message])
subprocess.run(["git", "push", "origin", "main"])
