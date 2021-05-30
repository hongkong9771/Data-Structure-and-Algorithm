# *-* coding: utf8 *-* 
# @Time : 2021/3/14 20:57
# @Author : 危红康
# @File : whk_sort.py
# @Software: PyCharm


class Sort(object):
    """
    十个经典的排序算法
    1.冒泡排序（Bubble Sort）
    2.选择排序（Selection Sort）
    3.插入排序（Insertion Sort）
    4.希尔排序（Shell Sort）
    5.归并排序（Merge Sort）
    6.快速排序（Quick Sort）
    7.堆排序（Heap Sort）
    8.计数排序（Counting Sort）
    9.桶排序（Bucket Sort）
    10.基数排序（Radix Sort）
    """
    def Bubble_Sort(self, nums):
        """
        1.冒泡排序
        每次排序之后，最大数会达到序列尾部，小的数会慢慢地向序列头部挪动
        """
        n = len(nums)
        for i in range(n):
            for j in range(1, n-i):         # i可以表示为遍历次数，j表示从头遍历到n-i，因为经历过i次遍历之后，序列尾部的i个值已经被排好序了（放置着最大的值）
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        return nums

    def Selection_Sort(self, nums):
        """
        2.选择排序
        从未排序的序列当中找到最小（大）的元素，并将其与序列头（尾）部元素进行调换，经过一次选择排序后的序列，
        头（尾）部第1个元素已被排列好，之后再从剩下未经排序的序列当中继续找最小（大）的元素，并与当前未排序序列的头（尾）部元素进行调换
        """
        n = len(nums)
        for i in range(n):
            temp = i
            for j in range(i, n):           # 设置下标temp的初始值为i，j从i开始一直往后挪动，当遇到比nums[temp]还小的值时,将temp的值更新为j。
                if nums[temp] > nums[j]:
                    temp = j
            nums[i], nums[temp] = nums[temp], nums[i]
        return nums

    def Insertion_Sort(self, nums):
        """
        3.插入排序
        默认第1位元素已经排好序，接着从第2位开始在已排好序的序列中，从后往前扫描，找到相应位置并插入，以此类推。
        """
        n = len(nums)
        for i in range(n-1):
            j = i + 1
            while j > 0 and nums[j] < nums[j-1]:        # 第i+1个元素在已排好序的序列（0~i）中从后往前扫描，找到相应位置并插入。
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
        return nums

    def Shell_Sort(self, nums):
        """
        4.希尔排序
        又称缩小增量排序，以gap为增量，将序列以gap为间隔分成n//gap个序列，对n//gap个序列分别进行插入排序，
        之后将gap缩小至gap//2，再次进行分割序列和排序操作，直至gap为0
        """
        n = len(nums)
        gap = n // 2
        while gap:      # while循环的时间复杂度为log2n
            for j in range(0, gap):             # 用于遍历以gap为间隙的组数，一共gap组，需遍历gap次
                for i in range(j, n, gap):      # 以gap为间隙，遍历每组，使用插入排序法进行排序，共需遍历n/gap次，结合上一个for循环，两个for循环的时间复杂度为O(n)
                    while i >= gap and nums[i - gap] > nums[i]:
                        nums[i - gap], nums[i] = nums[i], nums[i - gap]
                        i -= gap
            gap //= 2
        return nums

    def Merge_Sort(self, nums):
        """
        5.归并排序

        """


if __name__ == "__main__":
    nums = [23, 56, 3, 34, 12, 1, 13]
    # nums = [1]
    s = Sort()
    print("原始数组：",nums)
    # 冒泡排序
    # nums_bubble_sort = s.Bubble_Sort(nums)
    # print("冒泡排序后的数组：", nums_bubble_sort)

    # 选择排序
    # nums_selection_sort = s.Selection_Sort(nums)
    # print("选择排序后的数组：", nums_selection_sort)

    # 插入排序
    # nums_insertion_sort = s.Insertion_Sort(nums)
    # print("插入排序后的数组：", nums_insertion_sort)

    # 希尔排序
    nums_shell_sort = s.Shell_Sort(nums)
    print("希尔排序后的数组", nums_shell_sort)
