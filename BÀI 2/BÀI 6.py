a=[]
for b in range(2000,3201):
 if b%7==0 and b%5!=0:
  a.append(str(b))
print(",".join(a))
