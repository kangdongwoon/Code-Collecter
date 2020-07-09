import random
from timeit import default_timer as timer

class Node(object):
    def __init__(self, key, parent):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent    #부모 Node 주소를 저장할 변수

def insert(node,key,parent):
    if node is None:
        node = Node(key, parent)    # key값과 parent node의 주소를 저장한다.

    elif key < node.key:
        node.left = insert(node.left, key,node) #왼쪽 node로 이동하면서 자신의 주소를 넘겨준다.
    else:
        # node.parent = node
        node.right = insert(node.right, key,node)   #오른쪽 node로 이동하면서 자신의 주소를 넘겨준다.
    return node

# PPT에 설명되어 있음
def search(node, key):
    if node is None or node.key == key:
        return node
    if key < node.key:
        return search(node.left, key)
    return search(node.right, key)

def delete(node):
    global root # root를 전역변수로 사용하기 위해서 선언
    if node == root: # root 노드일 경우(parent노드가 없음)
        root = delete_node(node) # 노드지우기!
    elif node == node.parent.left: # parent노드의 왼쪽 자식을 지우는 경우
        node.parent.left = delete_node(node) # 노드지우기!
    else: # parent노드의 오른쪽 자식을 지우는 경우
        node.parent.right = delete_node(node) # 노드지우기!


def delete_node(node):
    if node.left is None and node.right is None: # 자식이 없는 노드
        return None
    elif node.left is not None and node.right is None: # 왼쪽 자식만 있는 노드
        return node.left # 왼쪽 자식을 Return하여 Parent_node에 연결시켜준다.
    elif node.right is not None and node.left is None: # 오른쪽 자식만 있는 노드
        return node.right # 오른쪽 자식을 Return하여 Parent_node에 연결시켜준다.
    else: # 자식이 둘다 있는 노드
        child = node.right # 오른쪽 자식노드에 들어간다.
        while child.left is not None: # 자식노드 중 가장 최소값을 찾을때까지 반복
            parent = child      # 최종 최소값 노드의 부모노드
            child = child.left  # 최종 최소값 노드
        node.key = child.key    # 삭제노드의 키값을 최종 최소값 노드의 키값으로 바꾼다.
        if child == node.right: # 가장 최소값이 오른쪽 자식노드일 경우
            node.right = child.right # 오른쪽 자식노드와 최소값 노드를 연결시켜준다.
        else:
            parent.left = child.right # '최소값 노드'의 우측을 '최소값 노드의 부모노드' 왼쪽과 연결시켜준다.
        return node

x = random.sample(range(10), 10)
value = x[5]

root=None
for i in x:
    root = insert(root, i,None)

found = search(root, value)
if search(root, value) is None:
    print("찾고자하는 값 : ",value,"는 없습니다.")
else:
    print("찾고자하는 값 : ",value,"는 있습니다.")

delete(found)

if search(root, value) is None:
    print("찾고자하는 값 : ",value,"는 없습니다.")
else:
    print("찾고자하는 값 : ",value,"는 있습니다.")