a = input("Nhập dãy các từ: ").split()
m = max(len(x) for x in a)
print([x for x in a if len(x) == m])
