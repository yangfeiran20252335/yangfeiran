today = 0
days = 100000000
result_day = (today + days) % 7
weekdays = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
print(f"{days}일 후는 {weekdays[result_day]}입니다.")
