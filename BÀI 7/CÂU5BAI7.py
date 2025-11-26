import os

thuMucTaiXuong = os.path.join(os.path.expanduser("~"), "Downloads")
tenFile = "kythuatlaptrinh111.txt"
duongDan = os.path.join(thuMucTaiXuong, tenFile)

vanBanThem = input("Nhập văn bản muốn nối vào tệp: ")
with open(duongDan, "a", encoding="utf-8") as tep:
    tep.write(vanBanThem + "\n")

print("\nNội dung tệp sau khi nối:")
with open(duongDan, "r", encoding="utf-8") as tep:
    noiDung = tep.read()
    print(noiDung)
