# 处理3次投掷
for _ in range(3):
    # 读取一行输入
    a, b, c, d = map(int, input().split())
    # 统计正面(1)的数量
    cnt = a + b + c + d
    # 根据正面数量映射结果
    if cnt == 3:
        print("A")    # 1个背面(0)，3个正面(1) → 도
    elif cnt == 2:
        print("B")    # 2个背面(0)，2个正面(1) → 개
    elif cnt == 1:
        print("C")    # 3个背面(0)，1个正面(1) → 걸
    elif cnt == 0:
        print("D")    # 4个背面(0) → 윷
    else:             # cnt == 4
        print("E")    # 4个正面(1) → 모
