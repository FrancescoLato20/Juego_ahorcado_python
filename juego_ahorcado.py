"""
Juego: Ahorcado
Autor código: Francesco Latorrata
"""

import random

# FUNCIONES

# funcion que imprime el menú
def menu():
    print('---------JUEGO PALABRAS----------')
    print('1. Nivel fácil\n'
          '2. Nivel medio\n'
          '3. Nivel dificil\n'
          '4. Salir')

# función que devuelve el nivel de dificultad entre 1 y 3 (fácil, medio, difícil)
def elegir_nivel():
    while True:
        nivel = input('Introduce nivel: ')
        if nivel.isdigit():
            nivel = int(nivel)
            if nivel in (1,2,3,4):
                break
            else:
                print('Error a teclear.')
                menu()
        else:
            print('Debes ingresar un número intero')
    return nivel

# función para insertar las palabras secreta del juego
def introducir_palabras(lista):
    listado_palabra = lista
    for i in range(3):
        for j in range(4):
            lista[i][j]=input(f'Introduce palabra fila {i}, columnna {j}: ')
    return listado_palabra

# función que ordena las palabra en 3 niveles de dificultad
def ordenar_listado(lista):
    listado_ordenado=[[],[],[]]
    for fila in lista:
        for palabra in fila:
            if len(palabra) >0 and len(palabra)<= 4:
                listado_ordenado[0].append(palabra)
            elif len(palabra) > 4 and len(palabra) <= 6:
                listado_ordenado[1].append(palabra)
            elif len(palabra) > 6 and len(palabra) <= 10:
                listado_ordenado[2].append(palabra)

    return  listado_ordenado

# función para mostrar las letras que va adivinando el jugador
def mostrar_revelada(palabra, letras_adivinadas):
    revelada = ""
    for i in palabra:
        if i in letras_adivinadas:
            revelada += i
        else:
            revelada += "_"
    return revelada

# función que almacena en la variable 'palabra' la palabra secreta que hay que adivinar
def palabra_secreta(lista ,nivel):
    palabra = random.choice(lista[nivel -1]).upper()
    return palabra

# función del flujo del juego
def jugar(nivel):
    nivel = opcion
    palabra = palabra_secreta(listado_ordenado, nivel)
    letras_adivinadas = []
    intentos = 3
    while intentos > 0:
        print()
        print(mostrar_revelada(palabra, letras_adivinadas))
        letra = input('Introduce letra: ').upper()
        if letra in palabra:
            letras_adivinadas.append(letra)
            if intentos > 1:
                print(f'Te quedano {intentos} intentos')

            if intentos == 1:
                print(f'Te queda {intentos} intento')

            if palabra == mostrar_revelada(palabra, letras_adivinadas):
                print(f'Has ganado, la palabra es {palabra}')
                break
        else:
            print('Te has equivocado')
            intentos -= 1
            if intentos > 1:
                print(f'Te quedan {intentos} intentos')
            else:
                print(f'Te queda {intentos} intento')



# MAIN

listado = [[""]*5 for _ in range(3)]

listado = introducir_palabras(listado)
listado_ordenado = ordenar_listado(listado)

opcion = 1

while opcion in (1,2,3):
    menu()
    opcion = elegir_nivel()

    match opcion:
        case 1:
            jugar(opcion)
        case 2:
            jugar(opcion)
        case 3:
            jugar(opcion)
        case 4:
            print('Hasta pronto!')

