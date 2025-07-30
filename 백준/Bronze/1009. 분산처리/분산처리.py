t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    a %= 10  # 마지막 자리만 보면 되니까!
    
    if a == 0:
        print(10)
    else:
        pattern = []
        tmp = a
        while tmp not in pattern:
            pattern.append(tmp)
            tmp = (tmp * a) % 10
        # 주기적으로 반복되기 때문에 b를 주기의 길이로 나눠서 인덱스 결정
        idx = (b - 1) % len(pattern)
        print(pattern[idx])
