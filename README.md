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

Un condicional en programación es una estructura que permite que un bloque de código se ejecute si se cumple una condición. Por así decirlo, permite que un programa tome decisiones dependiendo de diferentes situaciones. 

Se puede comparar con situaciones de la vida cotidiana, en las que hacemos una acción dependiendo de lo que ocurra. 

Por ejemplo:

- Si llueve, llevo paraguas
- Si tengo hambre, como algo
- Si hace frío, me pongo un abrigo

En programación funciona de forma parecida: dependiendo de si una condición es verdadera (`True`) o falsa (`False`), el programa ejecutará una acción u otra. 

Si la condición es verdadera, se ejecuta un bloque de código. Si no se cumple, podemos especificar otro bloque de código que se ejecutará en su lugar. 

Por ejemplo:
```python
edad >= 18
```
Si `edad` es 20, el resultado será `True`.
Si `edad` es 15, el resultado será `False`.

Además, es posible evaluar varias condiciones diferentes para ejecutar distintos bloques de código según el resultado.

Por ejemplo: 
Si llueve, llevo paraguas.
Si además hace frio, también llevo un abrigo.

Los condicionales se utilizan cuando queremos que un programa tome decisiones dependiendo de diferentes situaciones. 

Por ejemplo, podemos utilizarlos para:

- Comprobar si un usuario tiene edad suficiente para acceder a un contenido
- Verificar si una contraseña es correcta
- Decidir movimientos en un juego 

Para crear condiciones en Python se utilizan **operadores de comparación**, que permiten comparar valores. 

| Operador | Significado       |
|----------|-------------------|
| `==`     | Igual que         |
| `!=`     | Distinto de       |
| `>`      | Mayor que         |
| `<`      | Menor que         |
| `>=`     | Mayor o igual que |
| `<=`     | Menor o igual que |

### Sintaxis

```python
if condicion:
    # código a ejecutar si la condición es verdadera
elif otra_condicion:
    # código si se cumple esta otra condición
else:
    # código si ninguna condición anterior se cumple
```
- `if` inicia la condición principal
- `elif` permite añadir condiciones adicionales
- `else` se ejecuta cuando ninguna condición anterior se cumple 

### Ejemplo

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

En este ejemplo, el programa comprueba si la variable `edad` es mayor o igual a 18. 

Si la condición se cumple, el programa ejecuta el primer bloque de código e imprime **_"Eres mayor de edad"_**. 

Si la condición no se cumple, se ejecuta el código de `else`, mostrando el mensaje **_"Eres menor de edad"_**. 

De esta forma, el programa puede tomar decisiones dependiendo del valor de una variable. 

Es importante tener en cuenta que Python evalúa las condiciones de arriba hacia abajo. Cuando encuentra una condición verdadera, ejecuta ese bloque de código y no evalúa las siguientes.

### Ejemplo con varias condiciones
También es posible evaluar varias condiciones utilizando `elif`.

```python
nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

En este ejemplo, podemos ver como el programa evalúa diferentes rangos de notas y muestra un mensaje distinto dependiendo de la nota obtenida por el alumno.

## ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Los bucles en Python son herramientas que permiten repetir acciones sin escribir lo mismo muchas veces. 

Por ejemplo:
Si quieres escribir "Hola" 5 veces podrías escribirlo 5 veces o podrías usar un bucle. Dando una sola instrucción al programa, Python la repite las veces que necesites. 

Los principales tipos de bucles en Python son `for` y `while`. 

Se utilizan principalmente para automatizar tareas repetitivas, trabajar con listas de datos, ahorrar mucho código y crear programas inteligentes. 

Nos sirven para por ejemplo:
- Revisar 10000 contraseñas
- Procesar muchos archivos
- Analizar datos de un juego o app. 

Todo con un solo bucle, sin tener que duplicar código o repetirlo muchas veces. 

### `for`
El bucle `for` se utiliza cuando queremos recorrer una colección de datos (como listas, strings o rangos de números) o cuando sabemos cuántas veces queremos repetir una acción.  

Por ejemplo:
```python
for i in range(5):
    print("Hola")
```
- `range(5)` crea números del 0 al 4. 
- El bucle se repite 5 veces y cada vez imprime "Hola" sin tener que escribirlo manualmente. 

Sirve para recorrer listas de cosas, repetir algo cierto numero de veces o procesar datos uno por uno. 

### Sintaxis `for`

```python
for iterator in iterable:
    # bloque de código
```

#### Ejemplo de bucle `for`

```python
frutas = ['kiwi', 'mango', 'cereza']
for fruta in frutas:
    print(fruta)
```
Este bucle recorre la lista `frutas` e imprime cada una de las `frutas`

### `while`

Por otro lado, `while` repite un bloque de código mientras una condición sea **verdadera**. No siempre sabemos cuántas veces se va a repetir, pero sí sabemos cuál es la condicion que debe cumplirse para que el bucle continúe ejecutándose.  

### Sintaxis `while`

```python
while condicion:
    # bloque de código
