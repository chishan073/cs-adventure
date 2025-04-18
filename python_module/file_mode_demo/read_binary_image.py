with open("cat.jpg", "rb") as f:
    binary_data = f.read(10)
    print("📦 前 10 個位元組：", binary_data)