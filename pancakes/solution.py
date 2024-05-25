a = int(input())
b = int(input())
k = int(input())
if k >= a + b:
    print(0, 0)
elif k > a:
    print(0, a + b - k)
else:
    print(a - k, b)
