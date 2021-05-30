# *-* coding: utf8 *-* 
# @Time : 2021/4/13 14:48
# @Author : 危红康
# @File : binary search tree.py
# @Software: PyCharm


class TreeNode(object):
    """定义树节点"""
    def __init__(self, value, parent = None, left = None, right = None):
        '''
        value为树节点存储的数据
        parent为树节点的父节点
        left为左子节点
        right为右子节点
        '''
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def isLeft(self):
        '''判断是否为左子节点'''
        return self.parent and self.parent.left == self

    def isRight(self):
        '''判断是否为右子节点'''
        return self.parent and self.parent.right == self

    def hasLeft(self):
        '''判断是否有左子节点'''
        return self.left is not None

    def hasRight(self):
        '''判断是否有右子节点'''
        return self.right is not None

    def isLeaf(self):
        '''判断是否为叶子节点'''
        return not (self.left or self.right)
        # return not (self.hasLeft or self.hasRight)    # 利用已定义好的函数来判断是否含有左右子节点函数来判断叶子节点

    def isRoot(self):
        """判断是否为根节点"""
        return not self.parent

class BinSearchTree(object):
    '''创建二叉搜索树'''
    def __init__(self):
        '''定义初始化函数'''
        self.root = None        # 初始化根节点为None

    def get_min(self, node):
        """找到以node为根节点的子树的最小节点"""
        while node.left is not None:
            node = node.left
        return node

    def __insert(self, value):
        """
        向树结构中添加节点
        添加单个树节点
        """
        node = TreeNode(value)
        if self.root is None:       # 当BST为空时，将此节点设置为根节点
            self.root = node
        else:
            parent_node = self.root # 从根节点开始查找位置
            while True:     # 从根节点开始循环查找
                if node.value < parent_node.value:  # 当待插入节点的值小于父节点的值时
                    if not parent_node.hasLeft():   # 当父节点的左子节点为空时，将待插入节点插入至此处，然后跳出循环
                        parent_node.left = node
                        break
                    else:
                        parent_node = parent_node.left  # 当父节点的左子节点不为空时，将此左子节点设置为新的父节点，向下深入寻找
                else:                                   # 当待插入节点的值大于父节点的值时
                    if not parent_node.hasRight():      # 当父节点的右子节点为空时，将待插入节点插入至此处，然后跳出循环
                        parent_node.right = node
                        break
                    else:
                        parent_node = parent_node.right # 当父节点的右子节点不为空时，将此右子节点设置为新的父节点，向下深入寻找
            node.parent = parent_node   # 为新插入的节点设置父节点

    def insert(self, values):
        """
        调用__insert，向树结构中添加多个树节点（以列表形式）
        """
        for value in values:
            self.__insert(value)
        return self

    def search(self, value):
        '''
        查找值为value的树节点
        '''
        if self.root is None:
            raise Exception("The Tree is Empty！")
        else:
            parent_node = self.root
            while parent_node and parent_node.value != value:   # 判断parent_node非空是为了避免出现所查询的树节点不存在的情况
                if value < parent_node.value:
                    parent_node = parent_node.left
                else:
                    parent_node = parent_node.right
            if parent_node is None:
                print("The Tree Node doesn't Exist!")
            # print(parent_node)
            return parent_node

    def remove(self, value):
        """
        一、当树为空时
        二、当要删除的节点不存在时
        三、当要删除的节点存在时，可分为以下五种情况讨论
        1.当只有一个根节点，且要删除的节点就为根节点时
        2.当要删除的节点没有左、右子节点时，即为叶子节点
        3.当要删除的节点只有右子树时
        4.当要删除的节点只有左子树时
        5.当要删除的节点既有左子树，又有右子树时
        """
        # 一、树为空的情况在search函数中已经判断了，此处无需再次判断
        search_node = self.search(value)

        # 二、当要删除的节点不存在时
        if search_node is None:
            raise Exception("The Tree Node doesn't Exist!")

        # 三、当要删除的节点存在时，可分为以下五种情况讨论
        # 1.当只有一个根节点，且要删除的节点就为根节点时
        if search_node.isRoot() and not search_node.hasLeft() and not search_node.hasRight():
            search_node = None

        # 2.当要删除的节点没有左、右子树时
        elif search_node.isLeaf():
            if search_node.isLeft():            # 当该节点为左子节点时
                search_node.parent.left = None
            else:                               # 当该节点为右子节点时
                search_node.parent.right = None

        # 3.当要删除的节点只有右子树时
        elif search_node.hasRight() and not search_node.hasLeft():
            # 当要删除的节点为左子节点时
            if search_node.isLeft():
                search_node.parent.left = search_node.right
                search_node.right.parent = search_node.parent
            # 当要删除的节点为右子节点时
            elif search_node.isRight():
                search_node.parent.right = search_node.right
                search_node.right.parent = search_node.parent
            else:
            # 当要删除的节点为根节点时
                search_node.right.parent = None     # 将被删除节点的右子树的父节点设置为None
                self.root = search_node.right       # 将根节点设置为被删除节点的右子节点

        # 4.当要删除的节点只有左子树时
        elif search_node.hasLeft() and not search_node.hasRight():
            # 当要删除的节点为左子节点时
            if search_node.isLeft():
                search_node.parent.left= search_node.left
                search_node.left.parent = search_node.parent
            # 当要删除的节点为右子节点时
            elif search_node.isRight():
                search_node.parent.right = search_node.left
                search_node.left.parent = search_node.parent
            else:
            # 当要删除的节点为根节点时
                search_node.left.parent = None      # 将被删除节点的左子树的父节点设置为None
                self.root = search_node.left        # 将根节点设置为被删除节点的左子节点

        # 5.当要删除的节点既有左子树，又有右子树时
        else:
            min_node = self.get_min(search_node.right)  # 找到右子树的最小子节点
            self.remove(min_node.value)                 # 将该最小子节点的值赋给被删除的节点，并将最小子节点删除
            search_node.value = min_node.value


    '''
    二叉树的遍历分为两种：
    一、深度优先遍历
    1.先根次序遍历，简称先序遍历，即先遍历根节点，再遍历左右子节点  （根->左->右）
    2.中根次序遍历，简称中序遍历，即先遍历左子节点，然后中间遍历根节点，最后遍历右节点  （左->根->右）
    3.后根次序便利，简称后序遍历，即先遍历左右子节点，最后再遍历根节点。  （左->右->根）
    Tips：使用递归遍历，有点绕，仔细分析，或考虑使用非递归进行遍历，
    二、广度优先遍历
    又称层次遍历，即按照从上至下，从左至右的顺序遍历
    Tips：可使用队列的思想进行遍历
    '''


    # 一、深度优先遍历
    # 1.先序遍历（根->左->右）
    def pre_order(self, node):
        if node is not None:
            print(node.value, end=',')
            self.pre_order(node.left)
            self.pre_order(node.right)

    # 2.中序遍历（左->根->右）
    def mid_order(self, node):
        if node is not None:
            self.mid_order(node.left)
            print(node.value, end=',')
            self.mid_order(node.right)

    # 3.后序遍历（左->右->根）
    def pro_order(self, node):
        if node is not None:
            self.pro_order(node.left)
            self.pro_order(node.right)
            print(node.value)

    # 二、广度优先遍历(层次遍历)
    def level(self, node):
        res = []
        if node is not None:
            res.append(node)
        while len(res) != 0:
            if res[0].left is not None:
                res.append(res[0].left)
            if res[0].right is not None:
                res.append(res[0].right)
            print(res.pop(0).value, end=',')



if __name__ == '__main__':
    BSF = BinSearchTree()
    l = [15, 8, 17, 5, 9, 16, 31, 4, 7, 11, 28, 36, 23, 34]
    BSF.insert(l)

    # 测试二叉搜索树的查找
    # BSF.search(10)

    # 测试中序遍历
    print("*"*10, "测试二叉搜索树的中序遍历", "*"*10)
    print("二叉搜索树的中序遍历：" ,end=' ')
    BSF.mid_order(BSF.root)
    print('\n')

    # 测试层级序遍历
    print("*" * 10, "测试二叉搜索树的层级遍历", "*" * 10)
    print("二叉搜索树的层级遍历：", end=' ')
    BSF.level(BSF.root)
    print('\n')

    # 测试二叉搜索树的删除功能
    BSF.remove(15)
    # 中序遍历
    print("*" * 10, "测试二叉搜索树的中序遍历", "*" * 10)
    print("二叉搜索树的中序遍历：", end=' ')
    BSF.mid_order(BSF.root)
    print('\n')

    # 层级序遍历
    print("*" * 10, "测试二叉搜索树的层级遍历", "*" * 10)
    print("二叉搜索树的层级遍历：", end=' ')
    BSF.level(BSF.root)
    print('\n')
