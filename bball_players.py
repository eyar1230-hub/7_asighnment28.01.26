#start
#בצע לולאה כדי לנסות לקלוט 10 גילאים
bellow16: int = 0
above16: int = 0

for _ in range (1, 10 + 1):
    age: int = int(input('age of player: '))
    if age < 12:
        print('to young')
        continue
    if age > 18:
        print('to old - will be disqualified')
        age: int = int(input('age of player: '))
        break
    bellow16 += 1
    if age >= 16:
        above16 += 1
        continue

print('validplayers count:')
print('12 untill 16:', bellow16, '16 and above:',  above16)

#stop