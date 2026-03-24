n = int(input())
original = n
count = 0

while True:
    # 拆分十位和个位
    a = n // 10
    b = n % 10
    # 计算新数字
    n = b * 10 + (a + b) % 10
    count += 1
    # 回到原数则终止循环
    if n == original:
        break

print(count)