```

#### Ejemplo de bucle `while`

```python
contador = 0
while contador < 5:
    print("Hola")
    contador += 1
```
En este ejemplo, el bucle se ejecuta mientras `contador` sea menor que 5. Cuando `contador`deja de cumplir la condición (`contador`ya no es menor que 5), el bucle se detiene. 

El resultado es el mismo que el ejemplo anterior, se imprime Hola 5 veces pero partiamos de un punto diferente, no indicamos directamente el número de repeticiones, sino la condición que debe cumplirse para que el bucle siga ejecutándose. 

### Control de bucles

Tenemos formas de controlar los bucles, para ello usamos `break` y `continue`. 

`break`nos sirve para detener el bucle. 

```python
for numero in range(10):
    if numero == 5:
        break
    print (numero)
```
- `range` crea números del 0 al 9.
- `if` comprueba si el número es igual a 5.
- Cuando esto ocurre, `break` detiene el bucle inmediatamente.
- Al detener el bucle solo nos va a imprimir los números del 0 al 4. 

`continue` nos permite saltarnos una vuelta. 

```python
for numero in range(5):
    if numero == 2:
        continue
    print(numero)
```
- `range` crea números del 0 a 4.
- `if` comprueba si el número es 2. 
- Cuando ocurre, `continue`hace que el bucle salte esa vuelta y pase directamente a la siguiente. 
- Imprimiría los números de 0 a 4 pero saltando el 2. 

En resumen, tanto `for`como `while`nos permiten repetir código pero se utilizan de forma diferente:
- `for`: cuando queremos recorrer una colección de datos o repetir algo un número determinado de veces. 
- `while`: cuando queremos repetir algo mientras se cumpla una condición. 

## ¿Qué es una lista por comprensión en Python?

Una lista por comprensión es una forma de crear listas en Python utilizando una sintaxis más corta y compacta que reemplaza muchos bucles `for` tradicionales.  

Gracias a esta forma de crear listas en lugar de escribir varias líneas con un bucle, puedes hacerlo en una sola línea de código.

Es importante tener en cuenta que una lista por comprensión crea una lista nueva, no modifica la lista original. 

### Sintaxis

```python
nueva_lista = [expresion for elemento in iterable]
```
Esto significa:

- **expresión:** la operación que queremos realizar con cada elemento
- **elemento:** la variable que representa cada valor que se recorre
- **iterable:** la colección de datos que estamos recorriendo (lista, rango, etc.)

### Ejemplo

```python
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)
```
Este código crea una lista con los números del 0 al 4.

```python
numeros = [x for x in range(5)]
print(numeros)
```
Este código crea una lista con los números del 0 al 4 utilizando una lista por comprensión. Es mucho más corto y claro. 

Si tenemos una lista de palabras en minúsculas y queremos convertirlas a mayúsculas y guardarlas en una nueva lista, podemos hacerlo de la siguiente manera:

```python
palabras = ["hola", "mundo", "python"]
mayusculas = [p.upper() for p in palabras]
print(mayusculas)
```
Resultado:
```python
['HOLA', 'MUNDO', 'PYTHON']
```

También podemos añadir condiciones dentro de una lista por comprensión. 

```python
numeros_pares = [x for x in range(10) if x % 2 == 0]
print(numeros_pares)
```
Resultado: 
```python
[0, 2, 4, 6, 8]
```
En este ejemplo el programa recorre los números del 0 al 9 y solo guarda en la lista aquellos que son pares.

Las listas por comprensión tienen varias ventajas:

- Permiten escribir código más corto y limpio. 
- Son más fáciles de leer cuando se utilizan correctamente.
- En muchos casos son más eficientes que utilizar un bucle tradicional. 

Las listas por comprensión son una herramienta muy común en Python porque permiten escribir código más limpio, corto y fácil de entender cuando se utilizan correctamente. 

## ¿Qué es un argumento en Python?

Un argumento en Python es el valor que se pasa a una función cuando se la llama. 
Por así decirlo, son los valores con los que estamos proporcionando información a la función para que pueda ejecutar su bloque de código. 

### Sintaxis

```python
funcion(argumento)
```
### Ejemplo
Es importante no confundir **parámetro** con **argumento**.

- **Parámetro:** es la variable que se define en la función.
- **Argumento:** es el valor que se pasa a la función cuando se llama. 

```python
def saludar(nombre): # "nombre" es un parámetro
    print("Hola", nombre) 

saludar("Patricia") # "Patricia" es el argumento
```
En este ejemplo, "Patricia" es el **argumento** que se pasa a la función **saludar** y se asigna al parámetro **nombre**
La función recibe ese valor y lo utiliza dentro de su bloque de código. 

Python asigna los valores de los argumentos **por defecto según el orden** en el que se pasan a la función.

```python
def presentar(nombre,edad):
    print(nombre, "tiene", edad, "años")

