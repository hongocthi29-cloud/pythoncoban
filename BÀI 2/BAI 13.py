import math
a=float(input("nhap he so a: "))
b=float(input("nhap he so b: "))
c=float(input("nhap he so c: "))
if a==0:
    if b==0:
        print(" phuong trinh vo nghiem ")
    else:
        nghiem=-c/b
        print("nghiem cua phuong trinh la: " ,nghiem)
else:
   delta=b**2-4*a*c
   if delta<0:
      print("phuong trinh vo nghiem")
   elif delta==0:
      x1=x2=-b/(2*a)
      print("phuong trinh co nghiem kep",x1)
   else:
      x1=(-b+math.sqrt(delta))/(2*a)
      x2=(-b-math.sqrt(delta))/(2*a)
      print(" nghiem cua phuong trinh la: ",x1, "và", x2)
