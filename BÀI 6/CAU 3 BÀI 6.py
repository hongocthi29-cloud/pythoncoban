class Nguoi:
    def gioiTinh(self):
        return "Không xác định"


class Nam(Nguoi):
    def gioiTinh(self):
        return "Nam"


class Nu(Nguoi):
    def gioiTinh(self):
        return "Nữ"


# Ví dụ sử dụng
a = Nam()
b = Nu()

print(a.gioiTinh())   # In: Nam
print(b.gioiTinh())   # In: Nữ
