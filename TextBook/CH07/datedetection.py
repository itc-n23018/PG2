import re
from datetime import datetime

# 正規表現パターン
date_pattern = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(1[0-9]{3}|2[0-9]{3})\b'

# テスト用の文字列
test_strings = [
    "Today's date is 15/08/2021.",
    "The event is on 31/12/2999.",
    "Invalid dates: 31/02/2020, 31/04/2021, 32/01/2021, 00/10/2020, 29/13/2022, 15/08/999.",
    "The date is 05/07/1985."
]

def is_valid_date(day, month, year):
    try:
        datetime(year, month, day)
    except ValueError:
        return False
    return True

# 日付を検出し、検証する
for s in test_strings:
    matches = re.findall(date_pattern, s)
    if matches:
        for match in matches:
            day, month, year = map(int, match)
            if is_valid_date(day, month, year):
                print(f"Valid date found: {day:02d}/{month:02d}/{year}")
            else:
                print(f"Invalid date found: {day:02d}/{month:02d}/{year}")
    else:
        print(f"No valid dates found in '{s}'")

