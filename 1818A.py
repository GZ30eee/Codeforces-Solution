def solve():
    n, k = map(int, input().split())
    v = [input() for _ in range(n)]
    ans = 1
    for i in range(1, n):
        if v[i] == v[0]:
            ans += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()
