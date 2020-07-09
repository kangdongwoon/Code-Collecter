'''
Heap Sort
- 최대값 및 최소값을 찾아내는 연산을 빠르게 하기 위해 고안된 완전이진트리를 기본으로 한 자료구조
- Algorithm : 특정한 노드의 두 '자식 노드' 중에서 더 큰 자식과 자신의 위치를 바꾸는 알고리즘
`

최대 힙 : '부모 노드'가 '자식 노드' 보다 큰 힙
최소 힙 : '부모 노드'가 '자식 노드' 보다 작은 힙

Best        Worst       Average
nlogn       nlogn       nlogn

'''
import random
from timeit import default_timer as timer

def heapify(A, k, n):
    largest = k
    left = 2 * k + 1
    right = 2 * k + 2
    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        heapify(A, largest, n)


def heap_sort(A):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        heapify(A, i, n)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(100), 10)
start = timer()
heap_sort(x)
print(timer() - start)
print(x)
print(test(x))
