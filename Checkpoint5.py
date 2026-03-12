# Ejercicio 1: Cree un bucle For de Python.
frutas = ['kiwi', 'mango', 'cereza']
for fruta in frutas:
    print(fruta)

# Ejercicio 2: Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
def suma(num1, num2, num3):
    return num1 + num2 + num3

print(suma(1,1,1))

# Ejercicio 3: Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
suma_lambda = lambda num1, num2, num3: num1 + num2 + num3

print(suma_lambda(1,1,2))

# Ejercicio 4: Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
nombre = 'Enrique'

lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

if nombre in lista_nombre:
    print('Esta en la lista')
else:
    print('No esta en la lista')
    

