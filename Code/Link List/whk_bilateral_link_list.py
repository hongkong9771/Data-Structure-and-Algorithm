# *-* coding: utf8 *-* 
# @Time : 2021/3/9 14:33
# @Author : 危红康
# @File : whk_bilateral_link_list.py
# @Software: PyCharm


class Node(object):
    """双向链表的节点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # 初始化节点的指针为None，next是指向下一个节点的指针，
        self.next = None
        # 初始化节点的指针为None，pre是指向上一个节点的指针
        self.pre = None


class BilateralLinkList(object):
    """双向链表类"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """计算链表长度"""
        count = 0
        cur = self._head
        # 遍历到尾节点的距离
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        """遍历链表"""
        if self.is_empty():                     # 当链表为空时
            print("链表为空链表，无法遍历...")
            return
        cur = self._head
        while cur is not None:
            # 调用生成器，返回一个迭代器
            yield cur.item
            cur = cur.next

    def add(self, item):
        """在链表头部添加节点"""
        # 创建一个以item为元素的节点node
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            self._head.pre = node       # 原始头节点的pre指针指向新增加的节点
            node.next = self._head      # 新增加节点的next指针指向原始头节点
            self._head = node           # head指针指向新增加的节点，将此节点作为头节点

    def append(self, item):
        """在链表尾部添加节点"""
        # 创建一个以item为元素的节点node
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:  # 遍历找到尾节点
                cur = cur.next
            cur.next = node             # 原始尾节点的next指针指向新增加的节点
            node.pre = cur              # 新增加节点的pre指针指向原始尾节点

    def insert(self, index, item):
        """在链表指定位置插入节点"""
        # 创建一个以item为元素的节点node
        node = Node(item)
        # 当指定位置在头节点前面时
        if index <= 0:
            self.add(item)
        # 当指定位置在尾节点后面时
        elif index >= self.length():
            self.append(item)
        # 当指定位置在链表中间时
        else:
            cur = self._head
            count = 0
            while count < index:
                count += 1
                cur = cur.next
            cur.pre.next = node     # 插入点位置的前一个节点的next指针指向新增加的节点
            node.pre = cur.pre      # 插入点的pre指针指向插入点位置的前一个结点
            node.next = cur         # 插入点的next指针指向插入点位置的后一个节点
            cur.pre = node          # 插入点位置的后一个节点的pre指针指向新增加的节点

    def remove(self, item):
        """删除链表中的节点"""
        if self.is_empty():
            print("链表为空，无法删除节点....")
        else:
            # 当删除的节点为头节点时
            if self._head.item == item:
                # 当链表只包含一个元素时
                if self._head.next is None:
                    self._head = None
                # 当链表不止一个元素时
                else:
                    self._head.next.pre = None          # 将第二个节点的pre指针指向None
                    self._head = self._head.next        # 将head指针指向原始链表的第二个节点
            else:
                cur = self._head
                # 当删除的节点不为头节点时
                while cur.next is not None:      # 遍历链表，但是遍历不到尾节点就退出循环了
                    if cur.item != item:
                        cur = cur.next
                    else:
                        cur.next.pre = cur.pre
                        cur.pre.next = cur.next
                        return
                if cur.item == item:        # 当要删除的节点为尾节点时
                    cur.pre.next = None

    def find(self, item):
        return item in self.items()


if __name__ == '__main__':
    print("双向链表程序开始执行...")
    link_list = BilateralLinkList()

    # 在链表头部增加节点
    list_head = [5, 4, 3, 2, 1, 0]
    for i in list_head:
        link_list.add(i)

    # 判断链表是否为空
    print(link_list.is_empty())

    # 计算链表长度
    print(link_list.length())

    # 遍历链表元素
    for item in link_list.items():
        print(item, end=" ")
    print("\n")

    # 在链表尾部增加节点
    list_tail = [6,7,8,9,10]
    for i in list_tail:
        link_list.append(i)
    for item in link_list.items():
        print(item, end=" ")
    print("\n")

    # 在链表指定位置中插入节点
    link_list.insert(6, 30)
    for item in link_list.items():
        print(item, end=" ")
    print("\n")

    # 删除节点
    link_list.remove(10)
    for item in link_list.items():
        print(item, end=" ")
    print("\n")

    # 查找元素是否存在
    print(link_list.find(11))




