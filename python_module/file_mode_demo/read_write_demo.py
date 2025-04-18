with open("notes.txt", "w") as f:
    f.write("第一行\n第二行\n")

with open("notes.txt", "r+") as f:
    content = f.read()
    print("🔍 原內容：")
    print(content)

    f.seek(0)
    f.write("【已修改】")