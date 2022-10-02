"""
For

예시)
a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6, 7]

1. list, tuple, string

1) value만 보여주는 경우

for i in a:
    print(i)      # 1\n 2\n 3\n 4\n 5\n

2) index만 보여주는 경우

for i in range(len(a)):
    print(i)      # 0\n 1\n 2\n 3\n 4\n

3) index, value 모두 보여주는 경우

for i, v in enumerate(a):
    print(i, v)   # 0 1\n 1 2\n 2 3\n 3 4\n 4 5\n

4) 같은 index끼리 묶어주는 경우 -> 각각 깥은 리스트끼리 묶어서 보여준다.

for p, c in zip(a, b):
    if p != c:
        return p

5) 역순으로 for문을 돌림

denominations = [1, 2, 5, 10, 20, 50, 100]

for pos, coin in reversed(list(enumerate(denominations))):
    print(pos, coin)   # 6 100\n  5 50\n  4 20\n  3 10\n  2 5\n  1 2\n  0 1\n

"""