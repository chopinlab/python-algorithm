"""
Programmers Template

"""

import unittest


def solution(triangle):
    n = len(triangle)
    dp = [[0] * i for i in range(1, n+1)]  # 동적 계획법을 위한 2차원 배열 초기화

    # 첫 번째 행은 원래 삼각형의 값을 그대로 사용
    dp[0][0] = triangle[0][0]

    # 삼각형의 두 번째 행부터 마지막 행까지 순회하며 최대 합 계산
    for i in range(1, n):
        for j in range(i+1):
            # 왼쪽 끝 원소인 경우
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            # 오른쪽 끝 원소인 경우
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            # 그 외의 경우
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    # 마지막 행에서 최대값을 반환
    return max(dp[-1])


class ProgrammersTest(unittest.TestCase):

    def testSolution1(self):
        a = [[7], [3,8]]
        # b = ""
        result = solution(a)
        self.assertEqual(result, 15)

    def testSolution2(self):
        a = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
        # b = ""
        result = solution(a)
        self.assertEqual(result, 30)

    def testSolution3(self):
        a = ""
        b = ""
        result = solution(a, b)
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
