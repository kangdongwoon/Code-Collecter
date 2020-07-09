import random

Matrix =[[0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]]

def DP_Matrix(matrix):
    # matrix와 똑같은 크기의 배열 생성
    copy_matrix = [[None] * len(matrix) for i in range(len(matrix))]
    # 행렬의 초기값을 동일하게 맞춰준다
    copy_matrix[0][0] = matrix[0][0]
    # 첫 번째 열의 Cost를 차례로 더함
    for i in range(1,len(matrix)):
        copy_matrix[i][0] = matrix[i][0] + copy_matrix[i-1][0]
    # 첫 번쨰 행의 Cost를 차례로 더함
    for j in range(1,len(matrix)):
        copy_matrix[0][j] = matrix[0][j] + copy_matrix[0][j-1]
    # 2행 2열의 Data부터 왼쪽/위 Data를 비교해 더 큰 Cost의 값과 자기 자신의 Data를 더해 값을 저장한다.
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix)):
            copy_matrix[i][j] = matrix[i][j] + max(copy_matrix[i-1][j], copy_matrix[i][j-1])
    #최종 Cost 출력
    return copy_matrix[len(matrix)-1][len(matrix)-1]

def Print_Matrix(matrix): # Matrix 출력함수
    for i in range(0,len(matrix)):
        print(matrix[i])

def Make_Matrix_Random(matrix): # Matrix 랜덤생성함수
    for i in range(len(matrix)):
        matrix[i] = random.sample(range(1,10),len(matrix[i]))

Make_Matrix_Random(Matrix)
Print_Matrix(Matrix)
print(DP_Matrix(Matrix))