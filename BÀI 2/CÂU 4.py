print("HỒ NGỌC THI")
a=int(input("nhap vào a: "))
b=int(input("nhap vao b: "))
if a>=b:
    print("vui long nhập các giá trị khác")
else:
    for i in range(a+1 ,b):
      if i==0:
          print("khong co nghich dao")
      else:
          d=1/i;
          print(f"1/{i} = {d:.6f}")
           
          
      
    
