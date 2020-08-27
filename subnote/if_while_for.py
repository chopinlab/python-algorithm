# 1.0 if문 기본
a10 = ['paper', 'cellphone']
b10 = True
if 'money' in a10:
    print("택시를 타고가라")
elif b10:
    print("택시를 타고가라")
else:
    print("걸어가라")

# 1.1 if문에서 여러 값을 비교

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:  # for문을 돌릴 필요없이, 해당 리스트에 값이 들어있나를 판단할 수 있다.
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 1.2 3항 연산자
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우

score = 80
if score >= 60:
    message = "success"
else:
    message = "failure"

message = "success" if score >= 60 else "failure"


# 2.0 for문
test_list = ['one', 'two', 'three']
for i in test_list:  # 리스트(또는 튜플, 문자열)
    print(i)

# 2.1 range함수
add = 0
for i in range(11):  # 0부터 10까지.. 11은 포함되지 않음, range(11) = range(0, 11)
    add = add + i

print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

# 2.2 enumerate 함수, index와 value값을 모두 필요하는 경우

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)





