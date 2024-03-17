a, b, c = [int(i) for i in input().split()]

a, b = min(a,b), max(a,b)
print(a+min(c,a+b)+min(b,a+c))
