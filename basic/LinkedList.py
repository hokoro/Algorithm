class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)  # head 노드 선언

    def append(self, data):
        cur = self.head
        while cur.next is not None:  # cur 의 마지막 노드 가 되기 전까지
            cur = cur.next  # 다음 노드로 계속 연결한다.
        cur.next = Node(data)

    def print_all(self):
        cur = self.head  # head 부터 순회하기 위해
        while cur is not None:
            print(cur.data)
            cur = cur.next  # 다음 노드가 없을때까지 계속 탐색 해야 한다.

    def get_node(self, index):
        cnt = 0
        node = self.head  # 항상 head 노드를 고정하고  탐색 을 시작 한다.
        while cnt < index:
            cnt += 1
            node = node.next  # 계속해서 cnt  == index 랑 같아질때 까지 다음 노드로 위치를 바꾸고

        return node  # 해당 노드를 리턴

    def add_node(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)  # 노드를 삽입하기 위해 이전 노드의 위치를 알아야 한다
        next_node = node.next  # 다음 노드 위치 초기화
        node.next = new_node  # 노드의 다음을 새로운 노드 추가
        new_node.next = next_node  # 새로운 도드의 다음을 next node 로 설정

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next # 삭제할 노드의 다음 노드랑 연결
