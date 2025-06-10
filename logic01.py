def fu(a, b, c):
    return a <= b <= c or c <= b <= a

print(fu(5, 7, 10))  # True
print(fu(10, 7, 5))  # True