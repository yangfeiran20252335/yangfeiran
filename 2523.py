n = int(input())
for i in range(1, 2 * n):
    star_count = n - abs(n - i)
    print('*' * star_count)
