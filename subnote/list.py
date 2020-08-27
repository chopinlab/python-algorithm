"""
List 함수

zip함수 - 같은 index끼리 묶어준다.

"""
# 1. list

# 1.0 빈 List 생성
a10 = list()

# 1.1 List 합하기
a11 = [1, 2, 3]
b11 = [4, 5, 6]
print(a11 + b11)  # [1, 2, 3, 4, 5, 6]

# 1.2 List 길이 구하기
a12 = [1, 2, 3]
print(len(a12))  # 3

# 1.3 List 값 수정하기
a13 = [1, 2, 3]
a13[2] = 4
print(a13)  # [1, 2, 4]

# 1.4 List 요소 삭제하기
a141 = [1, 2, 3]
del a141[1]
print(a141)

a142 = [1, 2, 3, 4, 5]
del a142[2:]
print(a142)

# 1.5 List 정렬
a15 = [1, 2, 3, 4]
a15.append([5, 6])
print(a15)  # [1, 2, 3, 4, 5, 6]

# 1.6 List 정렬
a16 = [1, 4, 3, 2]
a16.sort()
print(a16)  # [1, 2, 3, 4]

# 1.7 List에 요소 삽입
a17 = [1, 2, 3]
a17.insert(0, 4)
print(a17)  # [4, 1, 2, 3]

# 1.8 List의 count 개수 세기
a18 = [1, 2, 3, 1]
print(a18.count(1))  # 2

# 1.9 리스트의 확장
a19 = [1,2,3]
a19.extend([4,5])
print(a19)  # [1, 2, 3, 4, 5]