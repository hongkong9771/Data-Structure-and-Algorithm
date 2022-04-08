# -*- coding:utf-8 -*- 
# @Time : 2021/7/22 17:03
# @Author : 危红康
# @File : 爬楼梯进阶版.py
# @Software: PyCharm


"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
"""


class Solution:
    def climbStairs_1(self, n: int) -> int:
        """
        此题可以理解成完全背包：
        每次爬的1个或2个台阶可以看成是物品的总类，共n阶楼梯可以看成是背包的总容量。
        因为每次都可以选择爬1阶或2阶楼梯，此外，1个或2个台阶是可以重复使用的，因此是完全背包。
        每次爬1个或者2个台阶的顺序不一样，也被称作不同的方法，因此为排列。所以需要先遍历背包，再遍历物品种类。
        """
        nums = [1, 2]
        dp = [0] * (n + 1)

        # 初始化动态数组
        dp[0] = 1

        # 动态传递
        for j in range(1, n+1):
            for i in range(2):
                if nums[i] <= j:
                    dp[j] = dp[j] + dp[j - nums[i]]
                else:   # 此块代码可以省略，加上只是为了保证代码的完整性
                    dp[j] = dp[j]
        return dp[n]

    def climbStairs_2(self, n, m):
        """
        此题可以理解成完全背包：
        每次爬的1个、2个...m个台阶可以看成是物品的总类，共n阶楼梯可以看成是背包的总容量。
        因为每次都可以选择爬1阶、2阶...m阶楼梯，此外，1阶、2阶...m阶楼梯是可以重复使用的，因此是完全背包。
        每次爬1个或者2个台阶的顺序不一样，也被称作不同的方法，因此为排列。所以需要先遍历背包，再遍历物品种类。
        """
        nums = [i for i in range(1, m+1)]
        dp = [0] * (n + 1)

        # 初始化动态数组
        dp[0] = 1

        # 动态传递
        for j in range(1, n+1):
            for i in range(len(nums)):
                if nums[i] <= j:
                    dp[j] = dp[j] + dp[j - nums[i]]
                else:   # 此块代码可以省略，加上只是为了保证代码的完整性
                    dp[j] = dp[j]
        return dp[n]


n = 15
m = 3
s = Solution()

res_1 = s.climbStairs_1(n)
print(res_1)

res_2 = s.climbStairs_2(n, m)
print(res_2)

