"""
Programmers Template
문제 설명
n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.

"""

import unittest

def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    return answer


def dfs(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else: return 0
    else:
        answer += dfs(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += dfs(numbers, target, depth+1)
        return answer


# leaf를 한번에 구한다고 생각하면 되네
# def solution(numbers, target):
#     answer = 0
#     leaves = [0]
#     print(leaves)
#     for num in numbers:
#         tmp = []
#         for parent in leaves:
#             tmp.append(parent + num)
#             tmp.append(parent - num)
#         leaves = tmp
#     for leaf in leaves:
#         if leaf == target:
#             answer += 1
#     return answer


class ProgrammersTest(unittest.TestCase):

    def testSolution1(self):
        a = ""
        b = ""
        result = solution(a, b)
        self.assertEqual(result, "")

    def testSolution2(self):
        a = ""
        b = ""
        result = solution(a, b)
        self.assertEqual(result, "")

    # def testSolution3(self):
    #     a = ""
    #     b = ""
    #     result = solution(a, b)
    #     self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
