# *-* coding: utf8 *-* 
# @Time : 2021/3/12 17:00
# @Author : 危红康
# @File : test.py
# @Software: PyCharm


class Node(object):
    """
    创建一个节点
    """
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.len = 0


    def get(self, index: int) -> int:   # 正确
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.len:
            return -1
        cur = self.head
        count = 0
        while count < index:
            cur = cur.next
            count += 1
        return cur.val


    def addAtHead(self, val: int) -> None:     # 正确
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self.len += 1


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
        self.len += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = Node(val)
        if index <= 0:
            self.addAtHead(val)
        elif index == self.len:
            self.addAtTail(val)
        elif index > self.len:
            return
        else:
            cur = self.head
            count = 0
            while count < index - 1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node
        self.len += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        length = self.len
        if index < 0 or index >= length:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            count = 0
            while count < index - 1:
                cur = cur.next
                count += 1
            cur.next = cur.next.next
        self.len -= 1


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

obj.addAtHead(5)
obj.addAtIndex(1, 2)
param_1 = obj.get(1)
obj.addAtHead(6)
obj.addAtTail(2)

# obj.deleteAtIndex(index)
# obj.addAtTail(val)