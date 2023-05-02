# 알고리즘
## Bruce force
1. 딱히 특이한 로직이 없음

```python

```

## Greedy algorythm
1. 거스름 돈 문제
* 가지고 있는 동전 종류에서 큰 단위가 작은 단위의 배수 형태이어야 한다.
* 탐욕적으로 문제에 접근했을 때 정확한 답을 찾을 수 있다는 보장이 있을 경우엔 매우 효과적이다.
* 하나씩 빼준다는 느낌으로 할 것.
* 그리고 리스트를 계속 새로 만들어내지 말고, 투포인터 사용할 것
```python
def solution(people, limit):
    people.sort(reverse=True)
    answer = 1
    limit_tmp = limit
    i, j = 0, len(people) - 1
    while i <= j:
        if limit_tmp - people[i] >= 0:
            limit_tmp -= people[i]
            i += 1
        else:
            if limit_tmp - people[j] >= 0:
                limit_tmp -= people[j]
                j -= 1
            else:
                limit_tmp = limit
                answer += 1
    return answer
```
## Two Pointers
* 투 포인터(Two Pointers)는 배열이나 리스트와 같은 순차 자료구조에서 두 개의 포인터를 조작하여 원하는 결과를 얻는 알고리즘입니다. 일반적으로 배열에서 연속된 부분집합(subarray)을 찾거나 정렬되지 않은 배열에서 두 원소의 합이 특정 값이 되는 쌍(pair)을 찾는 문제에 활용됩니다.
투 포인터 알고리즘은 보통 시작점과 끝점을 나타내는 두 개의 포인터를 사용합니다. 이 포인터들은 각각 배열의 첫 번째 원소와 마지막 원소를 가리키는 것으로 시작합니다. 그리고 포인터들을 이동시키면서 특정 조건을 만족하는 구간(subarray)이나 쌍(pair)을 찾습니다. 이 때, 포인터들이 서로 역방향으로 이동하게 될 때까지 알고리즘을 반복하게 됩니다.
예를 들어, 배열에서 합이 특정 값이 되는 두 원소를 찾는 문제를 투 포인터로 해결할 수 있습니다. 시작점과 끝점을 나타내는 포인터를 각각 배열의 첫 번째 원소와 마지막 원소를 가리키도록 설정합니다. 그리고 두 포인터가 가리키는 원소의 합이 특정 값보다 크면 끝점을 왼쪽으로 한 칸 옮겨서 더 작은 값으로 이동시킵니다. 반대로, 합이 특정 값보다 작으면 시작점을 오른쪽으로 한 칸 옮겨서 더 큰 값으로 이동시킵니다. 이 과정을 반복하다가 합이 특정 값이 되는 두 원소를 찾으면 알고리즘을 종료합니다.
투 포인터 알고리즘은 보통 O(n) 시간 복잡도를 가집니다. 따라서 대부분의 경우 빠르고 효율적인 알고리즘이라고 할 수 있습니다.
```python
def find_pair_with_sum(arr, target_sum):
    arr.sort()
    left, right = 0, len(arr) - 1
    
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target_sum:
            return (arr[left], arr[right])
        elif curr_sum < target_sum:
            left += 1
        else:
            right -= 1
            
    return None
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

def bfs(graph, start):
    visited = []  # 방문한 노드를 저장하는 리스트
    queue = deque([start])  # 큐(Queue) 자료구조를 사용하여 탐색할 노드를 저장

    while queue:
        node = queue.popleft()  # 큐에서 노드를 하나 꺼내옴

        if node not in visited:
            visited.append(node)  # 방문한 노드를 visited 리스트에 추가
            queue.extend(graph[node])  # 해당 노드의 인접 노드들을 큐에 추가

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

```python
from collections import deque

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False for _ in range(m)] for _ in range(n) ]

    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            answer = maps[x][y]
            return answer

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if not visited[nx][ny] and maps[nx][ny] != 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1
    answer = -1
    return answer
```

```python
from collections import deque

def solution(n, edge):
    answer = 0
    # graph = [[0 for _ in range(n)] for _ in range(n)]
    graph = [[] for _ in range(n)]
    is_visit = [False for _ in range(n)]
    is_visit[0] = True
    distance = [0 for _ in range(n)]
    queue = deque()
    queue.append(0)
    
    for i, j in edge:
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)
        
        
    while queue:
        now = queue.popleft()
        
        for next in graph[now]:
            if not is_visit[next]:
                is_visit[next] = True
                queue.append(next)
                distance[next] = distance[now] + 1 
                
    distance.sort(reverse=True)    
    return distance.count(distance[0])
```

```python
from collections import deque
#0         0
#1     -1     +1
#2   -1  +1 -1  +1
#3
#4
#5

# BFS를 이용한 풀이
def solution(numbers, target):
    
    leaves = [0]
    for v in numbers:
        tmp = []
        for leave in leaves:
            tmp.append(leave - v)
            tmp.append(leave + v)
        leaves = tmp
    count = 0
    for leaf in leaves:
        if leaf == target:
            count += 1

    return count
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
* Top-Down 방식
> 탑-다운 방식은 재귀 함수를 사용하여 큰 문제를 작은 부분 문제로 분해합니다. 문제를 자연스럽게 접근하는 데 도움이 되지만, 재귀 함수의 호출로 인한 오버헤드가 
발생할 수 있습니다. 탑-다운 방식에서는 메모이제이션을 구현할 때, 해시 테이블이나 배열을 사용하여 각 부분 문제의 결과를 저장합니다.
```python
def fibonacci_top_down(n, memo):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = fibonacci_top_down(n-1, memo) + fibonacci_top_down(n-2, memo)
    return memo[n]

memo = {}
n = 10
print(fibonacci_top_down(n, memo))
```
* Bottom-Up 방식
> 바텀-업 방식은 반복문을 사용하여 작은 부분 문제부터 차례대로 해결합니다. 작은 부분 문제의 해결책을 저장하고 이를 다음 부분 문제 해결에 사용함으로써, 
> 전체 문제의 최적해를 찾습니다. 재귀 호출 오버헤드가 없기 때문에 일반적으로 탑-다운 방식보다 효율적입니다. 바텀-업 방식에서는 메모이제이션을 구현할 때, 
> 일반적으로 1차원이나 2차원 배열을 사용하여 각 부분 문제의 결과를 저장합니다.
```python
def fibonacci_bottom_up(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = 10
print(fibonacci_bottom_up(n))
```
```python
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

```

