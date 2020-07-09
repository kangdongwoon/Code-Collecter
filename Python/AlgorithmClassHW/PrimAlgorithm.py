import sys  # Library for INT_MAX

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # Test 함수
    def printMST(self, parent):
        print ("Edge \tWeight")

        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])


    def minKey(self, key, mstSet):
        # 비교할 Inf Value 대입
        min = sys.maxsize
        for v in range(self.V): # 5번의 비교
            # 아직 지나가지 않은 노드에 대해 key값들을 비교해 가장 작은 Cost를 가진 노드의 Index 반환
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                #최종 최소값에 대한 Index값 반환
                min_index = v
        return min_index


    def primMST(self):
        # Edge들의 최소 Cost를 담을 List 변수, Inf 초기화
        key = [sys.maxsize] * self.V
        # 각 Node들이 누구와 연결되어 있는지 확인하는 지표
        parent = [None] * self.V
        # First Vertex를 0번 노드로 설정
        key[0] = 0
        # 한 번 지나간 노드를 체크하기 위한 List
        mstSet = [False] * self.V
        parent[0] = -1

        for cout in range(self.V):
            # 현재 노드의 최소 Cost 노드를 찾아 이동
            u = self.minKey(key, mstSet)
            # 먼저 지나갔다는 Flag를 세운다.
            mstSet[u] = True
            for v in range(self.V):
                # 현재 노드와 연결된 노드들 중 Cost를 비교해 가장 작은 Cost의 값으로 Key값을 초기화
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    # 현재노드의 최소 Cost Edge를 연결시켜줌
                    parent[v] = u

        self.printMST(parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

g.primMST();