# -*- coding:utf-8 -*- 
# @Time : 2021/7/21 17:19
# @Author : 危红康
# @File : 完全背包.py
# @Software: PyCharm

"""
题目描述：背包容量为bag_weight，从以下物品中取相应的物品，使得总价值最大，每个物品可以重复选取。
物品种类及价值：
                        重量          价值
            物品0         1           5
            物品1         2           20
            物品2         3           40

"""


def complete_pack_1(weights, values, bag_weight):
    """
    二维数组，注意一个物品可以重复使用，所以在dp赋值时，代码块为：
    dp[i][j] = max(dp[i - 1][j], dp[i][j - weights[i]] + values[i])
    """
    l = len(weights)
    dp = [[0] * (bag_weight + 1) for _ in range(l)]

    # 初始化动态数组
    if weights[0] <= bag_weight:
        for i in range(weights[0], bag_weight + 1):
            dp[0][i] = max(dp[0][i], dp[0][i - weights[0]] + values[0])

    # 动态传递过程
    for i in range(1, l):
        for j in range(1, bag_weight+1):
            if weights[i] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i][j-weights[i]] + values[i])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[l-1][bag_weight]


def complete_pack_2(weights, values, bag_weight):
    """
        一维数组，注意一个物品可以重复使用，所以在dp赋值时，
        只与它的上一个以及它前面赋完值的有关，则应该从前往后遍历。
        dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
    """
    l = len(weights)

    dp = [0] * (bag_weight + 1)

    for i in range(l):
        for j in range(1, bag_weight+1):
            if weights[i] <= j:
                dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
            else:
                dp[j] = dp[j]
    return dp[bag_weight]


weights = [1, 2, 3]
values = [5, 20, 40]
bag_weight = 4

res2 = complete_pack_1(weights, values, bag_weight)
res1 = complete_pack_2(weights, values, bag_weight)

print(res1)
print(res2)
