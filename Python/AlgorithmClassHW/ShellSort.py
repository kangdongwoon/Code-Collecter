import random

def shellSort(array, n):

    interval = [57, 23, 10, 4, 1]
    for gap in interval: # 지정한 간격으로 쉘 정렬
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp: # 삽입 정렬
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp

data = [random.randint(1,100) for i in range(100)]
size = len(data)
shellSort(data, size)
print(data)