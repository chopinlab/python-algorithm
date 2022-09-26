"""
완전탐색법에 나오는 내용
Programmers 모의고사

"""

import unittest


def solution(answers):

    answer = []

    person_1_pattern = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
    person_2_pattern = {0: 2, 1: 1, 2: 2, 3: 3, 4: 2, 5: 4, 6: 2, 7: 5}
    person_3_pattern = {0: 3, 1: 3, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 4, 8: 5, 9: 5}

    dic = {1: count_answer(answers, person_1_pattern),
           2: count_answer(answers, person_2_pattern),
           3: count_answer(answers, person_3_pattern)}

    val_max = max(dic.values())

    for p, q in dic.items():
        if q == val_max:
            answer.append(p)

    return answer


def count_answer(answers, pattern):

    result = 0
    for i, answer in enumerate(answers):

        temp_answer = pattern[i % len(pattern)]

        if answer == temp_answer:
            result = result + 1

    return result


class programmers_모의고사(unittest.TestCase):

    def testSolution1(self):
        a = [1, 2, 3, 4, 5]
        result = solution(a)
        self.assertEqual(result, [1])

    def testSolution2(self):
        a = [1, 3, 2, 4, 2]
        result = solution(a)
        self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
