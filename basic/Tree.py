class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, head):
        self.head = head

    def insertNode(self, data):
        if self.head is None:  # 트리에 한번도 데이터를 넣은적이 없는 경우
            self.head = Node(data)
        else:  # 트리에 노드가 하나 이상 존재 한다
            findNode = self.head  # 링크드 리스트와 마찬가지로 head 를 기준으로 탐색 을 시작해야함
            while True:
                if data < findNode.value:
                    if findNode.left is not None:
                        findNode = findNode.left
                    else:
                        findNode.left = Node(data)
                        break
                else:
                    if findNode.right is not None:
                        findNode = findNode.right

                    else:
                        findNode.right = Node(data)
                        break
        return True

    def Search(self, data):
        if self.head is None:
            return False
        else:
            findNode = self.head
            while findNode is not None:
                if findNode.value == data:
                    return findNode
                elif data < findNode.value:
                    findNode = findNode.left
                else:
                    findNode = findNode.right

        return False

    def delete(self, value):
        # 삭제할 노드 탐색
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False

            # case1
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None

        # case2
        elif self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

                # case 3
        elif self.current_node.left != None and self.current_node.right != None:  # case3
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left
            # case 3-2
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

        return True


head = Node(5)

tree = Tree(head)

for i in range(1, 5):
    tree.insertNode(i)

for i in range(6, 11):
    tree.insertNode(i)

for i in range(1, 11):
    print(tree.Search(i).value)
