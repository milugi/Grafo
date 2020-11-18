from TDA_Grafo import Grafo, insertar_vertice, insertar_arista, buscar_vertice, barrido_vertices, dijkstra_distancia, dijkstra_duracion
from TDA_PilaDin import desapilar, pila_vacia
from random import randint
from TDA_Grafo import adyacentes, existe_paso

g = Grafo(False)

#A Cada nodo tiene el nombre y el tipo.

insertar_vertice(g, 'Ubuntu', 'PC')
insertar_vertice(g, 'Debian', 'Notebook')
insertar_vertice(g, 'Switch 1', 'Switch')
insertar_vertice(g, 'Impresora', 'Impresora')
insertar_vertice(g, 'Mint', 'PC')
insertar_vertice(g, 'Router 1', 'Router')
insertar_vertice(g, 'Router 2', 'Router')
insertar_vertice(g, 'Router 3', 'Router')
insertar_vertice(g, 'Red Hat', 'Notebook')
insertar_vertice(g, 'Guarani', 'Servidor')
insertar_vertice(g, 'Switch 2', 'Switch')
insertar_vertice(g, 'Manjaro', 'PC')
insertar_vertice(g, 'Parrot', 'PC')
insertar_vertice(g, 'Fedora', 'PC')
insertar_vertice(g, 'Arch', 'Notebook')
insertar_vertice(g, 'MongoDB', 'Servidor')

# print('Listado de vértices')
# barrido_vertices(g)
# print()

#Carga de aristas desde Switch 1
ori = buscar_vertice(g, 'Switch 1')
des = buscar_vertice(g, 'Debian')
insertar_arista(g, 17, ori, des)
des = buscar_vertice(g, 'Ubuntu')
insertar_arista(g, 18, ori, des)
des = buscar_vertice(g, 'Impresora')
insertar_arista(g, 22, ori, des)
des = buscar_vertice(g, 'Mint')
insertar_arista(g, 80, ori, des)
des = buscar_vertice(g, 'Router 1')
insertar_arista(g, 29, ori, des)

#Carga de aristas desde Router 1
ori = buscar_vertice(g, 'Router 1')
des = buscar_vertice(g, 'Router 2')
insertar_arista(g, 37, ori, des)
des = buscar_vertice(g, 'Router 3')
insertar_arista(g, 43, ori, des)

#Carga de aristas desde Router 2
ori = buscar_vertice(g, 'Router 2')
des = buscar_vertice(g, 'Router 3')
insertar_arista(g, 50, ori, des)
des = buscar_vertice(g, 'Red Hat')
insertar_arista(g, 25, ori, des)
des = buscar_vertice(g, 'Guarani')
insertar_arista(g, 9, ori, des)

#Carga de aristas desde Switch 2
ori = buscar_vertice(g, 'Switch 2')
des = buscar_vertice(g, 'Router 3')
insertar_arista(g, 61, ori, des)
des = buscar_vertice(g, 'Manjaro')
insertar_arista(g, 40, ori, des)
des = buscar_vertice(g, 'Parrot')
insertar_arista(g, 12, ori, des)
des = buscar_vertice(g, 'MongoDB')
insertar_arista(g, 5, ori, des)
des = buscar_vertice(g, 'Arch')
insertar_arista(g, 56, ori, des)
des = buscar_vertice(g, 'Fedora')
insertar_arista(g, 3, ori, des)
# print('Listado de vértices y aristas')
# barrido_vertices(g)
# print()

#B Realizar barrido en profundidad y amplitud desde las tres netbooks
print('Barrido en profundidad desde Debian: ')
ori = buscar_vertice(g, 'Debian')
barrido_profundidad(g, ori)
print()
marcar_no_visitado(g)
print('Barrido en amplitud desde Debian: ')
ori = buscar_vertice(g, 'Debian')
barrido_amplitud(g, ori)
print()
marcar_no_visitado(g)
print('Barrido en profundidad desde Red Hat: ')
ori = buscar_vertice(g, 'Red Hat')
barrido_profundidad(g, ori)
print()
marcar_no_visitado(g)
print('Barrido en amplitud desde Red Hat: ')
ori = buscar_vertice(g, 'Red Hat')
barrido_amplitud(g, ori)
print()
marcar_no_visitado(g)
print('Barrido en profundidad desde Arch: ')
ori = buscar_vertice(g, 'Arch')
barrido_profundidad(g, ori)
print()
marcar_no_visitado(g)
print('Barrido en amplitud desde Arch: ')
ori = buscar_vertice(g, 'Arch')
barrido_amplitud(g, ori)
print()
marcar_no_visitado(g)

