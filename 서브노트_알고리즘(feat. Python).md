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

