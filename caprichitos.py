 #print ("Hola wilifrido")

#cantante = "Tito rojas"
#if cantante  == "El Allllffaaa" :           # Los for son condicionaels que se adpatan a elementos que sean de iteracion (lista, rango, etc)

 #   print ("El mas duro del dembow latinooo")
#else :
 #   print (f"{cantante}")

""""
contador = 0 
for contador in range (0,5) :                #contador del 0-4 
    print ("voy por el " +str(contador))

"""





"""
print(" Tabla de multiplicar ")

numero_usuario = int(input("De que numero es esta tabla"))
if numero_usuario <= 1:
    numero_usuario = 1
 
print (f"#Tabla de multiplicar del numero {numero_usuario}")

for numero_tabla in range(1,11):
    print (f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print("Tabla finalizada")
"""





"""
contador = 1
while contador <=100:
    print (f"Hoy mate {contador} mancos en el fornite")
    contador = contador+1

"""





"""
print(" Tabla de multiplicar ")

numero_usuario = int(input("De que numero es esta tabla"))
if numero_usuario <= 1:
    numero_usuario = 1
 
print (f"#Tabla de multiplicar del numero {numero_usuario}")      # La misma tabla de multiplicar pero con el metodo while

contador = 1
while contador <=10:
    print (f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    contador +=1
else: 
     print("tabla terminada")

"""





"""
print ("Promedio de los favoritos")

primera_nota = int(input("Ingrese la primera nota"))
segunda_nota = int(input("Ingrese la Segunda nota"))
tercera_nota = int(input("Ingrese la tercera nota"))

nota = primera_nota+segunda_nota+tercera_nota 
nota_final = nota / 3

if nota_final >= 4:
    if nota_final >=7:
        print ("Un lince")
    else:
        print("Pasaste de vaina")
else:
    print("Reprobado")

"""





"""
print (" ####  Numero mayor entre 3  ####")


primer_numero = int(input("Ingrese el primer numero"))
segundo_numero = int(input("Ingrese el segundo numero"))
tercer_numero = int(input("Ingrese el tercer numero"))
if primer_numero > segundo_numero and primer_numero > tercer_numero:
    print (f" EL primer numero = {primer_numero} es mayor a los otros dos")
else:
    print(f"El primer numero = {primer_numero} no es el mayor")
if segundo_numero > primer_numero and segundo_numero > tercer_numero:
    print (f" EL segundo numero = {segundo_numero} es mayor a los otros dos")
else:
    print(f"El segundo numero = {segundo_numero} no es el mayor")
if tercer_numero > segundo_numero and tercer_numero > primer_numero:
    print (f" EL tercer numero = {tercer_numero} es mayor a los otros dos")
else:
    print(f"El tercer numero = {tercer_numero} no es el mayor")
"""





"""
print(" ### Numero mayor entre 3  ###")

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))

if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3


print("El número mayor es:", mayor)
"""




"""
numeros = [int(input("Ingrese el primer número entero: ")), 
           int(input("Ingrese el segundo número entero: ")), 
           int(input("Ingrese el tercer número entero: "))]


mayor = max(numeros)

print("El número mayor es:", mayor)
"""



"""
print(" ###   Indicar si es del primer trimestre del año   ###")
dia = int(input("Ingrese el dia: ")), 
mes = int(input("Ingrese el numero del mes ")), 
año = int(input("Ingrese el año "))

if mes==1 or mes==2 or mes==3:
    print("Pertenece al primer trimestre")
else:
    print("No pertenece")

"""

