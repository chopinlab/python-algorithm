"""
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고,
올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

입출력 예
s	answer
"()()"	true
"(())()"	true
")()("	false
"(()("	false

# stack init
stack = []

# stack push
stack = [1, 2, 3]
stack.append(4)

# stack pop
stack = [1, 2, 3]
top = stack.pop()

# stack top
stack = [1, 2, 3]
top = stack[-1]
"""

import unittest


def solution(s):
    stack = []

    for v in s:
        if v == ')':
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
        else:
            stack.append(v)

    return True if len(stack) == 0 else False



class ProgrammersTest(unittest.TestCase):
    def testSolution1(self):
        param1 = "()()"
        result = solution(param1)
        self.assertEqual(result, True)

    def testSolution2(self):
        param1 = "(())()"
        result = solution(param1)
        self.assertEqual(result, True)

    def testSolution3(self):
        param1 = ")()("
        result = solution(param1)
        self.assertEqual(result, False)

    def testSolution4(self):
        param1 = "(()("
        result = solution(param1)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
