# -*- coding:utf-8 -*- 
# @Time : 2021/7/22 17:18
# @Author : 危红康
# @File : 多重背包.py
# @Software: PyCharm


"""
题目描述：背包容量为bag_weight，从以下物品中取相应的物品，使得总价值最大，每个物品可以选取的次数有限。
物品种类及价值：
                        重量          价值          数量
            物品0         1           5             2
            物品1         2           20            3
            物品2         3           40            4
"""


def multi_pack1(weights, values, bag_weight, nums):
    """
        二维数组，注意一个物品可以重复使用的次数有限，因此，可以考虑将物品乘以其数量，得到新的物品清单，这样就还是01背包的问题
        所以在dp赋值时，代码块为：
        dp[i][j] = max(dp[i - 1][j], dp[i-1][j - weights[i]] + values[i])
    """
    # 更新weights和values，变为01背包问题
    for i in range(len(nums)):
        while nums[i] > 1:
            weights.append(weights[i])
            values.append(values[i])
            nums[i] -= 1
    l = len(weights)
    dp = [[0] * (bag_weight + 1) for _ in range(l)]

    # 初始化动态数组
    if weights[0] <= bag_weight:
        for j in range(weights[0], bag_weight+1):
            dp[0][j] = values[0]

    # 动态传递
    for i in range(1, l):     # 先遍历物品
        for j in range(1, bag_weight + 1):  # 再遍历背包容量
            if weights[i] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[l-1][bag_weight]


def multi_pack2(weights, values, bag_weight, nums):
    """
    一维数组
    """
    # 更新weights和values，变为01背包问题
    for i in range(len(nums)):
        while nums[i] > 1:
            weights.append(weights[i])
            values.append(values[i])
            nums[i] -= 1
    l = len(weights)
    dp = [0] * (bag_weight + 1)
    # 初始化动态数组
    if weights[0] <= bag_weight:
        for i in range(weights[0], bag_weight+1):
            dp[i] = values[0]

    # 动态传递
    for i in range(1, l):       # 先遍历物品
        for j in range(bag_weight, weights[i] - 1, -1):     # 再遍历背包容量
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[bag_weight]


weights = [1, 2, 3]
values = [5, 20, 40]
bag_weight = 4
nums = [2, 3, 4]

res_1 = multi_pack1(weights, values, bag_weight, nums)
print(res_1)

res_2 = multi_pack2(weights, values, bag_weight, nums)
print(res_2)




