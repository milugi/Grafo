from TDA_Grafo import Grafo, insertar_vertice, insertar_arista, buscar_vertice, barrido_vertices, dijkstra_distancia, dijkstra_duracion
from TDA_PilaDin import desapilar, pila_vacia
from random import randint
from TDA_Grafo import adyacentes, existe_paso, prim


#A Y F

g = Grafo(False)

#Maravillas Modernas
insertar_vertice(g, 'Ciudad de Petra', ['Jordania','Arquitectonica'])
insertar_vertice(g, 'Taj Mahal', ['India', 'Arquitectonica'])
insertar_vertice(g, 'Machu Picchu', ['Peru', 'Arquitectonica'])
insertar_vertice(g, 'Chichen Itza', ['Mexico', 'Arquitectonica'])
insertar_vertice(g, 'Coliseo', ['Roma', 'Arquitectonica'])
insertar_vertice(g, 'Gran Muralla', ['China', 'Arquitectonica'])
insertar_vertice(g, 'Cristo Redentor', ['Brasil', 'Arquitectonica'])

#Maravillas Naturales
insertar_vertice(g, 'Bahía de Ha Long', ['Vietnam', 'Naturales'])
insertar_vertice(g, 'Isla de Komodo', ['Indonesia', 'Naturales'])
insertar_vertice(g, 'Río subterráneo de Puerto Princesa', ['Filipinas', 'Naturales'])
insertar_vertice(g, 'Montaña de la Mesa', ['Sudáfrica', 'Naturales'])
insertar_vertice(g, 'Cataratas del Iguazú', [['Argentina', 'Brasil'] , 'Naturales'])
insertar_vertice(g, 'Río Amazonas', [['Perú', 'Colombia',  'Brasil'], 'Naturales'])
insertar_vertice(g, '2 Islas Jeju', ['Corea del Sur', 'Naturales'])
barrido_vertices(g)

#b

#Naturales

ori = buscar_vertice(g, 'Bahía de Ha Long')
des = buscar_vertice(g, 'Isla de Komodo')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Río subterráneo de Puerto Princesa')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Montaña de la Mesa')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cataratas del Iguazú')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Río Amazonas')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, '2 Islas Jeju')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Isla de Komodo')
des = buscar_vertice(g, 'Río subterráneo de Puerto Princesa')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Montaña de la Mesa')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cataratas del Iguazú')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Río Amazonas')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, '2 Islas Jeju')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Río subterráneo de Puerto Princesa')
des = buscar_vertice(g, 'Montaña de la Mesa')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cataratas del Iguazú')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Río Amazonas')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, '2 Islas Jeju')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Montaña de la Mesa')
des = buscar_vertice(g, 'Cataratas del Iguazú')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Río Amazonas')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, '2 Islas Jeju')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Cataratas del Iguazú')
des = buscar_vertice(g, 'Río Amazonas')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, '2 Islas Jeju')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Río Amazonas')
des = buscar_vertice(g, '2 Islas Jeju')
insertar_arista(g, randint(1000, 8000), ori, des)

#Modernas

ori = buscar_vertice(g, 'Ciudad de Petra')
des = buscar_vertice(g, 'Taj Mahal')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Machu Picchu')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Chichen Itza')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Coliseo')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Gran Muralla')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cristo Redentor')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Taj Mahal')
des = buscar_vertice(g, 'Machu Picchu')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Chichen Itza')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Coliseo')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Gran Muralla')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cristo Redentor')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Machu Picchu')
des = buscar_vertice(g, 'Chichen Itza')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Coliseo')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Gran Muralla')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cristo Redentor')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Chichen Itza')
des = buscar_vertice(g, 'Coliseo')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Gran Muralla')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cristo Redentor')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Coliseo')
des = buscar_vertice(g, 'Gran Muralla')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cristo Redentor')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Gran Muralla')
des = buscar_vertice(g, 'Cristo Redentor')
insertar_arista(g, randint(1000, 8000), ori, des)


#C

bosque = prim(g)

print('Arbol de expansion minimo: ')
for i in range(0, len(bosque), 2): #avanza de a dos. Muestra datos en conjunto
    print(bosque[i], bosque[i+1])  #par de arboles 
print()


# d




