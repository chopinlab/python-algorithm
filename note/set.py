
# 1.0 empty set
a101 = set()
print(a101)


# 1.1 교집합, 합집합, 차집합 구하기
a111 = set([1, 2, 3, 4, 5, 6])
a112 = set([4, 5, 6, 7, 8, 9])

print(a111 & a112)
print(a111 | a112)
print(a111 - a112)


# 1.2 값 추가하기(한 개, 여러 개)
a121 = set([1, 2, 3])
a121.add(4)
print(a121)  # {1, 2, 3, 4}

a121.update([4, 5, 6])
print(a121)


# 1.3 특정 값 제거하기
a131 = set([1, 2, 3])
a131.remove(2)
print(a131)