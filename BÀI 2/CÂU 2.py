import math
print("HỒ NGỌC THI")
x1=int(input("enter x1: "))
y1=int(input("enter y1: "))

x2=int(input("enter x2: "))
y2=int(input("enter y2: "))
d1= (x2-x1)**2
d2= (y2-y1)**2
D = math.sqrt(d1 + d2)

print("khoang cach cua hai diem là:", D)
