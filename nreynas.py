# Variables globales
A = {i: True for i in range(1, 9)}        # Columnas libres: 1 a 8
B = {i: True for i in range(2, 17)}       # Diagonales principales: 2 a 16
C = {i: True for i in range(-7, 8)}       # Diagonales secundarias: -7 a 7
X = {i: 0 for i in range(1, 9)}           # Posición de reina en cada fila
Q = [False]                               # Mutable, para modificar dentro del procedimiento


def print_board():
    """Imprime la solución encontrada: posiciones de las reinas y el tablero."""
    for i in range(1, 9):
        print(f"{X[i]:4}", end='')
    print('\n')

    for i in range(1, 9):  # Filas
        for j in range(1, 9):  # Columnas
            if X[j] == i:
                print('*', end=' ')
            else:
                print('-', end=' ')
        print()  # Nueva línea al final de cada fila
    print()


def try_place(i, Q):
    """Intenta colocar una reina en la fila i."""
    j = 0
    while not Q[0] and j < 8:
        j += 1
        if A[j] and B[i + j] and C[i - j]:
            X[i] = j
            A[j] = B[i + j] = C[i - j] = False

            if i < 8:
                try_place(i + 1, Q)
                if not Q[0]:
                    A[j] = B[i + j] = C[i - j] = True
            else:
                Q[0] = True


def main_program():
    """Función principal para resolver el problema de las reinas."""
    for i in range(1, 9):
        A[i] = True
    for i in range(2, 17):
        B[i] = True
    for i in range(-7, 8):
        C[i] = True

    Q[0] = False
    try_place(1, Q)

    print('\nResultado:\n')
    if Q[0]:
        print_board()
    else:
        print("No hay solución posible.")


# Ejecutar el programa
main_program()
