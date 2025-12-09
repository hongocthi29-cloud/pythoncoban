import numpy as np

id_sinh_vien = np.array([101, 105, 102, 110, 103])
chieu_cao = np.array([170.2, 165.5, 172.0, 168.3, 160.7])

chi_so_sap_xep = np.lexsort((id_sinh_vien, chieu_cao))

# Lấy dữ liệu sau khi sắp xếp theo chiều cao tăng dần
id_sinh_vien_sap_xep = id_sinh_vien[chi_so_sap_xep]
chieu_cao_sap_xep = chieu_cao[chi_so_sap_xep]

print("Chỉ số mô tả thứ tự sắp xếp (lexsort):")
print(chi_so_sap_xep)

print("\nID sinh viên sau khi sắp xếp theo chiều cao tăng dần:")
print(id_sinh_vien_sap_xep)

print("\nChiều cao sau khi sắp xếp:")
print(chieu_cao_sap_xep)
