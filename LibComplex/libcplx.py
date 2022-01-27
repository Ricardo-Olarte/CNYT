import math

# Suma de un numero complejo
def suma(a,b):

    real = a[0] + b[0]
    imaginaria = a[1] + b[1]

    return (real,imaginaria)

# Resta de un numero complejo
def resta(a,b):

    real = a[0] - b[0]
    imaginaria = a[1] - b[1]

    return (real,imaginaria)

#Conjugado de un numero complejo
def conjugado(a):
    return (a[0],a[1]*-1)

# Multiplicacion de un numero complejo
def multiplicacion(a,b):

    real = a[0] * b[0]
    imaginaria = (a[0] * b[1]) + (a[1] * b[0]) + (a[1] * b[1] * -1)

    return (real,imaginaria)

#Division de un numero complejo
def division(a,b):

    numerador = multiplicacion(a,conjugado(b))
    denominador = (b[0]**2) + (b[1]**2)
    real = numerador[0]/denominador
    imaginaria = numerador[1]/denominador

    return (real,imaginaria)

#Modulo de un numero complejo
def modulo(a):
    return (a[0]**2 + a[1]**2)**0.5

#Fase de un numero complejo
def fase(a):
    return math.degrees(math.atan(abs(a[1]/a[0])))

#Coordenada Polar de un numero complejo
def polar(a):
    r = modulo(a)
    angulo = fase(a)
    return (r,angulo)

#Coordenada Cartesiana de un numero complejo
def cartesiana(a):
    r = a[0]
    angulo = a[1]
    seno = math.sin(angulo)
    coseno = math.cos(angulo)
    abscisa = r * coseno
    ordenada = r * seno
    return (abscisa, ordenada)

if __name__ == '__main__':
    print(suma((1,1),(2.5,-1.9))) # (1 + i) + (2.5 - 1.9i) = 3.5 - 0.9i
    print(resta((1,1),(2.5,-1.9))) # (1 + i) - (2.5 - 1.9i) = -1.5 + 2.9i
    print(multiplicacion((1,1),(2.5,-1.9))) # (1 + i) * (2.5 - 1.9i) = 2.5 + 2.5i
    print(division((1,1),(2.5,-1.9))) # (1 + i) / (2.5 - 1.9i) =  0.61 + 0.447i
    print(modulo((2.5,-1.9))) # |(2.5 - 1.9i)| = 3.14
    print(fase((2.5,-1.9))) # (2.5 - 1.9i) = 37.23
    print(polar((2.5,-1.9))) # (2.5 - 1.9i) = (3.14, 37.235)
    print(cartesiana((2.5,-1.9))) # (2.5 - 1.9i) = (-0.808,-2.365)
