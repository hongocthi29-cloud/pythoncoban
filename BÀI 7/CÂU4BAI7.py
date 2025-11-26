import os

thuMucTaiXuong = os.path.join(os.path.expanduser("~"), "Downloads")
tenFile = "kythuatlaptrinh111.txt"
duongDan = os.path.join(thuMucTaiXuong, tenFile)

n = int(input("Bạn muốn đọc bao nhiêu dòng đầu tiên? "))

with open(duongDan, "r", encoding="utf-8") as tep:
    for i in range(n):
        dong = tep.readline()
        if dong == "":
            break   # Nếu hết file thì dừng lại
        print(dong.rstrip())
