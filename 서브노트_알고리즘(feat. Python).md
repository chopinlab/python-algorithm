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
def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]
    
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(DFS_with_adj_list(graph_list, root_node))
```