def validnumero():
    while True:
            n = (input('Ingresa el nombre elegido: ').upper())
            if n == "GABRIEL": 
                break
            else:
                print('Debe ingresar un valor numerico entero o decimal'.upper)
                continue
       
    return n

num=validnumero()
print(num.capitalize())



def validnumero2():
    while True:
        try:
            n = float(input('Ingresa un número entero o decimal: '))
        except ValueError:
            print('Debe ingresar un valor numerico entero o decimal')
            continue
        break
    return n
print("ad")




