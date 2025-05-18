# Variables globales
A = {i: True for i in range(1, 9)}        # Columnas libres: índices 1 a 8
B = {i: True for i in range(2, 17)}        # Diagonales principales: índices 2 a 16
C = {i: True for i in range(-7, 8)}  # Diagonales secundarias: -7 a 7       
X = {i: 0 for i in range(1, 9)}
Q = [False] #se maneja en list apara poder cambiarla pues python no puede modificar bools directo por referencia          # Posiciones de las reinas* #

def print_board():
   
    """Imprime la solución encontrada: posiciones de las reinas y el tablero."""
    for i in range(1, 9):
        print(f"{X[i]:4}", end='')
    print('\n')

    for i in range(1, 9):  # Filas
        for j in range(1, 9):  # Columnas
            if X[j] == i:
                print('* ', end='') #end para no hacer salto de linea
            else:
                print('- ', end='') 
        print()  # Línea divisoria 
    print()  # Línea divisoria
    


def try_place(i, Q):
    """Intenta colocar una reina en la fila i."""
    j = 0
    while not  Q[0] and j < 8:
        j += 1
        if A[j] and B[i + j] and C[i - j]:
            # Marca que la posición está ocupada
            X[i] = j
            A[j] = False
            B[i + j] = False
            C[i - j] = False
            if i < 8:
                try_place(i + 1, Q)
                if not Q[0]:
                    # Backtracking: desmarca si no se pudo continuar
                    A[j] = True
                    B[i + j] = True
                    C[i - j] = True
            else:
                # Si llegamos a la fila 8, encontramos una solución
                Q[0] = True  # Así se modifica el valor real
        

def main_program():
    """Función principal para resolver el problema de las reinas."""
    for i in range(1, 9):
        A[i] = True
    for i in range(2, 17):
        B[i] = True
    for i in range(-7, 8):
        C[i] = True

    Q[0] = False  # Inicializa la lista de solución
    try_place(1, Q)
    print('\n')
    
    if Q[0]:
        print_board()
    else:
        print("No hay solución posible.")
        

main_program()
