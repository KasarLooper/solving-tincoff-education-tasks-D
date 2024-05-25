k = int(input())
m = int(input())
n = int(input())
n *= 2
a = 1 if n % k != 0 else 0
b = n // k + a
if b == 1:
    b = 2
print(b * m)