#C 

caminito = dijkstra(g, 'Manjaro', 'Impresora')
fin = 'Impresora'
peso_total = None
print('Camino más corto desde Manjaro: ')
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        print(dato[1][0].info)
        fin = dato[1][1]
print('El camino tiene un peso total de:', peso_total)
print()
marcar_no_visitado(g)
caminito = dijkstra(g, 'Red Hat', 'Impresora')
fin = 'Impresora'
peso_total = None
print('Camino más corto desde Red Hat: ')
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        print(dato[1][0].info)
        fin = dato[1][1]
print('El camino tiene un peso total de:', peso_total)
print()
marcar_no_visitado(g)
caminito = dijkstra(g, 'Fedora', 'Impresora')
fin = 'Impresora'
peso_total = None
print('Camino más corto desde Fedora: ')
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        print(dato[1][0].info)
        fin = dato[1][1]
print('El camino tiene un peso total de:', peso_total)
print()
marcar_no_visitado(g)

#D 
print('Árbol de expansión mínimo: ')
bosque = prim(g)
for i in range(0, len(bosque), 2):
    print(bosque[i], bosque[i+1])
print()

#E 
min = []
# Dijkstra Parrot
caminito = dijkstra(g, 'Parrot', 'Guarani')
fin = 'Guarani'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
min = ['Parrot', peso_total] 
marcar_no_visitado(g)
# Dijkstra Manjaro
caminito = dijkstra(g, 'Manjaro', 'Guarani')
fin = 'Guarani'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
if (peso_total < min[1]):
    min = ['Manjaro', peso_total]
marcar_no_visitado(g)
# Dijkstra Fedora
caminito = dijkstra(g, 'Fedora', 'Guarani')
fin = 'Guarani'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
if (peso_total < min[1]):
    min = ['Fedora', peso_total]
marcar_no_visitado(g)
# Dijkstra Mint
caminito = dijkstra(g, 'Mint', 'Guarani')
fin = 'Guarani'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
if (peso_total < min[1]):
    min = ['Mint', peso_total]
marcar_no_visitado(g)
# Dijkstra Ubuntu
caminito = dijkstra(g, 'Ubuntu', 'Guarani')
fin = 'Guarani'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
if (peso_total < min[1]):
    min = ['Ubuntu', peso_total]
marcar_no_visitado(g)
print('La PC con el camino más corto hasta el server Guaraní es:', min[0], 'con un peso de', min[1])
print()

#F 

mini = []
# Dijkstra Ubuntu
caminito = dijkstra(g, 'Ubuntu', 'MongoDB')
fin = 'MongoDB'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
mini = ['Ubuntu', peso_total]
marcar_no_visitado(g)
# Dijkstra Mint
caminito = dijkstra(g, 'Mint', 'MongoDB')
fin = 'MongoDB'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
if (peso_total < mini[1]):
    mini = ['Mint', peso_total]
marcar_no_visitado(g)
print('La PC con el camino más corto hasta el server MongoDB es:', mini[0], 'con un peso de', mini[1])
print()

#G 

ori = buscar_vertice(g, 'Impresora')
des = buscar_vertice(g, 'Switch 1')
eliminar_arista(g, ori, 'Switch 1')
# barrido_vertices(g)
print()
des = buscar_vertice(g, 'Router 2')
insertar_arista(g, 50, ori, des)
# barrido_vertices(g)
print('Barrido en profundidad desde Debian: ')
ori = buscar_vertice(g, 'Debian')
barrido_profundidad(g, ori)
print()
marcar_no_visitado(g)
print('Barrido en amplitud desde Debian: ')
ori = buscar_vertice(g, 'Debian')
barrido_amplitud(g, ori)
print()
marcar_no_visitado(g)
print('Barrido en profundidad desde Red Hat: ')
ori = buscar_vertice(g, 'Red Hat')
barrido_profundidad(g, ori)
print()
marcar_no_visitado(g)
print('Barrido en amplitud desde Red Hat: ')
ori = buscar_vertice(g, 'Red Hat')
barrido_amplitud(g, ori)
print()
marcar_no_visitado(g)
print('Barrido en profundidad desde Arch: ')
ori = buscar_vertice(g, 'Arch')
barrido_profundidad(g, ori)
print()
marcar_no_visitado(g)
print('Barrido en amplitud desde Arch: ')
ori = buscar_vertice(g, 'Arch')
barrido_amplitud(g, ori)
print()
marcar_no_visitado(g)
