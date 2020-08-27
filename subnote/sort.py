"""
정렬에 사용되는 method
1. sort()  --> 이것이 더 많이 사용됨
list.sort() -> 해당 list가 정렬되어 오름차순으로 저장된다.
list.sort(reverse=True) -> 해당 list가 정렬되어 내림차순으로 저장된다.

2. sorted()
listA = sorted(listB)
"""


listA = [15, 22.4, 8, 10, 3.14]
listA.sort()
print(listA)

listA.sort(reverse=True)
print(listA)
