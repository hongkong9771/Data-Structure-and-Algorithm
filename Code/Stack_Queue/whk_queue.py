# *-* coding: utf8 *-* 
# @Time : 2021/3/24 14:12
# @Author : 危红康
# @File : whk_queue.py
# @Software: PyCharm


class Queue(object):
    """创建一个队列的类"""
    def __init__(self, size=0):
        """
        创建一个空的队列，并指定队列的大小为size
        指定两个指针front和rear，一个指向出队（front）位置，一个指向入队（rear）位置
        """
        self.queue = []
        self.size = size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        """判断队列是否为空"""
        return self.front == self.rear

    def is_full(self):
        """判断队列是否已满"""
        return self.rear - self.front == self.size

    def print_queue(self):
        """打印队列内容"""
        print(self.queue)

    def show_head(self):
        """读队头元素"""
        if self.is_empty():
            print("Queue is empty, which do not exist any item!")
            return None
        return self.queue[0]

    def length(self):
        """统计队列中元素的数量"""
        return self.rear - self.front

    def enqueue(self, item):
        """入队，在队列尾部添加元素item"""
        if self.is_full():
            print("Queue is full, which can not do enqueue operation!")
            return None
        self.queue.append(item)
        self.rear += 1

    def dequeue(self):
        """出队，在队列头部删除元素"""
        if self.is_empty():
            print("Queue is empty, which do not exist any item!")
            return None
        self.queue.pop(0)
        self.front += 1


if __name__ == '__main__':
    Q = Queue(6)
    print(Q.is_empty())

    for i in range(0, 10, 2):
        Q.enqueue(i)
    Q.print_queue()
    print(Q.rear, Q.front)      # 打印头部和尾部位置

    print(Q.show_head())
    Q.dequeue()
    Q.print_queue()
    print(Q.rear, Q.front)  # 打印头部和尾部位置

    print(Q.length())

