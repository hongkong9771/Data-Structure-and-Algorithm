# *-* coding: utf8 *-* 
# @Time : 2021/3/24 10:29
# @Author : 危红康
# @File : whk_stack.py
# @Software: PyCharm


class Stack(object):
    """创建一个栈的类"""
    def __init__(self, size=0):
        """
        创建一个空栈，并指定栈的大小为size，
        初始化栈顶元素位置为-1，每增加一个元素top加1，每减少一个元素top减1
        """
        self.stack = []
        self.size = size
        self.top = -1

    def is_empty(self):
        """判断栈是否为空"""
        return self.top == -1

    def is_full(self):
        """判断栈是否已满"""
        return self.top + 1 == self.size

    def print_stack(self):
        """打印栈的内容"""
        print(self.stack)

    def length(self):
        """统计栈中元素的数量"""
        return self.top + 1

    def peek(self):
        """找出栈中的顶部项"""
        if self.is_empty():     # 调用is_empty方法，判断栈是否为空，若为空则返回None，若不为空，则返回栈顶元素
            print("Stack is empty, which do not exist any item!")
            return None
        return self.stack[-1]

    def pop(self):
        """出栈，删除栈的顶部元素"""
        if self.is_empty():     # 调用is_empty方法，判断栈是否为空，若为空则返回None，若不为空，则返回栈顶元素
            print("Stack is empty, which do not exist any item!")
            return None
        self.stack.pop()
        self.top -= 1

    def push(self, item):
        """压栈，在栈的顶部添加元素item"""
        if self.is_full():      # 调用is_full方法，判断栈是否已满，若已满则返回None，若未满，则执行压栈操作
            print("Stack is full, which can not do push operation!")
            return None
        self.stack.append(item)
        self.top += 1

if __name__ == '__main__':
    # 创建一个栈
    S = Stack(10)

    for i in range(1, 10, 2):
        S.push(i)           # 压栈
    S.print_stack()

    S.push("hello")
    S.print_stack()

    print(S.length())

    S.pop()
    S.print_stack()

    print(S.peek())