import os

thuMucTaiXuong = os.path.join(os.path.expanduser("~"), "Downloads")
tenFile = "kythuatlaptrinh111.txt"
duongDan = os.path.join(thuMucTaiXuong, tenFile)

with open(duongDan, "r", encoding="utf-8") as tep:
    soDong = sum(1 for dong in tep)

print("Số dòng trong tệp là:", soDong)
