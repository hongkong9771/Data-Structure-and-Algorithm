# *-* coding: utf8 *-* 
# @Time : 2021/3/6 19:21
# @Author : 危红康
# @File : whk_single_cycle_link_list.py
# @Software: PyCharm


class Node(object):
    """单循环链表的节点"""
    def __init__(self, item):
        # item存放链表元素
        self.item = item
        # 初始化节点的指针为None，next是指向下一个节点的指针，
        self.next = None

class SingleCycleLinkList(object):
    """单向循环链表类"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """计算链表长度"""
        count = 0
        cur = self._head
        if self._head is None:      # 当链表为空时，返回0
            return count
        else:
            while cur.next != self._head:
                count += 1
                cur = cur.next
            return count+1

    def items(self):
        """遍历链表"""
        # 当链表为空时
        if self.is_empty():
            print("链表为空")
        else:
            cur = self._head
            while cur.next != self._head:
                # 调用生成器，返回一个迭代器
                yield cur.item
                cur = cur.next
            yield cur.item  # 最后一个节点的元素值未输出，因此，在此处输出

    def add(self, item):
        """在链表头部添加节点"""
        # 创建节点
        node = Node(item)
        # 链表头部指向新增加的节点
        if self.is_empty():                 # 当链表为空时
            self._head = node
            node.next = node
        else:
            cur = self._head
            node.next = self._head          # 将添加的节点指针指向头部
            while cur.next != self._head:   # 找到尾部节点，使得尾部节点的指针指向新添加的节点
                cur = cur.next
            cur.next = node
            self._head = node               # 修改head指向新增加的节点

    def append(self, item):
        """在链表尾部添加节点"""
        # 创建节点
        node = Node(item)
        if self.is_empty():             # 当链表为空时
            self._head = node
            node.next = node
        else:
            cur = self._head
            node.next = cur             # 新增加的节点指针指向头节点
            while cur.next != self._head:
                cur = cur.next
            cur.next = node             # 链表尾部节点指针指向新增加的节点

    def insert(self, index, item):
        """在指定位置插入元素"""
        # 创建节点
        node = Node(item)
        if index <= 0:                  # 指定位置在第一个元素之前，在头部插入
            self.add(item)
        elif index > self.length() - 1: # 指定位置超出链表尾部，在尾部插入
            self.append(item)
        else:
            cur = self._head
            count = 0
            while count < index - 1:
                count += 1
                cur = cur.next
            # 在插入节点时，先连接后面的节点，再连接前面的节点
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除链表中的节点"""
        if self.is_empty():
            print("链表为空，不能删除此节点")
        else:
            cur = self._head
            # 当第一个节点为要删除的元素时
            if self._head.item == item:
                # 当链表只有一个节点，即头节点时，将head指针指向None
                if self._head.next == self._head:
                    self._head = None
                # 当链表不止一个节点时
                else:
                    while cur.next != self._head:       # 遍历找到尾节点
                        cur = cur.next
                    self._head = self._head.next        # 将head指针指向头节点的下一个节点，即原链表的第二个节点
                    cur.next = self._head               # 将尾节点的指针指向更新后链表的头节点，即原链表的第二个节点
            else:
                # 当被删除的元素不是头节点时
                pre = None
                while cur.next != self._head:           # 遍历链表，但是遍历不到尾节点就退出循环了
                    # 找到指定的元素之后，将所删除节点的前一个结点指向所删除节点的后一个节点，并退出判断
                    if cur.item == item:
                        pre.next = cur.next
                        return
                    else:
                        pre = cur
                        cur = cur.next
                # while循环不能遍历到链表尾节点，在此处添加对尾节点的判断
                if cur.item == item:
                    pre.next = cur.next
                    return

    def find(self, item):
        """查找元素是否存在"""
        return item in self.items()


if __name__ == '__main__':
    # 创建一个链表
    link_list = SingleCycleLinkList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    # 将节点添加至链表，使得链表的头指针指向节点
    link_list._head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node1

    # 判断链表是否为空
    print(link_list.is_empty())

    # 计算链表长度
    print(link_list.length())

    # 遍历链表
    for item in link_list.items():
        print(item, end=" ")
    print("\n")

    # 在链表头部添加节点
    link_list.add(0)
    for item in link_list.items():
        print(item, end=" ")
    print("\n")

    # 在链表尾部添加节点
    link_list.append(6)
    for item in link_list.items():
        print(item, end=" ")
    print("\n")

    # 在链表指定位置插入节点
    link_list.insert(3, 30)
    for item in link_list.items():
        print(item, end=" ")
    print("\n")

    # 删除元素为item的节点
    link_list.remove(0)
    for item in link_list.items():
        print(item, end=" ")
    print("\n")

    # 查找元素是否在链表中
    print(link_list.find(3))

