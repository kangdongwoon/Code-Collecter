Red = 'Red'
Black = 'Black'

class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data
        self.color = Red # 초기 노드는 Red Color

def left_rotate(x): # 오른쪽 자식을 위로 끌어올려 붙이고 자신은 왼쪽 밑으로 내려감
    global root
    global nil_node
    # 오른쪽 자식노드 떼기
    y = x.right
    # '오른쪽 자식노드'의 왼쪽 자식을 '오른쪽 자식노드'에 붙이고 부모를 x로 지정해준다.
    x.right = y.left
    if y.left != nil_node:
        y.left.parent = x # 부모노드 x로 설정
    # '오른쪽 자식노드'의 부모노드를 자신의 부모노드와 연결한다.
    y.parent = x.parent
    # x 노드가 root 노드일 경우
    if x.parent == nil_node:
        root = y
    # x 노드가 왼쪽 노드일 경우
    elif x == x.parent.left:
        x.parent.left = y
    # x 노드가 오른쪽 노드일 경우
    else:
        x.parent.right = y
    # x 노드의 부모와 '오른쪽 자식노드'를 부모-자식관계로 이어준다.
    y.left = x
    x.parent = y

def right_rotate(x): # 왼쪽 자식을 위로 끌어올려 붙이고 자신은 오른쪽 밑으로 내려감
    global root
    global nil_node
    # 왼쪽 자식노드 떼기
    y = x.left
    # '왼쪽 자식노드'의 오른쪽 자식을 '왼쪽 자식노드'에 붙이고 부모를 x로 지정해준다.
    x.left = y.right
    if y.right != nil_node:
      y.right.parent = x # 부모노드 x로 설정
    # '왼쪽 자식노드'의 부모노드를 자신의 부모노드와 연결한다.
    y.parent = x.parent
    # x 노드가 root 노드일 경우
    if x.parent == nil_node:
      root = y
    # x 노드가 오른쪽 노드일 경우
    elif x == x.parent.right:
      x.parent.right = y
    # x 노드가 왼쪽 노드일 경우
    else:
      x.parent.left = y
    # x 노드의 부모와 '왼쪽 자식노드'를 부모-자식관계로 이어준다.
    y.right = x
    x.parent = y

def insert_fixup(z):
    global nil_node
    global root
    while z.parent.color == Red: # z 부모노드가 Red이면
      if z.parent == z.parent.parent.left: #z.parent 가 왼쪽 노드이면
          y = z.parent.parent.right # z.parent의 Uncle노드
          if y.color == Red: #case 3-1 : Uncle노드가 Red일때 Parent와 Uncle을 Black으로 만들고
              z.parent.color = Black
              y.color = Black
              z.parent.parent.color = Red # 그들의 Parent를 Red로 변경시켜준다.
              z = z.parent.parent
          else:
              if z == z.parent.right: #case 3-2-2 : z가 오른쪽 노드이면
                  z = z.parent # z를 parent node로 올리고
                  left_rotate(z) # left_rotate
              #Uncle Node는 이미 Black이다.
              z.parent.color = Black #made parent black
              z.parent.parent.color = Red #made parent red
              right_rotate(z.parent.parent)
      else: # z.parent is the right child
          y = z.parent.parent.left #uncle of z
          if y.color == Red: # Case 3-1
              z.parent.color = Black
              y.color = Black
              z.parent.parent.color = Red
              z = z.parent.parent
          else:
              if z == z.parent.left: # Case 3-2-2
                  z = z.parent #marked z.parent as new z
                  right_rotate(z)
              # Uncle Node는 이미 Black이다.
              z.parent.color = Black #made parent black # Case 3-2-1
              z.parent.parent.color = Red #made parent red
              left_rotate(z.parent.parent)
      root.color = Black

def insert(z):
    global root
    global nil_node
    y = nil_node #nll_node 대입
    temp = root #현재 root node 대입

    while temp != nil_node: # root node에 값이 있다면
	    y = temp # 부모노드 저장하기 위한 변수 y
	    if z.data < temp.data:
	      temp = temp.left
	    else:
	      temp = temp.right
    # temp에 z노드가 들어갈 nil 노드 저장
    z.parent = y # z 노드의 부모 지정

    if y == nil_node: # root 노드에 처음 추가할 때
        root = z # 현재 노드 저장
        z.color = Black # Color Black으로 바꿔줌
    elif z.data < y.data: # Parent Data와 비교후 작으면 왼쪽 크면 오른쪽 자식과 연결
    	y.left = z
    else:
    	y.right = z
    # 자식 노드들 nil_node에 연결하기
    z.right = nil_node
    z.left = nil_node

    insert_fixup(z)

def inorder(n):
    if n != nil_node:
      inorder(n.left)
      print(n.data)
      inorder(n.right)

def search(n, key):
    while n != nil_node and key != n.data:
        if key < n.data:
            n = n.left
        else:
            n = n.right
    return n

if __name__ == '__main__':

    nil_node = TreeNode(0) # leaf 노드의 이름 nil 노드로 지정
    nil_node.color=Black # nil node들의 색깔은 black이다.
    root = nil_node # root 노드의 초기값 : nil 노드

    values = [110, 120, 30, 100, 90, 40, 50,10, 20, 60, 70, 80, 150, ]
    for i in values:
        insert(TreeNode(i)) # 배열에 있는 key 값들을 RBT에 넣는다.

    tmp=search(root,40) # data값이 40인 노들 root로부터 찾아서 tmp에 넣는다.
    inorder(tmp) # data가 40인 노드로부터 밑에 있는 노드 순서대로 정렬하는 함수, 인자를 root(90)로 넣으면 모두 출력가능!