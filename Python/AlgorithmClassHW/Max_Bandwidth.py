import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] # 그래프 생성
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for i in range(1,self.V):
            print(dist[i],"-",i, " : ", self.graph[i][dist[i]]) # 노드들의 최대 dist값을 출력

    def maxDistance(self, dist, sptSet):
        max = 0
        for v in range(self.V):
            if dist[v] > max and sptSet[v] == False: # 방문하지 않은 노드 기준 Max값 갱신
                max = dist[v]
                max_index = v
        return max_index

    def Max_Bandwidth(self, src):
        dist = [0] * self.V # 거리값 초기화
        dist[src] = sys.maxsize # 시작 노드 Infinite
        sptSet = [False] * self.V # 방문 노드집합 초기화
        parent = [None] * self.V
        parent[0]= -1
        for cout in range(self.V):

            u = self.maxDistance(dist, sptSet) #dist에 연결된 간선으로 Max값 갱신
            sptSet[u] = True # Max값 노드 방문완료
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] < min(dist[u] , self.graph[u][v]):
                    dist[v] = min(dist[u] , self.graph[u][v])
                    parent[v] = u
                    # dist값과 간선을 비교해 작은 것과 현재 dist 중 큰 것으로 초기화
        self.printSolution(parent)

g = Graph(6)
g.graph = [[0, 3, 9, 6, 0, 0],
           [3, 0, 2, 0, 7, 0],
           [9, 2, 0, 8, 5, 1],
           [6, 0, 8, 0, 0, 4],
           [0, 7, 5, 0, 0, 0],
           [0, 0, 1, 4, 0, 0]
           ];

g.Max_Bandwidth(0)