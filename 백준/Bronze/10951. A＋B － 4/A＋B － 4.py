import sys

for line in sys.stdin:                 # EOF까지 한 줄씩 읽기
    if not line.strip():               # 혹시 공백/빈 줄이 있으면 건너뛰기(안전장치)
        continue
    a, b = map(int, line.split())
    print(a + b)
