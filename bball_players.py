#start
#בצע לולאה כדי לנסות לקלוט 10 גילאים
age: int = int(input('age of player: '))
count: int = 1
midage: int = 1
while True:
    age: int = int(input('age of player: '))
    if age < 12:
        print('to young')
        continue
    if age > 18:
        print('to old - will be disqualified')
        age: int = int(input('age of player: '))
        break
    if age >= 16 and count < 10:
        midage += 1
        count += 1
        age: int = int(input('age of player: '))
        continue
    if count < 10:
        age: int = int(input('age of player: '))
        count+=1
        continue
    else:
        print('validplayers count:')
        print('12 untill 16:', count - midage,'16 and above:',  midage)
        break

#stop