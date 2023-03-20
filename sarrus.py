#ejercicio2

#de manera iterativa:
def iterativaSarrus():
    print('\033[35m'+ "DE MANERA ITERATIVA " + '\033[0m')
    matriz = [] 
    for i in range(3): 
        matriz.append([])   
        for j in range(3): 
            matriz[i].append(int(input("ingrese el numero de la posicion ["+str(i)+"]["+str(j)+"]: "))) #creamos la matriz
    print(matriz[0][0], matriz[0][1], matriz[0][2])
    print(matriz[1][0], matriz[1][1], matriz[1][2])
    print(matriz[2][0], matriz[2][1], matriz[2][2])   
    print('\033[36m'+"¿desea cambiar algún numero de la matriz? (si/no)"+'\033[0m')
    respuesta = input("->")
    if respuesta == "si":   
        print("ingrese la posicion del numero que desea cambiar")
        print("fila: ") 
        fila = int(input("->")) 
        print("columna: ")
        columna = int(input("->")) 
        print("ingrese el nuevo numero: ")
        numero = int(input("->")) 
        matriz[fila][columna] = numero 
        print("la matriz es: ")
        print(matriz[0][0], matriz[0][1], matriz[0][2])
        print(matriz[1][0], matriz[1][1], matriz[1][2])
        print(matriz[2][0], matriz[2][1], matriz[2][2])
    else:  
        print("la matriz se queda igual")

    determinante = matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[0][1]*matriz[1][2]*matriz[2][0] + matriz[0][2]*matriz[1][0]*matriz[2][1] - matriz[0][2]*matriz[1][1]*matriz[2][0] - matriz[0][1]*matriz[1][0]*matriz[2][2] - matriz[0][0]*matriz[1][2]*matriz[2][1] #utilizamos la fórmula del determinante de una matriz cuadrada de 3x3
    print("el determinante de la matriz es: ", determinante)   
    print('\033[35m'+ "===================" + '\033[0m')

iterativaSarrus()  

#de manera recursiva:
def recursivaSarrus():  
    print('\033[35m'+ "DE MANERA RECURSIVA " + '\033[0m')

    matriz = [] 
    for i in range(3):  
        matriz.append([])   
        for j in range(3):  
            matriz[i].append(int(input("ingrese el numero de la posicion ["+str(i)+"]["+str(j)+"]: "))) #agregamos los numeros ingresados por el usuario a la lista matriz
    print("la matriz es: ")
    print(matriz[0][0], matriz[0][1], matriz[0][2])
    print(matriz[1][0], matriz[1][1], matriz[1][2])
    print(matriz[2][0], matriz[2][1], matriz[2][2])
    print('\033[36m'+"¿desea cambiar algún numero de la matriz? (si/no)"+'\033[0m')
    respuesta = input()
    if respuesta == "si":   
        print("ingrese la posicion del numero que desea cambiar")
        print("fila: ") 
        fila = int(input("->")) 
        print("columna: ")
        columna = int(input("->")) 
        print("ingrese el nuevo numero: ")
        numero = int(input("->")) 
        matriz[fila][columna] = numero 
        print("la matriz es: ")
        print(matriz[0][0], matriz[0][1], matriz[0][2])
        print(matriz[1][0], matriz[1][1], matriz[1][2])
        print(matriz[2][0], matriz[2][1], matriz[2][2])
    else:  
        print("la matriz se queda igual")

    def determinante(matriz):   
        if len(matriz) == 1:   
            return matriz[0][0] 
        else:   
            det = 0 
            for i in range(len(matriz)):   
                det += (-1)**i*matriz[0][i]*determinante([fila[:i] + fila[i+1:] for fila in (matriz[1:])])   #lo calculamos por menores para que sea de manera recursiva
            return det  
        
    print("el determinante de la matriz es: ", determinante(matriz)) 
    print('\033[35m'+ "===================" + '\033[0m')  

recursivaSarrus()  