print("HỒ NGỌC THI")
x, y = 0, 1
tong_chan = 0

print("Dãy Fibonacci nhỏ hơn 4.000.000:")

while x < 4000000:
  print(x, end=" ")
  if x % 2 == 0:
     tong_chan += x
  x, y = y, x + y

print("\nTổng các số chẵn trong dãy:", tong_chan)
