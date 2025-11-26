import os

duongdan = os.path.join(os.path.expanduser("~"), "Downloads")
tep = os.path.join(duongdan, "kythuatlaptrinh111.txt")
danhsach = ["A", "B", "C", "D"]

with open(tep, "w", encoding="utf-8") as t:
    for phantu in danhsach:
        t.write(phantu + "\n")

with open(tep, "r", encoding="utf-8") as t:
    noidung = t.read()

print("Noi dung vua duoc ghi vao tep la:")
print(noidung)
