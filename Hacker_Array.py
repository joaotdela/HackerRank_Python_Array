
arry = []
n = 0
for n in range(0, 100):
    n += 1
    N = int(input('Escolha o valor de N:'))
    if N == 1:
        i = input('Escolha o valor de i:')
        e = input('Escolha o valor de e1:')
        arry.insert(int(i), int(e))
        print(arry)
    elif N == 2:
        print(arry)
    elif N == 3:
        arry.remove(int(e))
        print(arry)
    elif N == 4:
        e = input('Escolha o valor de e:')
        arry.append(int(e))
    elif N == 5:
        arry.sort()
        print(arry)
    elif N == 6:
        arry.pop()
    elif N == 7:
        arry.reverse()
        print(arry)
    else:
        break
