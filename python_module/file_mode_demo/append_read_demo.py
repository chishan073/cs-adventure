with open("log.txt", "a+") as f:
    f.write("✨ 新增一行 in a+ 模式\n")

    f.seek(0)
    print("🔍 檔案所有內容：")
    print(f.read())