presentar("Patricia", 34)
```
El resultado es:
```python
Patricia tiene 34 años
```
Pero si cambias el orden:

```python
presentar(34, "Patricia")
```
El resultado es totalmente incorrecto ya que Python asigna `nombre = 34` y `edad = "Patricia"`

Para evitar este problema podemos utilizar **argumentos con nombre (keyword arguments)**.

```python
def presentar(nombre,edad):
    print(nombre, "tiene", edad, "años")

presentar(edad=34, nombre="Patricia")
```
En este caso el orden ya no importa ya que hemos indicado cual es el valor de cada argumento. 

También podemos definir un **valor por defecto para un parámetro**.  
Ese valor se utilizará si no se pasa ningún argumento al llamar a la función. 

```python
def saludar(nombre="amigo"):
    print("Hola", nombre)

saludar()
```
En este ejemplo, el resultado será:
```python
Hola amigo
```
Esto ocurre porque hemos definido un valor por defecto para el parámetro `nombre`.

### Argumentos variables en Python

En Python tambien es posible crear funciones que acepten un número variable de argumentos. Para ello se utilizan `*args`y `**kwargs`.

#### `*args`

`*args` permite que una función reciba varios argumentos posicionales, incluso si no sabemos cuántos se van a pasar. 

Ejemplo:

```python
def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    print(total)

sumar(1, 2, 3)
sumar(5, 10, 15, 20)
```
En este caso, `*numeros` recogen todos los valores que se pasan a la función y los guarda en una **tupla**.

#### `**kwargs`

`**kwargs` permite que una función reciba argumentos con nombre en forma de diccionario.

```python
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(clave, ":", valor)

mostrar_datos(nombre="Patricia", edad=34, ciudad="Bilbao")
```
En este caso, los valores se guardan en un diccionario donde:

- la **clave** es el nombre del argumento
- el **valor** es el dato que se ha pasado

## ¿Qué es una función Lambda en Python?

Las expresiones lambda son una forma corta de definir funciones en Python. 
Se trata de funciones anónimas (funciones sin nombre propio) que se pueden definir en una sola línea utilizando la palabra clave **lambda**.

Son ideales cuando necesitamos realizar operaciones simples de forma rápida y concisa. 

Se suelen utilizar cuando:
- La función es muy corta
- Solo se usa una vez
- Hace una operación simple

Se ha de evitar cuando:
- La función es larga
- Tiene varias operaciones
- Es necesario reutilizarla. 
En esos casos, mejor usar `def`

### Sintaxis

```python
lambda parametros: expresion
```

### Ejemplo
Normalmente, una función se escribe así:
```python 
def suma(a, b):
    return a + b

print(suma(3, 5))
```

Con `lambda`, lo mismo se puede hacer en una sola línea:

```python
suma = lambda a, b: a + b

print(suma(3, 5))
```
En este ejemplo se crea una función lambda que suma dos números. 
Los valores 3 y 5 se pasan como argumentos y la función devuelve su suma. 

Las funciones `lambda` solo pueden contener una única expresión y no permiten escribir varias instrucciones como en una función definida con `def`.

Las funciones lambda son útiles para operaciones pequeñas y rápidas, especialmente cuando necesitamos una función temporal que solo se utilizará una vez dentro de otra función. 

## ¿Qué es un paquete pip?

Un paquete de Python es una colección de librerías o módulos que contienen código reutilizable. Este código preescrito se pueden instalar, actualizar y eliminar fácilmente utilizando la herramienta de gestión de paquetes `pip` desde la terminal.

La mayoría de los paquetes de Python se distribuyen a través de [PyPI (Python Package Index)](https://pypi.org), que es el repositorio oficial donde los desarrolladores publican sus librerías para que otros puedan instalarlas y utilizarlas en sus proyectos.

Gracias a `pip`, los desarrolladores pueden añadir nuevas funcionalidades a sus programas sin tener que escribir todo el código desde cero.

Por ejemplo, existen paquetes para:

- desarrollo web
- análisis de datos
- inteligencia artificial
- automatización

### Comandos básicos de `pip`

**Para instalar un paquete utilizando `pip`, abre la terminal y ejecuta:**

```bash
pip install nombre_del_paquete
```

**Para ver paquetes instalados:**

```bash
pip list
```
Muestra todos los paquetes instalados en el entorno de Python. 

**Actualizar un paquete:**

```bash
pip install --upgrade nombre_del_paquete
```

Actualiza un paquete a su versión más reciente. 

**Eliminar un paquete:**

```bash
pip uninstall nombre_del_paquete
```

Elimina un paquete instalado. 

Gracias a `pip`, permite que Python sea un lenguaje en constante actualización ya que puedes utilizar librerías creadas por otros desarrolladores sin tener que escribir todo el código desde cero. 
