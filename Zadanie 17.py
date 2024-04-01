f = open('input.txt')
m = [int(i) for i in f]
mx = -999999
k = 0
z = 0
mx2 = -999999
for j in range(len(m)):
    if m[j] > mx and m[j] % 100 == 17:
        mx = m[j]
for i in range(len(m) - 2):
    a = m[i]
    b = m[i+1]
    c = m[i+2]
    if (a + b + c) > mx:
        if a % 5 == 0 or b % 5 == 0 or c % 5 == 0:
            n1 = len(str(a))
            n2 = len(str(b))
            n3 = len(str(c))
            if (n1 == 4 and n2 == 4) or (n1 == 4 and n3 == 4) or (n2 == 4 and n3 == 4):
                z += 1
                if a + b + c > mx2:
                    mx2 = a + b + c

print(z, mx2)
