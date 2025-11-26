import os

thuMucTaiXuong = os.path.join(os.path.expanduser("~"), "Downloads")
tenFile = "kythuatlaptrinh111.txt"
duongDan = os.path.join(thuMucTaiXuong, tenFile)

with open(duongDan, "r", encoding="utf-8") as tep:
    noiDung = tep.read()

print("Nội dung của tệp:")
print(noiDung)
