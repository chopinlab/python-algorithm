"""
몫 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120805
정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.

제한사항
0 < num1 ≤ 100
0 < num2 ≤ 100

입출력 예
num1	num2	result
10	5	2
7	2	3
"""

import unittest


def solution(num1, num2):
    answer = int(num1 / num2)
    return answer


class ProgrammersTest(unittest.TestCase):
    def testSolution1(self):
        num1 = 10
        num2 = 5
        result = solution(num1, num2)
        self.assertEqual(result, 2)

    def testSolution2(self):
        num1 = 7
        num2 = 2
        result = solution(num1, num2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
