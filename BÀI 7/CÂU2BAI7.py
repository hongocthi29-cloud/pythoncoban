import os

thuMucTaiXuong = os.path.join(os.path.expanduser("~"), "Downloads")
tenFile = "kythuatlaptrinh111.txt"
duongDan = os.path.join(thuMucTaiXuong, tenFile)

with open(duongDan, "r", encoding="utf-8") as tep:
    noiDung = tep.read()

soKyTu = len(noiDung)
soTu = len(noiDung.split())
soDong = noiDung.count("\n") + 1 if noiDung.strip() != "" else 0

print("Số ký tự trong file:", soKyTu)
print("Số từ trong file:", soTu)
print("Số dòng trong file:", soDong)
