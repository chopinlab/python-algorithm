import collections
import unittest

"""
프로그래머스_완주하지못한선수

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
"""

# 1. 가장 짧은 코드

# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

# 2. 처음 내가 푼 방법

# def solution(participant, completion):
#
#     participant.sort()
#     completion.sort()
#     answer = participant[-1]
#
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             answer = participant[i]
#             break
#
#     return answer


# 3. 가장 좋은 풀이 방법


def solution(participant, completion):

    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant[-1]


class TddTest(unittest.TestCase):

    def testSolution1(self):
        a = ["leo", "kiki", "eden"]
        b = ["eden", "kiki"]
        result = solution(a, b)
        self.assertEqual(result, "leo")

    def testSolution2(self):
        a = ["marina", "josipa", "nikola", "vinko", "filipa"]
        b = ["josipa", "filipa", "marina", "nikola"]
        result = solution(a, b)
        self.assertEqual(result, "vinko")

    def testSolution3(self):
        a = ["mislav", "stanko", "mislav", "ana"]
        b = ["stanko", "ana", "mislav"]
        result = solution(a, b)
        self.assertEqual(result, "mislav")


if __name__ == '__main__':
    unittest.main()
