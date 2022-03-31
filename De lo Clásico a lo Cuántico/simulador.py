import matplotlib.pyplot as pyplot
import libcplx as lc
import libopvcymtrz as lovm
import numpy

'''

DE LO CUANTICO A LO CLASICO

ELABORADO POR: JOSE RICARDO OLARTE PARDO

'''

#Ejercicio canicas
def canicas(matriz,vector,clicks):

    r = lovm.producto_matrices(matriz,matriz)
    clicks -= 1
    while clicks > 0:
        r = lovm.producto_matrices(r,matriz)
        clicks -= 1
    return lovm.producto_matrices(r,vector);

#Multiple Rendija
def multiplerendija(matriz,clicks):
    
    k,matriz1 = 0,matriz[:];
    while k!= clicks:
        for k in range(clicks):matriz = matriz*matriz1
        k+=1
    fila, columna = len(matriz), len(matriz[0])
    for i in range(fila):
        nueva_fila = []
        for j in range(columna):nueva_fila.append([(lc.modulo(matriz[i][j]) ** 2), 0])
        matriz[i] = nueva_fila
    return matriz;

#Probabilidad
def sistema_probabilistico(matriz,vector,clicks):
    
    k,r=0,[];
    while k != clicks:
        vec = matriz*vector
        k+=1
    for i in range(len(vector)):
        r = r + [[float(vector[i])]]
    return r;

#Grafico
def grafico(vector):
    data =len(vector)
    x = numpy.array([x for x in range(data)])
    y = numpy.array([round(vector[x][0] * 100, 2) for x in range(data)])

    pyplot.bar(x, y, color='r', align='center')
    pyplot.title('Probabilidad del Vector')
    pyplot.show()
