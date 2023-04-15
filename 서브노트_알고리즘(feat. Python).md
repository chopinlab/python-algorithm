# 알고리즘
## Bruce force
1. 딱히 특이한 로직이 없음

```python

```

## Greedy algorythm
1. 거스름 돈 문제
* 가지고 있는 동전 종류에서 큰 단위가 작은 단위의 배수 형태이어야 한다.
* 탐욕적으로 문제에 접근했을 때 정확한 답을 찾을 수 있다는 보장이 있을 경우엔 매우 효과적이다.
```python

```

## DFS(Depth First Search, 깊이 우선 탐색)
* 한놈만 팬다(?)라는 느낌
* 스택(Stack)을 사용

```python
def dfs(graph, start_node):
    visited = list()
    stack = list()
    stack.append(start_node)
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
            # stack.extend(reversed(graph[node]))
    return visited

print(dfs(graph_list, root_node))
```

## BFS(Breadth First Search, 너비 우선 탐색)
* python에서는 deque를 사용한다.
```python
from collections import deque

def bfs(graph, start_node):
    visited = list()
    adjacency_nodes = deque([start_node])

    while adjacency_nodes:
        node = adjacency_nodes.popleft()
        if node not in visited:
            visited.append(node)
            adjacency_nodes.extend(graph[node])
    return visited

graph = {
    'A': ['B', 'F', 'I'],
    'B': ['A', 'E', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'G', 'H'],
    'E': ['B', 'C', 'G'],
    'F': ['A', 'G'],
    'G': ['E', 'F', 'D'],
    'H': ['D'],
    'I': ['A']
}
bfs(graph, 'A')
```

## Binary Search

1. 거꾸로 구한다고 생각하면 됨
2. left값 설정하고, right값 설정하고, mid = (left + right) // 2로 생각하고, 조건에 따라 왼쪽, 오른쪽을 반복적으로 찾아 나간다.

```python
def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times)*n
    while left <= right:
        mid = (left + right) // 2
        checked = 0
        for time in times:
            checked += mid // time
            if checked >= n:
                break
        if checked >= n:
            answer = mid
            right = mid - 1
        elif checked < n:
            left = mid + 1
    return answer
```


## Recursive Function(재귀 함수)
* 재귀 함수의 종료 조건을 반드시 명시해야 한다.
```python
def recursive_function(i):
    # 종료 조건을 명시
    if i == 100:
        return
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다')
    
recursive_function(1)
```

## Dynamic Programming(동적 계획법)
* 큰 문제를 작은 문제로 나눌 수 있다.
* 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
* Top-Down 방식 - 재귀함수를 사용해 구현하는 다이나믹 프로그래밍 방법 (메모제이션 기법을 활용)
* Bottom-Up 방식 - 단순 반복문을 활용 (DP 테이블을 활용)
```python
import time

d = [0] * 50

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

for num in range(5, 40, 10):
    start = time.time()
    res = fibo(num)
    print(res, '-> 러닝타임:', round(time.time() - start, 2), '초')

# --------------------------------------------
d = [0] * 100

d[1] = 1 # 첫 번째 항
d[2] = 1 # 두 번째 항
N = 99   # 피보나치 수열의 99번째 숫자는?

for i in range(3, N+1):
    d[i] = d[i-1] + d[i-2]

print(d[N])
```

