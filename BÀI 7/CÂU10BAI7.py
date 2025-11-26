import os

duongdan = os.path.join(os.path.expanduser("~"), "Downloads")
tep = os.path.join(duongdan, "kythuatlaptrinh2222.txt")

with open(tep, "r", encoding="utf-8") as t:
    vanban = t.read()

tuvan = vanban.split()
dodai = 0
ketqua = []

for tu in tuvan:
    if len(tu) > dodai:
        dodai = len(tu)
        ketqua = [tu]
    elif len(tu) == dodai:
        ketqua.append(tu)

print("Tu dai nhat la:", ketqua)
print("Do dai:", dodai)
