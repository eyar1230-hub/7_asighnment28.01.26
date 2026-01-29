#start

a: int = int(input('place a numb for a: '))
b: int = int(input('place a numb for b: '))
c: int = int(input('place a numb for c: '))
not_counted: int = 0

while True:
    if a > b and b > c:
        print('total incorrect inputted numbers=', not_counted)
        print('a > b=', a, '>', b, '| and: a > c=', a, '>', c)
        break
    else:
        a: int = int(input('place a numb for a: '))
        b: int = int(input('place a numb for b: '))
        c: int = int(input('place a numb for c: '))
        not_counted += 3
        continue
#stop