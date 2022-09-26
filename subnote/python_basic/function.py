# 1.0 여러 개의 입력값을 받는 함수 만들기

def add_many(*args):  # 여러 개의 인수를 받을 수 있다.
    result00 = 0
    for i in args:
        result00 = result00 + i
    return result00


result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)


# 1.1 함수의 리턴값

def add_and_mul(a, b):
    return a + b, a * b  # [a + b, a * b] 이렇게 하면 tuple이 반환된다.


result1, result2 = add_and_mul(3, 4)
print(add_and_mul(3, 4))


# 1.2 Lambda
# lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다. 보통 함수를 한줄로 간결하게 만들 때 사용한다
add = lambda a, b: a+b
result = add(3, 4)
print(result)

