import libcplx as cplx
import libopvcymtrz as lovm
import  numpy as np

#Calcula el bra
def bra(ket):
    return lovm.matriz_vector_conjugada(ket);

#Probabilidad del ket
def probabillidad_particle(ket, posicion):
    
    norma_ket = lovm.norma(ket)**2
    for i in range(len(ket)):norma_posicion = lovm.modulo(ket[i])**2
    norma_posicion = (modulo(ket[posicion])) ** 2
    return posicion, norma_posicion/norma_ket;

# A --> B
def amplitud_transicion(psi,phi):
    phi = lovm.matriz_vector_conjugada(phi)
    norma_phi = lovm.norma(phi);norma_psi = lovm.norma(psi)
    norma_ab = norma_phi*norma_psi
    probabillidad = [lovm.producto_matrices(psi, phi)]
    r = lovm.multiplicacion_escalar_vectores((1/norma_ab, 0), probabillidad)
    return r;

def media(observable, ket):
    if lovm.hermitian(observable):
        bra_ket = bra(ket);temp = lovm.accion(observable, ket)
        r = lovm.producto_interno_vectores(temp, bra_ket)
        return r;
    else:
        return "No se puede resolver, no es Hermitiano lo Observable";

def varianza(observable, ket):
    if lovm.hermitian(observable):
        bra_ket = bra(ket)
        media = media(observable, ket)
        identidad_media =  [[(0, 0) for j in range(len(observable[0]))] for i in range(len(observable))]
        for i in range(len(observable)):
            for j in range(len(observable[i])):
                if i==j:
                    identidad_media[i][j] = lovm.inversa_vectores(media)
        identidad_media = lovm.adicion_matrices(identidad_media, observable)
        observablealcudrado = lovm.producto_matrices(identidad_media, identidad_media)
        temp = lovm.accion(observablealcudrado, ket)
        r = lovm.producto_matrices(temp, bra_ket)
        return r;
    else:
        return "No se puede resolver, no es Hermitiano lo Observable";

def eigen_valores_propios(observable):
    
    valores, vectores = np.linalg.eig(observable)
    valores_propios = []
    vectores_propios = []
    for i in range(len(valores)):valores_propios += [(valores[i].real, valores[i].imag)]
    for i in range(len(vectores)):
        vector = []
        for j in range(len(vectores[0])):vector += [(vectores[i][j].real, vectores[i][j].imag)]
        vectores_propios += [vector]
    return valores_propios, vectores_propios;

def probabillidad_vectores(ket, observable, posicion):
    vectores = eigen_valores_propios(observable)[1]
    return amplitud_transicion(ket, vectores[posicion]);

# Ejercicio 4.3.1
def Ejercicio_431():


    v = [(1, 0), (0, 0)];observable = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    vector_resultado = lovm.accion(observable, v)
    valores, vectores = eigen_valores_propios(observable)
    print("El resultado de la observacion es: ", vector_resultado)
    print("Valores propios: ", valores, "\nVectores Propios: ", vectores)

# Ejercicio 4.3.2
def Ejercicio_432():

    v = [[(1, 0)], [(0, 0)]];observable = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    valores, vectores = eigen_valores_propios(observable)
    #r = probabillidad_vectores(v, observable, 1)
    for i in range(len(vectores)):print(amplitud_transicion(v,vectores[i]))

# Ejercicio 4.4.1
def Ejercicio_441():
    
    U1 = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    U2 = [[((2**(1/2))/2, 0), ((2**(1/2))/2, 0)], [((2**(1/2))/2, 0), (-(2**(1/2))/2, 0)]]
    if unitaria(U1) and unitaria(U2):print(cplx.unit(cplx.producto_matrices(U1,U2)))

# Ejercicio 4.4.2
def Ejercicio_442():

    
    matriz = [[(0, 0), (1/(2**(1/2)), 0), (1/(2**(1/2)), 0), (0, 0)],[(1/(2**(1/2)), 0), (0, 0), (0, 0), (-1/(2**(1/2)), 0)],[(1 / (2 ** (1 / 2)), 0), (0, 0), (0, 0), (1 / (2 ** (1 / 2)), 0)],[(0, 0), (-1/(2**(1/2)), 0), (1/(2**(1/2)), 0), (0, 0)]]
    vector_estado = [(1,0), (0,0), (0,0), (0,0)]
    clicks = 3
    
    if unitaria(matriz):
        for i in range(clicks):vector_estado = accion_Mat_Vector(matriz, vector_estado)
        print(vector_estado)
    else:
        print("No se puede resolver, la matriz no es unitaria")
    
    matriz = [[(0, 0), (1 / (2 ** (1 / 2)), 0), (1 / (2 ** (1 / 2)), 0), (0, 0)],[(0, 1 / (2 ** (1 / 2))), (0, 0), (0, 0), (1 / (2 ** (1 / 2)), 0)],[(1 / (2 ** (1 / 2)), 0), (0, 0), (0, 0), (0, 1 / (2 ** (1 / 2)))],[(0, 0), (1 / (2 ** (1 / 2)), 0), (-1 / (2 ** (1 / 2)), 0), (0, 0)]]
    vector_estado = [(1, 0), (0, 0), (0, 0), (0, 0)]
    clicks = 3
    
    if unitaria(matriz):
        for i in range(clicks):vector_estado = accion_Mat_Vector(matriz, vector_estado)
        print(vector_estado)
    else:
        print("No se puede resolver, la matriz no es unitaria")

Ejercicio_431();
print();
Ejercicio_432();
print();
Ejercicio_441();
print();
Ejercicio_442();
