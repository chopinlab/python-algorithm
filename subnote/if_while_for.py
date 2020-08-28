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
