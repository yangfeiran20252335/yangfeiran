# 비윤년 각 월 일수
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 1월 1일은 목요일 (인덱스 3: 일=0, 월=1, 화=2, 수=3, 목=4, 금=5, 토=6)
weekdays = ["일", "월", "화", "수", "목", "금", "토"]

month = int(input("월을 입력하세요 (1-12): "))

# 대상 월 1일의 요일 계산
total_days = sum(days_in_month[:month-1])
first_weekday = (3 + total_days) % 7  # 3은 1월 1일의 요일 인덱스

# 헤더 출력
print(f"        {month}월")
print(" ".join(f"{day:2s}" for day in weekdays))

# 선행 공백 출력
print(" " * (first_weekday * 3), end="")

# 날짜 출력
for day in range(1, days_in_month[month-1] + 1):
    print(f"{day:2d}", end=" ")
    if (first_weekday + day) % 7 == 0:
        print()
