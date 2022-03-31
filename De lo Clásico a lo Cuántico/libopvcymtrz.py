import libcplx as lc

'''

LIBRERIA OPERACIONES DE VECTORES Y MATRICES

ELABORADO POR: JOSE RICARDO OLARTE PARDO

'''


# Adicion de vectores complejos
def adicion_vectores(v1, v2):
    v3 = []
    if len(v1) == len(v2):
        for i in range(len(v1)):
            res = lc.suma(v1[i], v2[i])
            v3.append(res)
        return v3


# Inverso (Aditivo) de un vector complejo
def inversa_vectores(v1):
    v3 = []
    for i in v1:
        oper = (i[0] * -1, i[1] * -1)
        v3.append(oper)
    return v3


# Multiplicacion de un escalar en un vector complejo
def multiplicacion_escalar_vectores(k, v1):
    v3 = []
    for i in v1:
        oper = (i[0] * k, i[1] * k)
        v3.append(oper)
    return v3


# Adición de matrices complejas
def adicion_matrices(m1, m2):
    matriz = [[0] * (len(m1[0])) for i in range(len(m1))]
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for a in range(len(m1)):
            for b in range(len(m1[0])):
                matriz[a][b] = lc.suma(m1[a][b], m2[a][b])
        return matriz
    else:
        return False


# Inversa (aditiva) de una matriz compleja
def inversa_matrices(k, m1):
    matriz = [[None] * len(m1[0]) for x in range(len(m1))]
    if type(k) is not tuple:
        k = (k, 0)
    for a in range(len(m1)):
        for b in range(len(m1[a])):
            matriz[a][b] = lc.multiplicacion(k, m1[a][b])
    return matriz


# Transpuesta de una matriz/vector
def transpuesta(m1):
    matriz = [[None] * len(m1[0]) for i in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m1[0])):
            matriz[i][j] = m1[j][i]
    return matriz


# Conjugada de una matriz/vector
def matriz_vector_conjugada(m1):
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            m1[i][j] = lc.conjugado(m1[i][j])
    return m1

# Adjunta (daga) de una matriz/vector
def adjunta(m1):
    m2 = matriz_vector_conjugada(transpuesta(m1))
    return m2

# Producto de dos matrices
def producto_matrices(m1, m2):
    matriz = [[(0, 0)] * len(m2[0]) for i in range(len(m1))]
    cos = 0
    if len(matriz) == 1:
        cos = 1

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(matriz) + cos):
                matriz[i][j] = lc.suma(matriz[i][j], lc.multiplicacion(m1[i][k], m2[k][j]))
    return matriz

# Accion de una matriz sobre un vector
def accion(v, m):
    w = multiplicacion_escalar_vectores(v, m)
    return w

# Producto interno entre dos vectores
def producto_interno_vectores(v1,v2):
    a, b = lc.shape(v1), lc.shape(v2)
    c=0
    for i in range(len(v1)):
        c = c+ (v1[i]*v2[i])
    return c

# Norma de un vector
def norma(m1):
    m2 = 0
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m2 += (m1[i][j][0]) ** 2 + (m1[i][j][1]) ** 2
    raiz = round(m2 ** 0.5, 2)
    return raiz

# Distancia entre matrices
def distancia(m1, m2):
    m3 = [[(0, 0)] * len(m1[0]) for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m3[i][j] = lc.resta(m1[i][j], m2[i][j])
    d = norma(m3)
    return d

# Revisar si es unitaria
def unit(m1):
    res = multiplicacion_escalar_vectores(m1, adjunta(m1))
    identidad = [[(0, 0)] * len(m1) for i in range(len(m1))]
    for i in range(len(identidad)):
        identidad[i][i] = (1, 0)
    if res == identidad:
        return True
    else:
        return False


# Revisar si es hermitian
def hermitian(m1):
    if adjunta(m1) == m1:
        return True
    else:
        return False


# Producto tensor entre vectores
def producto_tensor_vector(v1, v2):
    res = []
    for i in range(len(v1)):
        for j in range(len(v2)):
            res.append(lc.multiplicacion(v1[i], v2[j]))
    return res


# Producto tensor entre matrices
def producto_tensor_matriz(m1, m2):
    m3 = []
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            m3.append((producto_matrices(m1[i][j], m2)))
    return m3


# Main
if __name__ == '__main__':
    print()