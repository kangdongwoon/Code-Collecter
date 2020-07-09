# Python program to print topological sorting of a DAG
from collections import defaultdict

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_front(self, data):  # 연결 리스트의 맨 앞에 새 노드 삽입
        if self.size is 0:  # 연결 리스트가 비어있을 경우
            self.head = Node(data, None)  # head노드에 추가
        else:
            self.head = Node(data, self.head)  # 새 노드 추가
        self.size += 1

    def print_list(self):
       p = self.head
       while p:
           if p.next != None: # head노드부터 끝까지 출력
               print(p.data, ' -> ', end='')
           else:
               print(p.data)
           p = p.next  # 노드 순차탐색

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        self.linked_list = LinkedList() # 결과값을 담을 LinkedList 생성

    def addEdge(self, u, v):
        self.graph[u].append(v) # list graph에 Edge 추가

    def DFS(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False: # 이전 노드에 방문한적이 없다면
                self.DFS(i, visited)
        # 마지막 노드에 방문하면 linked_list의 앞쪽에 추가
        self.linked_list.insert_front(v)

    def TopologicalSort(self):
        visited = [False] * self.V # Visited Flag 변수 List
        for i in range(self.V): # 모든 노드 방문여부 검사
            if visited[i] == False: # 아직 방문하지 않았다면
                self.DFS(i, visited)

g = Graph(6)
# Edge 추가
g.addEdge(5, 3)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.TopologicalSort()
g.linked_list.print_list()