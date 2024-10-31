from datetime import date

today = date.today()
day_of_week = today.weekday()

if day_of_week >= 5:
    status = "Сьогодні вихідний!"
else:
    status = "Сьогодні робочий день."

print(f"{today}: {status}")