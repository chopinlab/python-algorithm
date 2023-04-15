import unittest

"""
하샤드수
https://school.programmers.co.kr/learn/courses/30/lessons/12947
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

제한사항
x는 1 이상, 10000 이하인 정수입니다.

입출력 예
arr	return
10	true
12	true
11	false
13	false
"""

def solution(x):
    sum = 0
    for v in str(x):
        sum += int(v)
    return x % sum == 0


class ProgrammersTest(unittest.TestCase):
    def testSolution1(self):
        num1 = 10
        result = solution(num1)
        self.assertEqual(result, True)

    def testSolution2(self):
        num1 = 12
        result = solution(num1)
        self.assertEqual(result, True)

    def testSolution3(self):
        num1 = 11
        result = solution(num1)
        self.assertEqual(result, False)

    def testSolution4(self):
        num1 = 13
        result = solution(num1)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
