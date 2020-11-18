from TDA_Grafo import Grafo, insertar_vertice, insertar_arista, buscar_vertice, barrido_vertices, dijkstra_distancia, dijkstra_duracion
from TDA_PilaDin import desapilar, pila_vacia
from random import randint
from TDA_Grafo import adyacentes, existe_paso

grafo = Grafo(False)

#A Y D

insertar_vertice(grafo, 'Argentina', [" S34°0'0'' O84°0'0'' ", randint(1,19)])
insertar_vertice(grafo, 'Brasil', [" S14°0'0'' 94°0'0'' ",randint(1,78)])
insertar_vertice(grafo, 'Tailandia', [" S391°0'0'' O64°0'0'' ",randint(1,12)])
insertar_vertice(grafo, 'Grecia', [" S34°0'0'' O64°0'0'' ",randint(1,12)])
insertar_vertice(grafo, 'Alemania', [" S34°0'0'' O64°0'0'' ",randint(1,12)])
insertar_vertice(grafo, 'Francia', [" S34°0'0'' O64°0'0'' ",randint(1,13)])
insertar_vertice(grafo, 'Japon', [" S34°0'0'' O64°0'0'' ",randint(1,32)])
insertar_vertice(grafo, 'China', [" S14°0'0'' O64°0'0'' ",randint(1,7)])
insertar_vertice(grafo, 'EE.UU', [" S14°0'0'' O64°0'0'' ",randint(1,12)])
insertar_vertice(grafo, 'Jamaica', [" S934°0'0'' O64°0'0'' ",randint(1,3)])

#B

ori = buscar_vertice(grafo,'China')
des = buscar_vertice(grafo,'Japon')
insertar_arista(grafo, ['15:00 hs', '10:00 hs', 'Aerolinea', 1200, 15, 8987], ori, des)

ori = buscar_vertice(grafo,'Argentina')
des = buscar_vertice(grafo,'Japon')
insertar_arista(grafo, ['15:00 hs', '10:00 hs', 'Aerolinea0', 656, 15, 2987], ori, des)

ori = buscar_vertice(grafo,'Tailandia')
des = buscar_vertice(grafo,'EE.UU')
insertar_arista(grafo, ['13:00 hs', '18:00 hs', 'Aerolinea1', 12, 9, 1987], ori, des)

ori = buscar_vertice(grafo,'Tailandia')
des = buscar_vertice(grafo,'Japon')
insertar_arista(grafo, ['13:00 hs', '18:00 hs', 'Aerolinea1', 56, 9, 187], ori, des)

ori = buscar_vertice(grafo,'Brasil')
des = buscar_vertice(grafo,'China')
insertar_arista(grafo, ['20:00 hs', '08:00 hs', 'Aerolinea2', 499, 28, 9898], ori, des)

ori = buscar_vertice(grafo,'Brasil')
des = buscar_vertice(grafo,'Alemania')
insertar_arista(grafo, ['20:00 hs', '08:00 hs', 'Aerolinea2', 400, 8, 988], ori, des)

ori = buscar_vertice(grafo,'Jamaica')
des = buscar_vertice(grafo,'Francia')
insertar_arista(grafo, ['21:00 hs', '11:30 hs', 'Aerolinea3', 760, 24, 1009], ori, des)

ori = buscar_vertice(grafo,'Alemania')
des = buscar_vertice(grafo,'Grecia')
insertar_arista(grafo, ['02:00 hs', '11:00 hs', 'Aerolinea3', 800, 17, 1187], ori, des)

ori = buscar_vertice(grafo,'Argentina')
des = buscar_vertice(grafo,'Brasil')
insertar_arista(grafo, ['13:00 hs', '10:00 hs', 'Aerolinea4', 80, 15, 100], ori, des)

#                                                                           distancia[5]

#barrido_vertices(grafo)

#E i Menor distancia

'''masCorto = dijkstra_distancia(grafo, 'Argentina', 'Tailandia')
fin = 'Tailandia'
peso_total = None
while(not pila_vacia(masCorto)):
    dato = desapilar(masCorto)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        # print(dato[1][0].info) MUESTRA LA INFO DE LA ARISTA
        fin = dato[1][1]
print('Menor distancia posible a recorrer:', peso_total, 'Km')
print()
'''

# ii Menor duracion

menorduracion = dijkstra_duracion(grafo, 'Argentina', 'Tailandia')
fin = 'Tailandia'
peso_total = None
while(not pila_vacia(menorduracion)):
    dato = desapilar(menorduracion)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        # print(dato[1][0].info) MUESTRA LA INFO DE LA ARISTA
        fin = dato[1][1]
print('Menor duracion posible a recorrer:', peso_total, 'hs')
print()

# iii Menor costo


menorcosto = dijkstra_duracion(grafo, 'Argentina', 'Tailandia')
fin = 'Tailandia'
peso_total = None
while(not pila_vacia(menorcosto)):
    dato = desapilar(menorcosto)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        # print(dato[1][0].info) MUESTRA LA INFO DE LA ARISTA
        fin = dato[1][1]
print('Menor costo posible :', peso_total, 'USD')
print()

# iv Menor nro escalas ??

#v directa o indirecta

ori= buscar_vertice(grafo, 'Grecia')
print('Paises desde que se puede arribar directamente a Grecia: ')
adyacentes(ori)

lista = ['Argentina', 'Alemania', 'Brasil', 'China', 'Estados Unidos', 'Francia', 'Japón', 'Jamaica', 'Tailandia']

print('Paises desde que se puede arribar indirectamente a Grecia: ')

for elemento in lista:
    des = buscar_vertice(grafo, elemento)
    if existe_paso(grafo, ori, des):
        pila = dijkstra_duracion(grafo, ori, des)
        while not pila_vacia(pila):
            x = desapilar(pila)
            print(x[1][0].info, x[1][0].adyacentes.inicio.info)
























