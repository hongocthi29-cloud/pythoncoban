def benefit(t, n, k):
    rate = t / 100
    final_amount = n * (1 + rate) ** k
    return final_amount
t = float(input("Nhập lãi suất (%/tháng): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))
result = benefit(t, n, k)
print("Số tiền nhận được sau", k, "tháng là:", round(result, 2))
