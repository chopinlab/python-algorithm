
# 1. Integer
a = 0o34  # 8진수
b = 0x2A  # 16진수

# 1.1 x의 y제곱
c = 3 ** 4  # 결과 81
# 1.2 나머지 반환
d = 7 % 3   # 결과 1

# 1.3 몫을 반환
e = 7 // 3  # 결과 2

# 2. String

# 2.1 MultiLine
f = """하이염
하이염
."""

# 2.2 문자열 곱하기
g = "=" * 50

# 2.3 문자열 길이 구하기
h = len(g)

# 2.4 문자열 인덱싱
i = "hihihi"
print(i[2])  # h
print(i[-2])  # h

# 2.5 문자열 슬라이싱
j = "Life is too short, You need Python"
print(j[0:4])
print(j[3:])

# 2.6 문자 개수 세기
a26 = "hobby"
print(a26.count('b'))

# 2.7 문자열 삽입
a27 = ",".join('abcd')
print(a27)

a271 = ",".join(['a', 'b', 'c', 'd'])
print(a271)

# 2.8 문자열 교환
a28 = "Life is too short"
print(a28.replace("Life", "Your leg"))

# 2.9 문자열 나누기
a29 = "Life is too short"
print(a29.split())  # 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준
