s = input("Nhập chuỗi: ")
new_s = ''.join(ch for ch in s if not ch.isdigit())
print("Chuỗi sau khi loại bỏ chữ số là:", new_s)
