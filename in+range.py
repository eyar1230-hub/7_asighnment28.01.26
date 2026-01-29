#start
#קלוט lower
#לאחר קליטת lower קלוט higher בלולאת while True

lower: int = int(input('enter the lowest number- '))
i: int = 0

while True:
    higher: int = int(input('enter the highest number- '))
# אם higher קטן או שווה ל־lower – יש להמשיך לקלוט שוב 2 ערכים
    while lower >= higher:
        lower: int = int(input('enter the lowest number- '))
        higher: int = int(input('enter the highest number- '))
        continue
# כאשר higher גדול מ־lower – יוצאים מהלולאה ב break
    if lower > higher:
        break
    break
#הדפס את כל המספרים מ־lower עד higher (כולל) באמצעות for עם range
for lower in range(lower, higher + 1):
    print(lower, end='| ')

# stop