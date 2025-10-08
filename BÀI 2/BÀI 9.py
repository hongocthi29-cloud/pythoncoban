print("HỒ NGỌC THI")
chuoi = input("Nhập một xâu ký tự: ")

dem_ky_tu = {}

for ky_tu in chuoi:
    if ky_tu in dem_ky_tu:
        dem_ky_tu[ky_tu] += 1   
    else:
        dem_ky_tu[ky_tu] = 1    

print("Kết quả đếm ký tự:")
print(dem_ky_tu)
