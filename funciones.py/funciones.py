# Ejemplo

"""
Ya queda definido el valor de la funcion



def muestra_nombre ():
    print ("Max")
    print("Jesus")

muestra_nombre()


"""

# Ejemplo 2


"""
Se puede cambiar el valor de la funcion con la variable


nombre = "Alejandro"
def muestra_nombre2 ():
    print(f"Mi nombre es {nombre}")

muestra_nombre2()

"""


# Ejemplo 3


"""
Los valores se pueden cambiar mediante los parametros



def muestrar_nombre3 (nombre1, rut, saludo):
    print(f"Tu nombre es : {nombre1} {rut} {saludo}")

muestrar_nombre3("Maximiliano", 266, "Holaa")
muestrar_nombre3("Jesus", 26336, "Habla")


"""


# Ejemplo 4

def muestra_nombre4 (nombre2):
    print(f"Tu nombre es : {nombre2}")

nombre2 = input("Ingrese su nombre")
muestra_nombre4(nombre2)