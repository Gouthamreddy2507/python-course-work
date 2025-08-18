def print_A(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or j == size - 1 or i == size // 2:
                print("*", end=" ")
            elif (i == 0 and (j > 0 and j < size - 1)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_B(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or (j == size - 1 and (i != 0 and i != size - 1 and i != size // 2)):
                print("*", end=" ")
            elif (i == 0 or i == size - 1 or i == size // 2) and j < size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_C(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or (i == 0 or i == size - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_D(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or (j == size - 1 and i != 0 and i != size - 1):
                print("*", end=" ")
            elif (i == 0 or i == size - 1) and j < size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_E(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or i == 0 or i == size // 2 or i == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_F(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or i == 0 or i == size // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_G(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or (i == 0 or i == size - 1) or (i >= size // 2 and j == size - 1) or (i == size // 2 and j >= size // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_H(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or j == size - 1 or i == size // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_I(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == size // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_J(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or (j == size // 2) or (i == size - 1 and j < size // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_K(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or (i + j == size // 2) or (i - j == size // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_L(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or i == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_M(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or j == size - 1 or (i <= size // 2 and (i == j or i + j == size - 1)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_N(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or j == size - 1 or i == j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_O(size):
    for i in range(size):
        for j in range(size):
            if (i == 0 or i == size - 1 or j == 0 or j == size - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_P(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or (i == 0 or i == size // 2) or (j == size - 1 and i < size // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_Q(size):
    for i in range(size):
        for j in range(size):
            if (i == 0 or i == size - 2 or j == 0 or j == size - 2):
                print("*", end=" ")
            elif i == size - 1 and j == size - 3:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_R(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or (i == 0 or i == size // 2) or (j == size - 1 and i < size // 2) or (i - j == size // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_S(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or i == size // 2 or (j == 0 and i < size // 2) or (j == size - 1 and i > size // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_T(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or j == size // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_U(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or j == size - 1 or i == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_V(size):
    for i in range(size):
        for j in range(size):
            if i == j and i >= size // 2 or i + j == size - 1 and i >= size // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_W(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or j == size - 1 or (i >= size // 2 and (i == j or i + j == size - 1)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_X(size):
    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_Y(size):
    for i in range(size):
        for j in range(size):
            if (i == j and i <= size // 2) or (i + j == size - 1 and i <= size // 2) or (j == size // 2 and i > size // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_Z(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or i + j == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


name=input('Enter Name: ').upper()
for i in name:
    fun='print_'+i
    print(fun)
    globals()[fun](5)