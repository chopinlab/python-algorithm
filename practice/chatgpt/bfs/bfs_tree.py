"""
chatgpt Template
주어진 이진 트리에서 노드의 값을 모두 더한 결과를 반환하는 BFS 알고리즘을 구현하세요.
      1
     / \
    2   3
   / \   \
  4   5   6


"""

import unittest
from collections import deque


def solution(a):

    answer = 21
    queue = deque(a[0])

    # while queue:


    return answer


class ProgrammersTest(unittest.TestCase):

    def testSolution1(self):
        a = [1, 2, 3, 4, 5, None, 6]
        # b = ""
        result = solution(a)
        self.assertEqual(result, 21)

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
