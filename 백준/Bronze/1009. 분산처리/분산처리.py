n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a %= 10  # 마지막 자리만 보면 돼!

    if a == 0:
        print(10)
        continue

    # 패턴 저장
    pattern = []
    tmp = a
    while tmp not in pattern:
        pattern.append(tmp)
        tmp = (tmp * a) % 10

    idx = (b - 1) % len(pattern)
    print(pattern[idx])
