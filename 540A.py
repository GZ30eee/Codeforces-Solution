n = int(input())
k1 = list(map(int, input()))
k2 = list(map(int, input()))
print(sum(min(10 - abs(k1[i] - k2[i]),
 abs(k1[i] - k2[i])) for i in range(n)))
