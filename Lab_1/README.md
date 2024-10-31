# Звіт до першої лабораторної
## Тема: перша програма на мові *Python*



+ 1.Фотозовіт першої програми [фото](img1.png)
+ 2.фотозвіт доповнений [картинка](img2.png)



___


```python
from datetime import date

today = date.today()
day_of_week = today.weekday()

if day_of_week >= 5:
    status = "Сьогодні вихідний!"
else:
    status = "Сьогодні робочий день."

print(f"{today}: {status}")

```