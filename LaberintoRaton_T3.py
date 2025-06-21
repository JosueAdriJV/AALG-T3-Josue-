#Profesor como el  F y el I equivalen a 1 le coloque 1 en la matriz
matriz = [
    [1, 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    [1, 1, 3, 1, 0, 1, 1, 1, 1]
]

# Matriz para guardar el camino
res = [[0 for i in range(9)] for i in range(9)]

intentos = 0  


def puntos_celda(valor):
    if valor == 3:
        return 3
    elif valor == 4:
        return 4
    else:
        return 0

def es_valido(f, c):
    if f < 0 or f >= 9:
        return False
    if c < 0 or c >= 9:
        return False
    if matriz[f][c] == 0:
        return False
    if res[f][c] == 1:
        return False
    return True

def mostrar(m):
    for fila in m:
        for valor in fila:
            print(valor, end=" ")
        print()
    print()

def resolver(fil, col, puntos):
    global intentos

    if fil == 0 and col == 0:
        puntos += puntos_celda(matriz[fil][col])
        if puntos >= 23:
            res[fil][col] = 1
            intentos += 1
            print(f"Intento {intentos}:")
            mostrar(res)
            return True
        else:
            return False

    if es_valido(fil, col):
        res[fil][col] = 1
        puntos += puntos_celda(matriz[fil][col])
        intentos += 1
        print(f"Intento {intentos}:")
        mostrar(res)

         # Abajo
        if resolver(fil + 1, col, puntos): 
            return True
        # Derecha
        elif resolver(fil, col + 1, puntos):  
            return True
        # Izquierda
        elif resolver(fil, col - 1, puntos):  
            return True
        # Arriba
        elif resolver(fil - 1, col, puntos):  
            return True
        else:
            # Retrocede
            res[fil][col] = 0  
    return False


print("Laberinto originaal:")
mostrar(matriz)

if resolver(8, 0, 0):
    print("Camino encontrado con almenos 23 puntos")
else:
    print("Camino no encontrado con  23 puntos.")

print("\nCamino final:")
mostrar(res)
