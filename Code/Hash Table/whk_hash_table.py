# *-* coding: utf8 *-* 
# @Time : 2021/3/13 20:40
# @Author : 危红康
# @File : whk_hash_table.py
# @Software: PyCharm


class HashTable(object):
    """哈希表类"""
    def __init__(self, capacity):
        self.capacity = capacity
        """
        当哈希表内的元素增加时，产生冲突的可能性增加，因此，需要设定一个载荷因子（一般设定为0.75），
        当α(=元素个数/表长)达到载荷因子时，需要重新定义表的长度，一般选择扩大到已插入元素数量的2倍，
        即size的两倍(2*size)，或者当前容量的1.5倍(capacity*1.5)
        """
        self.load_factor = 0.75
        self.size = 0
        self.hash_table = [(None, None) for _ in range(self.capacity)]

    def hash(self, x):
        return x % self.capacity

    def resize(self):
        """
        当哈希表内的元素增加时，产生冲突的可能性增加，因此，需要设定一个载荷因子（一般设定为0.75），
        当α(=元素个数/表长)达到载荷因子时，需要对表进行扩容，一般选择扩大到已插入元素数量的2倍，
        即size的两倍(2*size)，或者当前容量的1.5倍(capacity*1.5)
        原数组中的数据必须重新计算其在新数组中的位置之后，再放入新数组中
        """
        capacity_new = int(self.capacity*1.5)
        self.capacity = capacity_new
        hash_table_new = [(None, None) for _ in range(capacity_new)]

        for (key, value) in self.hash_table:
            if key is not None:
                hash_k = self.hash(key)
                if hash_table_new[hash_k][0] is None:
                    hash_table_new[hash_k] = (key, value)
                else:
                    for i in range(self.capacity):
                        hash_k = self.hash(key+i)
                        if hash_table_new[hash_k][0] is None:
                            hash_table_new[hash_k] = (key, value)
                            break
        self.hash_table = hash_table_new
        print("扩容函数被调用了......")         # 用于检测扩容函数被调用的次数

    def put(self, key, value):
        # 放置元素
        hash_k = self.hash(key)
        # 当存储数据与哈希表容量比大于载荷因子时，进行扩容
        if self.size/self.capacity > self.load_factor:
            self.resize()
        # 冲突处理
        if self.hash_table[hash_k][0] is None:
            self.hash_table[hash_k] = (key, value)
        else:
            for i in range(self.capacity):
                hash_k = self.hash(key + i)             # 线性探测
                if self.hash_table[hash_k][0] is None:
                    self.hash_table[hash_k] = (key, value)
                    break
        self.size += 1

    def get(self, key):
        # 获取元素值
        hash_k = self.hash(key)
        # 判断是否冲突，若冲突，则通过线性探测法（只要和前面放置元素的方法一致即可）寻找。
        h_key, h_value = self.hash_table[hash_k]
        if h_key == key:
            return h_value
        else:
            for i in range(self.capacity):
                hash_k = self.hash(key+i)
                h_key, h_value = self.hash_table[hash_k]
                if h_key == key:
                    return h_value
        return -1


if __name__ == "__main__":
    Dic = HashTable(capacity = 10)
    for i in range(23):
        Dic.put(i, "number {}".format(i))
    print(Dic.capacity)
    print(Dic.size)
    print(Dic.get(2))


