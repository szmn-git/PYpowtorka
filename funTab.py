
def counting(lista):
    avg = sum(lista)/len(lista)
    var = 0
    for i in lista:
        var = var + pow(i-avg,2)/len(lista)
    return (avg,var)

def adding(lista):
    print("podaj liczbe albo napisz 'stop' zeby przestac")
    while True:
        number = input()
        if number == 'stop':
            break
        try:
            lista.append(int(number))
        except ValueError:
            print('Podaj liczbe albo stop')
    return lista
