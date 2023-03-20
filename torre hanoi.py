#ejercicio 1 torre de hanoi con 74 discos y 3 pilas a b y c para ir apilando y desapilando los discos 
class nodoPila:
    def __init__(self, dato): #constructor de la clase nodoPila
        self.dato = dato  #dato que se va a almacenar en la pila
        self.siguiente = None   #apuntador al siguiente nodo

class pila:    #clase pila
    def __init__(self): #constructor de la clase pila
        self.cima = None    #apuntador a la cima de la pila
        self.tam = 0    #tamaño de la pila

    def vacia(self):    #metodo para saber si la pila esta vacia
        if self.cima == None:   #si la cima de la pila es nula
            return True     #la pila esta vacia
        else:   #si no
            return False    #la pila no esta vacia
        
    def apilar(self, dato):  #metodo para meter un dato en la pila
        if self.vacia():    #si la pila esta vacia
            self.cima = nodoPila(dato)  #la cima de la pila apunta al nuevo nodo
        else:   #si no
            aux = nodoPila(dato)    #creamos un nuevo nodo
            aux.siguiente = self.cima   #el nuevo nodo apunta a la cima de la pila
            self.cima = aux     #la cima de la pila apunta al nuevo nodo
        self.tam += 1   #aumentamos el tamaño de la pila

    def desapilar(self):    #metodo para sacar un dato de la pila
        if self.vacia():    #si la pila esta vacia
            return None     #no se puede sacar nada
        else:   #si no
            aux = self.cima     #creamos un auxiliar que apunte a la cima de la pila
            self.cima = self.cima.siguiente  #la cima de la pila apunta al siguiente nodo
            self.tam -= 1   #disminuimos el tamaño de la pila
            return aux.dato     #retornamos el dato del nodo que se saco de la pila
        
    def cimaPila(self): #metodo para saber cual es el dato que esta en la cima de la pila
        if self.vacia():    #si la pila esta vacia
            return None     #no hay cima
        else:   #si no
            return self.cima.dato   #retornamos el dato que esta en la cima de la pila
        
    def tamPila(self):  #metodo para saber el tamaño de la pila
        return self.tam     #retornamos el tamaño de la pila
    
    def mostrarPila(self):  #metodo para mostrar los datos de la pila
        aux = self.cima  #creamos un auxiliar que apunte a la cima de la pila
        while aux != None:  #mientras el auxiliar no sea nulo
            print(aux.dato) #imprimimos el dato del nodo
            aux = aux.siguiente #el auxiliar apunta al siguiente nodo

def hanoi(n, origen, destino, auxiliar): #funcion para resolver el problema de las torres de hanoi
    i=0 #contador
    if n == 1:  #si solo hay un disco
        destino.apilar(origen.desapilar())  #se mueve el disco de la pila origen a la pila destino
    else:   #si no
        hanoi(n-1, origen, auxiliar, destino) #se llama a la funcion hanoi con n-1 discos, la pila origen, la pila auxiliar y la pila destino
        destino.apilar(origen.desapilar())  #se mueve el disco de la pila origen a la pila destino
        hanoi(n-1, auxiliar, destino, origen) #se llama a la funcion hanoi con n-1 discos, la pila auxiliar, la pila destino y la pila origen
    print("se han realizado ", i, " movimientos")

def main(): #funcion principal
    origen = pila() #creamos la pila origen
    destino = pila()    #creamos la pila destino
    auxiliar = pila()   #creamos la pila auxiliar
    for i in range(74, 0, -1):  #recorremos los numeros del 74 al 1
        origen.apilar(i)    #apilamos los numeros en la pila origen
    hanoi(74, origen, destino, auxiliar)    #llamamos a la funcion hanoi con 74 discos, la pila origen, la pila destino y la pila auxiliar
    destino.mostrarPila()   #mostramos los datos de la pila destino

main()  #llamamos a la funcion principal
