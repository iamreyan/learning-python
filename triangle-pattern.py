t = 6
d = '$'
space = ' '
for y in range(6):
    print(d*y)

for y in range(6,0,-1):
    print(d*y)

for y in range(5):
    s = t - y
    print(s*space,end='')
    print(d*y)
    print(s+d)



