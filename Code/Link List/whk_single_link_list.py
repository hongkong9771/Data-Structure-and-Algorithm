# *-* coding: utf8 *-* 
# @Time : 2021/3/6 10:38
# @Author : 危红康
# @File : whk_single_link_list.py
# @Software: PyCharm


class Node(object):
    """单链表的节点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # 初始化节点的指针为None，next是指向一个节点的指针，
        self.next = None


class SingleLinkList(object):
    """单链表类"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        # None 返回True，非None返回False.
        return self._head is None

    def length(self):
        """链表长度"""
        # 初始指针指向head
        cur = self._head
        count = 0
        # 指针指向None 表示到达尾部
        while cur is not None:
            count += 1
            # 指针下移
            cur = cur.next
        return count

    def items(self):
        """遍历链表"""
        cur = self._head
        while cur is not None:
            # 调用生成器，返回一个迭代器
            yield cur.item
            # print(cur.item)
            cur = cur.next

    def add(self, item):
        """向链表头部添加元素"""
        # 创建一个以item为元素的节点node
        node = Node(item)
        # 新节点的指针指向链表的原头部节点
        node.next = self._head
        # 头部节点的指针修改为新增加的节点
        self._head = node

    def append(self,item):
        """在链表尾部添加元素"""
        # 创建一个以item为元素的节点node
        node = Node(item)
        # 先判断是否为空链表
        if self._head is None:
            """若为空链表，则链表的头部指向新节点"""
            self._head = node
        else:
            """若不是空链表，则找到链表尾部，将尾部节点的next指向新节点"""
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        """在指定位置插入元素"""
        if index <= 0:                  # 指定位置在第一个元素之前，在头部插入
            self.add(item)
        elif index > self.length() - 1: # 指定位置超出链表尾部，在尾部插入
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            while count < index-1:
                cur = cur.next
                count += 1
            # 在插入节点时，先连接后面的节点，再连接前面的节点
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除链表中的节点"""
        if self.is_empty():
            print("链表为空，不能删除此节点")
        else:
            # 当第一个元素为要删除的元素
            if self._head.item == item:
                self._head = self._head.next
            else:
                cur = self._head
                pre = None  # 用于记录被删除节点的前一个节点
                while cur is not None:      # 当删除的元素不是第一个元素时
                    # 找到指定的元素之后，将所删除节点的前一个结点指向所删除节点的后一个节点，并退出判断
                    if cur.item == item:
                        pre.next = cur.next
                        return
                    else:
                        pre = cur
                        cur = cur.next

    def find(self, item):
        """查找元素是否存在"""
        return item in self.items()


if __name__ == '__main__':
    link_list = SingleLinkList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(4)
    node4 = Node(5)
    # 将节点添加到链表，使得链表的头指针指向node1
    link_list._head = node1
    # 将第一个节点的指针指向下一个节点
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # 判断链表是否为空
    print(link_list.is_empty())

    # 计算链表长度
    print(link_list.length())

    # 遍历链表
    for i in link_list.items():
        print(i, end=" ")
    print("\n")

    # 在链表头部增加节点
    link_list.add(3)
    for i in link_list.items():
        print(i, end=" ")
    print("\n")

    # 在链表尾部增加节点
    link_list.append(7)
    for i in link_list.items():
        print(i, end=" ")
    print("\n")

    # 在链表指定位置插入节点
    link_list.insert(1, 8)
    for i in link_list.items():
        print(i, end=" ")
    print("\n")

    # 删除链表中的元素
    link_list.remove(3)
    for i in link_list.items():
        print(i, end=" ")
    print("\n")

    # 查找元素是否在链表中
    print(link_list.find(7))

    # print(link_list._head)
    # print(node1)
    # print(node1.next)
    # print(node2)