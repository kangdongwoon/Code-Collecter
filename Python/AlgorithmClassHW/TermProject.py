'''
[Problem Definition]
어느 한 갑부가 자신이 가지고 있는 많은 숫자의
섬들에 관리인을 배치하려고 한다.
섬들을 위에서 찍은 위성사진을
OpenCV를 통해 섬들을 구분할 수 있도록
이진화를 시킨 사진이 있다고 할 때,
섬마다 배치해야할 관리인의 최소 인원을 알 수 있는 알고리즘을 구하시오.
단, 관리인이 관리할 수 있는 최대 섬의 면적은 3km^2로 정해져 있고
배열 1개의 크기는 약 1km^2이다.
'''
import sys
# sys.setrecursionlimit(50000)  # 재귀제한높이설정(기본값이상으로 안해주면 런타임에러) ※기본값:1000

# Direction
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

img = [ # 이진화된 맵을 표현한 Graph
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
height = len(img)
width = len(img[0])

def DFS(x, y):
    img[x][y] = 0 # 동일한 섬의 Pixel을 두 번 검사하지 않기 위해 0으로 만든다.
    tmp = 1 # 하나의 Pixel을 Count하기 위한 변수
    for i in range(4):  # (x+1, y), (x-1, y), (x, y+1), (x, y-1)
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= height or ny < 0 or ny >= width: # 사진의 해상도를 벗어날 때
            continue
        if img[nx][ny] == 1:
            tmp+=DFS(nx, ny) # 인접한 Pixel 검사하고 면적을 누적
    return tmp # 현재까지 누적된 면적 반환

def pixel():
    Keeper = 0 # 관리인 인원 수
    for i in range(height):
        for j in range(width):
            if img[i][j] == 1: # 섬의 한 Pixel을 인식하면
                Area= (DFS(i, j))
                while Area > 3 :
                    Keeper += 1 # 섬의 영역이 3이상 일때 관리인 1명 추가
                    Area -= 3
                Keeper += 1 # 하나의 섬에는 최소 한명의 관리인 배치
    print("최소 필요 관리인: ",Keeper) # 최종 필요 관리인 출력

def CreateMap():
    while True:
        try :
            print("Map의 크기를 결정하세요: ")
            height, width = list(map(int, sys.stdin.readline().split(',')))
            try :
                print("섬을 구성할 좌표의 갯수를 결정하세요: ")
                Item = int(input())
            except ValueError:  # 좌표의 개수가 안 맞을 때
                print("올바른 갯수를 입력하세요")
            else:
                return height, width, Item
        except ValueError:  # Map의 크기가 안 맞을 떄
            print("Height,Width 순으로 입력하세요.")
            print("입력 예시: 5,7")

def PrintMap():
    for i in range(height):
        for j in range(width):
            if img[i][j] == 1: # 섬의 한 Pixel을 인식하면
                print('\033[107m'+"   ",end='') # 검정색 바탕색 출력
            else :
                print('\033[40m'+"   ",end='') # 흰색 바탕색 출력
        print('\033[0m'+"") # 기본 Setting으로 개행


print("Map을 입력하시겠습니까? (입력을 원할때 Y or y 입력)" )
Answer=input()
if 'Y'== Answer or 'y' == Answer: # 사용자의 입력을 받아 모든 변수 Update
    height, width, Item = CreateMap() # 입력받은 Map 정보 반환
    img = [[0] * width for _ in range(height)]  # 빈 Img 생성
    i = 0
    while Item > 0 :
        i += 1
        try :
            print(i, "번째 좌표: x,y")
            Coor = list(map(int, input().split(',')))
            img[Coor[0]][Coor[1]] = 1 # 선택한 좌표를 Img에 Update
        except IndexError :
            print("범위 내 좌표를 정확하게 입력하세요. ex.X,Y")
            Item += 1 # Error가 났을 때 Loop 변수 +1 추가
            i -= 1 # 좌표 번호 -1 감소
        finally:
            Item -= 1

PrintMap()
pixel()






