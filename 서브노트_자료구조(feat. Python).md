# 자료 구조
## stack

```python
# stack init
stack = [] 

# stack push
stack = [1, 2, 3]
stack.append(4)

# stack pop
stack = [1, 2, 3]
top = stack.pop()

# stack top
stack = [1, 2, 3]
top = stack[-1]
```

## queue

1. list를 쓰면 비효율적이므로, deque를 쓰도록 한다.
2. 더할 땐 append, 뺄 땐 popleft 메소드를 쓴다.

```python
from collections import deque
dq = deque()
dq.append('a') # deque(['a'])
dq.append('b') # deque(['a', 'b'])
dq.popleft()   # 맨 왼쪽 것부터 차례대로 빼기
```


* deque vs queue
    * deque 양방향 큐
        * 앞, 뒤 방향에서 element를 추가하거나 삭제할 수 있다. 양쪽 끝을 모두 추출할 수 있는 큐를 일반화한 형태의 추상자료형이다.
        * 이중연결 리스트로 구현되어 있다.
        * 리스트의 pop(0)은 시간복잡도가 O(n)인데 반해, 데크의 popleft는 O(1)이다.

## heapq

1. binary 이진 트리라고 생각하면 됨
2. 자동으로 정렬이 되기 때문에, 계속해서 정렬해야 되는 문제에서 사용할 것 -> 이렇게 안풀어도 되지만, 효율성이 필요한 문제에서 유리함

```python
import heapq
heapq.heapify(hq)
heapq.heappush(hq, "a")
heapq.heappop(hq)

from heapq import heapify, heappush, heappop
def solution(scoville, K):
    answer = 0
    hq = scoville
    heapify(hq)
    while True: 
        if len(hq) == 1:
            if hq[0] >= K:
                return answer
            else:
                return -1    
        else:
            if hq[0] >= K:
                return answer
        heappush(hq, heappop(hq) + (heappop(hq)*2))
        answer += 1
    return answer


```