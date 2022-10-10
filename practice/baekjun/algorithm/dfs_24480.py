"""
DFS

https://www.acmicpc.net/problem/24480
첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.
다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다.
(1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

"""


# def dfs(graph, root):
#     visited = []
#     stack = [root]
#
#     while stack:
#         n = stack.pop()
#         if n not in visited:
#             visited.append(n)
#             if n in graph:
#                 temp = list(set(graph[n]) - set(visited))
#                 # temp.sort(reverse=True)
#                 temp.sort()
#                 stack += temp
#     # return " ".join(str(i) for i in visited)
#     return visited
#
#
# # input 받는 부분
# graph = {}
# node, edge, start = map(int, input().split())
#
# for i in range(edge):
#     edge_info = input().split(' ')
#     n1, n2 = [int(j) for j in edge_info]
#
#     # 양방향 그래프에 해당
#     # 1. 한쪽 방향 그래프
#     if n1 not in graph:
#         graph[n1] = [n2]
#     elif n2 not in graph[n1]:
#         graph[n1].append(n2)
#
#     # 2. 다른 쪽 그래프
#     if n2 not in graph:
#         graph[n2] = [n1]
#     elif n1 not in graph[n2]:
#         graph[n2].append(n1)
#
# result = dfs(graph, start)
# while len(result) < node:
#     result.append(0)
#
# print("\n".join(str(i) for i in result))

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,r = map(int,input().split())
link = [[] for _ in range(n+1)]
ans = [0]*(n+1)
cur = 1

for _ in range(m):
    a,b = map(int,input().split())
    link[a].append(b)
    link[b].append(a)
for lst in link:
    lst.sort(reverse = True)

def dfs(v):
    global cur
    ans[v] = cur
    for to_v in link[v]:
        if ans[to_v]:
            continue
        cur+=1
        dfs(to_v)
dfs(r)
for i in ans[1:]:
    print(i)
