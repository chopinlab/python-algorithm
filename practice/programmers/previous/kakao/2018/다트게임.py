"""
Programmers Template
카카오톡 게임별의 하반기 신규 서비스로 다트 게임을 출시하기로 했다. 다트 게임은 다트판에 다트를 세 차례 던져 그 점수의 합계로 실력을 겨루는 게임으로, 모두가 간단히 즐길 수 있다.
갓 입사한 무지는 코딩 실력을 인정받아 게임의 핵심 부분인 점수 계산 로직을 맡게 되었다. 다트 게임의 점수 계산 로직은 아래와 같다.

1. 다트 게임은 총 3번의 기회로 구성된다.
2. 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
3. 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
4. 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
5. 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
6. 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
7. 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
8. Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
9. 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.


"""
"""
** 로직
1. 파싱하기
input - string
output - stack

2. 각각의 값 계산하기
input - stack
- *이면 전의 값도 두배 곱함 -> 전의 stack값을 뽑아서 2를 곱한 후 넣어 줌
- #이면 이번 값만 두개 더함
output - stack


3. 큐의 값 모두 더하기
input - stack
output - 숫자(int)

"""

import unittest
from collections import deque


def parse_string(dartResult):
    stack = deque()
    for i in dartResult:
        if i in '0123456789':
            if len(stack) != 0:
                temp = stack.pop()
                if temp[-1] in 'SDT*#':
                    stack.append(temp)
                    stack.append(i)
                else:
                    temp += i
                    stack.append(temp)
            else:
                stack.append(i)
        if i in 'SDT*#':
            temp = stack.pop()
            temp += i
            stack.append(temp)

    print(stack)

    return stack


def main_logic(queue: deque):
    result_queue = deque()
    temp_queue = queue
    while len(temp_queue) > 0:
        temp: str = temp_queue.popleft()
        temp_result = 1
        while len(temp) > 0:
            if temp[-1] == '#':
                temp = temp[0:len(temp) - 1]
                temp_result *= -1
            elif temp[-1] == '*':
                temp = temp[0:len(temp) - 1]
                temp_result *= 2
                # 두 개를 곱해 줌
                if len(result_queue) > 0:
                    temp_int: int = result_queue.pop()
                    temp_int *= 2
                    result_queue.append(temp_int)
            else:
                if temp[-1] == 'S':
                    temp = temp[0:len(temp) - 1]
                    temp_result *= int(temp)
                    temp = ''
                elif temp[-1] == 'D':
                    temp = temp[0:len(temp) - 1]
                    temp_result = temp_result * int(temp) * int(temp)
                    temp = ''
                elif temp[-1] == 'T':
                    temp = temp[0:len(temp) - 1]
                    temp_result = temp_result * int(temp) * int(temp) * int(temp)
                    temp = ''
        result_queue.append(temp_result)
    return result_queue



def add_stack_element(queue):
    result = 0
    temp_queue = queue
    while len(temp_queue) > 0:
        temp = temp_queue.popleft()
        result += temp
    return result


def solution(dartResult):

    answer = 0
    # solution

    result_queue = parse_string(dartResult)
    main_queue = main_logic(result_queue)
    print(main_queue)
    answer = add_stack_element(main_queue)
    return answer


class ProgrammersTest(unittest.TestCase):

    def testSolution1(self):
        a = "1S2D*3T"
        result = solution(a)
        self.assertEqual(result, 37)

    # def testSolution2(self):
    #     a = ""
    #     b = ""
    #     result = solution(a, b)
    #     self.assertEqual(result, "")
    #
    # def testSolution3(self):
    #     a = ""
    #     b = ""
    #     result = solution(a, b)
    #     self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
