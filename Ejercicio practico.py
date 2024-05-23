# Cree un bucle For de Python.
for town in ["Paris", "Albacete","Oñati"] :
    print(f'El participante es de {town}')

# Cree una función de Python llamada suma que tome 3 argumentos y 
#devuelva la suma de los 3.
def suma(arg1,arg2,arg3):
    return arg1+arg2+arg3

# Cree una función lambda con la misma funcionalidad que la función de suma 
# que acaba de crear.
suma_total = lambda arg1,arg2,arg3 : arg1+arg2+arg3
print(suma_total(1,1,1))

# Utilizando la siguiente lista y variable, determine si el valor de la variable 
#coincide o no con un valor de la lista. 
#*Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

# Opcion 1: utulizar if-else y comparar directamente
if nombre in lista_nombre:
    print("El nombre está en la lista")
else:
    print("El nombre está en la lista")

# Opcion 2: utilizar for-else y comparar los nombres uno a uno
for nomb in lista_nombre :
    if nombre == nomb :
        print(f"El nombre {nomb} aparece en la lista")
        break
else:
    print(f'El nombre {nomb} no está en la lista')
