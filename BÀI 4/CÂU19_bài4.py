def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

P = tuple(i for i in range(2, 1000000) if is_prime(i))
print("Tuple P gồm các số nguyên tố nhỏ hơn 1 triệu đã được tạo.")
