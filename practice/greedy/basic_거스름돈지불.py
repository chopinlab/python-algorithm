"""
https://skerritt.blog/greedy-algorithms/
거스름돈 지불

"""

import unittest


def solution(change, denominations):

    # solution
    answer = [0] * len(denominations)

    for pos, coin in reversed(list(enumerate(denominations))):
        # while we can still use coin, use it until we can't
        while coin <= change:
            change = change - coin
            answer[pos] += 1
    return answer


class ProgrammersTest(unittest.TestCase):

    def testSolution1(self):
        a = 30
        b = [1, 2, 5, 10, 20, 50, 100]
        result = solution(a, b)
        self.assertEqual(result, [0, 0, 0, 1, 1, 0, 0])

    def testSolution2(self):
        a = 100
        b = [1, 2, 5, 10, 20, 50, 100]
        result = solution(a, b)
        self.assertEqual(result, [0, 0, 0, 0, 0, 0, 1])

    # def testSolution3(self):
    #     a = ""
    #     b = ""
    #     result = solution(a, b)
    #     self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
