# 读取输入
h, m, s = map(int, input().split())
d = int(input())

# 计算总秒数
total = h * 3600 + m * 60 + s + d

# 换算回时分秒
end_h = (total // 3600) % 24
end_m = (total % 3600) // 60
end_s = total % 60

# 输出结果
print(end_h, end_m, end_s)
