"""
counter함수 - 특정 List의 각각의 원소를 계산해 주는 함수

import collections

갯수가 많은 순으로 Dictionary형태로 보여준다.


출제) programmers_완주하지못한선수
"""

import collections

lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']
print(collections.Counter(lst))
'''
결과
Counter({'aa': 2, 'cc': 1, 'dd': 1, 'bb': 1, 'ee': 1})
'''