
# 1.0 딕셔너리 타입
a101 = {1: 'hi'}
a102 = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

# 1.1 쌍 추가하기
a111 = {1: 'a'}
a111[2] = 'b'
print(a111)  # {1: 'a', 2: 'b'}

# 1.2 요소 삭제하기 -> 딕셔너리의 키와 값을 삭제한다.
a121 = {1: 'a', 2: 'b'}
del a121[1]
print(a121)  # {2: 'a'}

# 1.3 키 리스트 만들기
a131 = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a131.keys())  # dict_keys(['name', 'phone', 'birth'])
print(list(a131.keys()))
# list(a.keys())를 사용하면 된다. dict_keys, dict_values, dict_items 등은 리스트로 변환하지 않더라도 기본적인 반복(iterate) 구문(예: for문)을 실행할 수 있다.

# 1.4 밸류 리스트 만들기
a141 = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a141.values())  # dict_values(['pey', '0119993323', '1118'])
print(list(a141.values()))  # ['pey', '0119993323', '1118']

# 1.5 키 밸 쌍 얻기
a151 = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a151.items())  # dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
print(list(a151.items()))  # [('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')]

# 1.6 키로 value 얻기
a161 = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a161.get('1111'))  # pey
# print(a161['1111'])  # error 발생함 -> get을 쓰는 것이 나을 것 같은데

# 1.7 해당 키가 딕셔너리에 있지 조사하기
a171 = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print('name' in a171)  # True
print('email' in a171)  # False



