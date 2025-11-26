import os

thuMucTaiXuong = os.path.join(os.path.expanduser("~"), "Downloads")
tenFile = "kythuatlaptrinh111.txt"
duongDan = os.path.join(thuMucTaiXuong, tenFile)

n = int(input("Bạn muốn đọc bao nhiêu dòng cuối? "))

with open(duongDan, "r", encoding="utf-8") as tep:
    cacDong = tep.readlines()

tongDong = len(cacDong)

print(f"\n{n} dòng cuối cùng trong tệp:")
for dong in cacDong[-n:]:
    print(dong.rstrip())
