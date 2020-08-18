'''
Funciones (Clase 4)

Aca estan definidas las siguientes funciones:
1. promedio -> realiza el promedio de un conjunto de valores
2. lista_aleatoria -> realiza una lista con numeros aleatorios
3. ordenar -> ordena un conjunto de valores de forma asc o dec
4. contar -> cuanta la cantidad de veces que hay un valor dentro de una lista
'''

__author__ = "Pablo Ruiz Diaz"
__email__ = "rd.pablo@gmail.com"
__version__ = "1.0"


import random


def promedio(numeros):
    '''
    promedio(numeros)
    
    La funcion "promedio" retorna el promedio
    de una lista de valores numericos ingresados 
    por el usuario.
    
    Parametros:
        numeros = lista numerica ingresada
    '''
    
    return sum(numeros) / len(numeros)


def lista_aleatoria(inicio, fin, cantidad):
    '''
    lista_aleatoria(inicio, fin, cantidad)

    La funcion "lista_aleatoria" retorna una lista de
    valores numericos random, cuyas especificaciones
    son marcadas por el usuario.
    
    Parametros:
        inicio = numero mas chico aceptado de la lista
        fin = numero mas grande aceptado de la lista
        cantidad = cantidad de valores numericos dentro de la lista
    '''

    lista_random = []

    for i in range(cantidad):
        numero = random.randrange(inicio, fin + 1)
        
        lista_random.append(numero)
    
    return lista_random


def ordenar(lista, orden='ascendente'):
    '''
    ordenar(lista, orden='ascendente')

    La funcion "ordenar" retorna el orden ascendente
    o descendente de una lista, sea numerica o alfabetica.
    
    Parametros:
        lista = lista ingresada por el usuario
        orden = "ascendente" (default) o "descendente"
    '''
    
    if orden == 'descendente':
        return lista.sort(reverse=True)
    elif orden == 'ascendente':
        return lista.sort(reverse=False)
    else:
        print('Parametro de Orden erroneo')
        return lista


def contar(lista, valor):
    '''
    contar(lista, valor)

    La funcion "contar" retorna un valor numerico
    en referencia a la cantidad de veces que el
    mismo es repetido dentro de la lista cargada.

    Parametros:
        lista = lista del usuario a ser analizada
        valor = valor alfanumerico para contar sus repeticiones
    '''

    return lista.count(valor)