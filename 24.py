# 读取输入数据
hamburger1 = int(input())  # 上德汉堡价格
hamburger2 = int(input())  # 中德汉堡价格
hamburger3 = int(input())  # 下德汉堡价格
drink1 = int(input())      # 可乐价格
drink2 = int(input())      # 雪碧价格

# 初始化最便宜的套餐价格为一个较大的值
min_price = float('inf')

# 遍历所有组合
prices = [
    hamburger1 + drink1 - 50,
    hamburger1 + drink2 - 50,
    hamburger2 + drink1 - 50,
    hamburger2 + drink2 - 50,
    hamburger3 + drink1 - 50,
    hamburger3 + drink2 - 50
]

# 找出最小值
min_price = min(prices)

# 输出结果
print(min_price)
