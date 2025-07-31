import math

n = int(input())
for _ in range(n):
	x, y = map(int, input().split())
	d = y - x  # 총 이동 거리
	root = int(math.sqrt(d))  # d의 제곱근의 정수 부분

	if root ** 2 == d:
		print(2 * root - 1)
	elif root ** 2 < d <= root * (root + 1):
		print(2 * root)
	else:
		print(2 * root + 1)
