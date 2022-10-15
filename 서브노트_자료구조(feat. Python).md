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

* deque vs queue
    * queue는 양방향 큐
        * 앞, 뒤 방향에서 element를 추가하거나 삭제할 수 있다. 양쪽 끝을 모두 추출할 수 있는 큐를 일반화한 형태의 추상자료형이다.
        * 이중연결 리스트로 구현되어 있다.
        * 리스트의 pop(0)은 시간복잡도가 O(n)인데 반해, 데크의 popleft는 O(1)이다.