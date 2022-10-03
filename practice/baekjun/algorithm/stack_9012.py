"""
stack
https://www.acmicpc.net/problem/9012
"""

# (())()) -> NO
"""
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

3
((
))
())(()
"""


def is_valid_list(element):
    """ 스택을 이용해서 유효한지 확인하는 함수"""
    temp_stack = []
    is_valid = False

    for i in element:
        if i == '(':
            temp_stack.append(i)
        elif i == ')':
            if len(temp_stack) > 0:
                top = temp_stack[-1]
                if top == '(':
                    temp_stack.pop()
                else:
                    temp_stack.append(i)
            else:
                temp_stack.append(i)

    if len(temp_stack) == 0:
        is_valid = True

    if is_valid:
        return "YES"
    else:
        return "NO"


input_list = list()
for _ in range(int(input())):
    input_list.append(input())

for input_element in input_list:
    result = is_valid_list(input_element)
    print(result)





