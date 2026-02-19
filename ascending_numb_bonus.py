#start

a: int = int(input('place a numb for a: '))
b: int = int(input('place a numb for b: '))
c: int = int(input('place a numb for c: '))
#print 3 ascending numbers in order low to high.
while True:
    if b == c or a == b or c == a:
        a: int = int(input('place a numb for a: '))
        b: int = int(input('place a numb for b: '))
        c: int = int(input('place a numb for c: '))
        break
# print a is the largest
    if a > b > c:
        break
    if a > c > b:
        b, c = c, b
        break
# print b is the largest
    if b > a > c:
        a, b, c = b, a, c
        break
    if b > c > a:
        a, b, c = b, c, a
        break
# print c is the largest
    if c > b > a:
        a, c = c, a
        break
    if c > a > b:
        a, b, c = c, a, b
        break
print(c, b, a)

#stop