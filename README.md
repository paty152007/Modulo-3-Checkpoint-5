# CONCEPTOS BÁSICOS DE PYTHON

Este documento recoge algunos conceptos fundamentales de Python explicados de forma sencilla para personas que están empezando en programación.

## Índice

1. [¿Qué es un condicional?](#qué-es-un-condicional)
2. [Tipos de bucles en Python](#cuáles-son-los-diferentes-tipos-de-bucles-en-python-por-qué-son-útiles)
3. [Lista por comprensión](#qué-es-una-lista-por-comprensión-en-python)
4. [¿Qué es un argumento en Python?](#qué-es-un-argumento-en-python)
5. [Funciones Lambda](#qué-es-una-función-lambda-en-python)
6. [¿Qué es un paquete pip?](#qué-es-un-paquete-pip)

## ¿Qué es un condicional?

Un condicional en programación es una estructura que permite que un bloque de código se ejecute si se cumple una condición. 

Si la condición es verdadera, se ejecuta ese bloque de código. Si no se cumple, podemos especificar otro bloque de código que se ejecutará en su lugar. 

Además, es posible indicar varias condiciones diferentes para ejecutar distintos bloques de código dependiendo del resultado. 

Los condicionales se utilizan para que un programa pueda tomar decisiones dependiendo de diferentes situaciones. 

### Sintaxis

```python
if condicion:
    # código a ejecutar si la condición es verdadera
elif otra_condicion:
    # código si se cumple esta otra condición
else:
    # código si ninguna condición anterior se cumple
```

### Ejemplo

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

En este ejemplo, el programa comprueba si la edad es mayor o igual a 18. 


Si la condición se cumple, el programa imprime **_"Eres mayor de edad"_**. 


Si la condición no se cumple, se ejecuta el código de 'else', por lo que imprimiría **_"Eres menor de edad"_**. 

## ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Los principales tipos de bucles en Python son `for` y `while`. 

Estos bucles permiten repetir bloques de código de forma eficiente. 

Se utilizan principalmente para automatizar tareas repetitivas o trabajar con conjuntos de datos. 

El bucle `for` se utiliza para iterar sobre una secuencia (como una lista, un string o un rango de números) por lo que se puede entender como un "bucle definido". 

Por otro lado, `while` repite un bloque de código mientras una condición sea **verdadera**. 

### Sintaxis

```python
for iterator in iterable:
    # bloque de código 

while condicion:
    # bloque de código
```

### Ejemplo

#### Ejemplo de bucle `for`

```python
frutas = ['kiwi', 'mango', 'cereza']
for fruta in frutas:
    print(fruta)
```
Este bucle recorre la lista **frutas** e imprime cada elemento. 

#### Ejemplo de bucle `while`

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```
En este ejemplo, el bucle se ejecuta mientras `contador` sea menor que 5. Cuando la condición deja de cumplirse el bucle se detiene. 

## ¿Qué es una lista por comprensión en Python?

Una lista por comprensión es una forma de crear listas en Python utilizando una sintaxis más corta y compacta basada en bucles. 

Gracias a esta forma de crear listas, es posible reducir varias líneas de código a una sola, además de expresar la intención de la creación de la lista de forma más clara. 

### Sintaxis

```python
nueva_lista = [expresion for elemento in iterable]
```
### Ejemplo

```python
numeros = [x for x in range(5)]
print(numeros)
```
Este código crea una lista con los números del 0 al 4 utilizando una lista por comprensión. 

Si no utilizásemos una lista por comprensión, tendríamos que hacerlo de la siguiente manera:

```python
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)
```
El resultado es el mismo, pero utilizando una lista por comprensión podemos simplificar un bloque de código de varias líneas en una sola.  

## ¿Qué es un argumento en Python?

Un argumento en Python es el valor que se pasa a una función cuando se la llama. 
Por así decirlo, son los valores con los que estamos proporcionando información a la función para que pueda ejecutar su bloque de código. 

### Sintaxis

```python
funcion(argumento)
```
### Ejemplo

```python
def saludar(nombre):
    print("Hola", nombre) 

saludar("Patricia")
```
En este ejemplo, "Patricia" es el **argumento** que se pasa a la función **saludar**. 
La función recibe ese valor y lo utiliza dentro de su bloque de código. 

## ¿Qué es una función Lambda en Python?

Las expresiones lambda son una forma corta de declarar funciones en Python. 
Se trata de funciones anónimas (es decir, funciones que no tienen nombre) que se pueden definir en una sola línea utilizando la palabra clave **lambda**.

Son ideales cuando necesitamos realizar operaciones simples de forma rápida y concisa. 

### Sintaxis

```python
lambda argumentos: expresion
```

### Ejemplo

```python
suma = lambda a, b: a + b

print(suma(3, 5))
```
En este ejemplo se crea una función lambda que suma dos números. 
Los valores 3 y 5 se pasan como argumentos y la función devuelve su suma. 

## ¿Qué es un paquete pip?

Un paquete de Python es una colección de librerías o módulos de código preescrito que se pueden instalar, actualizar y eliminar fácilmente utilizando la herramienta de gestión de paquetes `pip`. 

Estas librerías de código las obtienes fácilmente del repositorio oficial [PyPI (Python Package Index)](https://pypi.org) En las versiones más recientes de Python 'pip' viene instalado por defecto. 

### Ejemplo

Para instalar un paquete utilizando `pip`, abre la terminal y ejecuta:

```bash
pip install nombre_del_paquete
```