#start
#בצע לולאה כדי לנסות לקלוט 10 גילאים
BOLD_RED = "\033[1;31m"
age: int = int(input('age of player: '))
count: int = 1
midage: int = 1
while True:
    if age < 12:
        print('to young')
        age: int = int(input('age of player: '))
        continue
    if age >= 18:
        break
    if age >= 16 and count < 10:
        midage += 1
        count += 1
        age: int = int(input('age of player: '))
        continue
    if count < 4:
        age: int = int(input('age of player: '))
        count+=1
        continue
    else:
        print('validplayers count:')
        print('12 untill 16:', count - midage,'16 and above:',  midage)
        break

#stop