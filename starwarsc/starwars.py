import csv

"""
Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves– de las que conocemos su nombre, largo, tripulación y c
antidad de pasajeros, desarrollar los algoritmos necesarios para resolver las actividades detalladas a continuación:

realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;
mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
indicar cuál es la nave que requiere mayor cantidad de tripulación;
mostrar todas las naves que comienzan con AT;
listar todas las naves que pueden llevar seis o más pasajeros;
mostrar toda la información de la nave más pequeña y la más grande.
"""


class Nave(object):
    """Clase nave"""
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        """Crea una nave con nombre, largo, tripulacion y pasajeros"""
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros

    def __str__(self):
        """Muestra la informacion de la nave"""
        return "Nombre: " + self.nombre + " Largo: " + str(self.largo) + " Tripulacion: " + str(self.tripulacion) + " Pasajeros: " + str(self.pasajeros)
    
    def __lt__(self, other):
        """Ordena por nombre"""
        return self.nombre < other.nombre
    
    def __gt__(self, other):
        """Ordena por largo"""
        return self.largo > other.largo
    
    def __eq__(self, other):
        """Compara por nombre"""
        return self.nombre == other.nombre
    
    def __ne__(self, other):
        """Compara por nombre"""
        return self.nombre != other.nombre
    
    def __le__(self, other):
        """Compara por nombre"""
        return self.nombre <= other.nombre
    
    def __ge__(self, other):
        """Compara por nombre"""
        return self.nombre >= other.nombre
    
    def __cmp__(self, other):
        """Compara por nombre"""
        return self.nombre.__cmp__(other.nombre)
    

class ListaNaves(object):
    """Clase lista de naves"""
    def __init__(self):
        """Crea una lista de naves"""
        self.lista = []
    
    def __str__(self):
        """Muestra la lista de naves"""
        return str(self.lista)
    
    def agregar_nave(self, nave):
        """Agrega una nave a la lista"""
        self.lista.append(nave)
    
    def ordenar_nombre(self):
        """Ordena la lista por nombre"""
        self.lista.sort()
    
    def ordenar_largo(self):
        """Ordena la lista por largo"""
        self.lista.sort(reverse=True)
    
    def mostrar_halcon(self):
        """Muestra la informacion del halcon milenario"""
        for nave in self.lista:
            if nave.nombre == "Millennium Falcon":
                print(nave)
    
    def mostrar_estrella(self):
        """Muestra la informacion de la estrella de la muerte"""
        for nave in self.lista:
            if nave.nombre == "Death Star":
                print(nave)
    
    def mostrar_top(self):
        """Muestra las 5 naves con mayor cantidad de pasajeros"""
        self.lista.sort(key=lambda nave: nave.pasajeros, reverse=True)
        for i in range(5):
            print(self.lista[i])
    
    def mostrar_tripulacion(self):
        """Muestra la nave que requiere mayor cantidad de tripulacion"""
        self.lista.sort(key=lambda nave: nave.tripulacion, reverse=True)
        print(self.lista[0])
    
    def mostrar_at(self):
        """Muestra las naves que comienzan con AT"""
        for nave in self.lista:
            if nave.nombre.startswith("AT"):
                print(nave)
    
    def mostrar_pasajeros(self):
        """Muestra las naves que pueden llevar 6 o mas pasajeros"""
        for nave in self.lista:
            if nave.pasajeros >= 6:
                print(nave)
    
    def mostrar_mas_pequeña(self):
        """Muestra la nave mas pequeña"""
        self.lista.sort(key=lambda nave: nave.largo)
        print(self.lista[0])
    
    def mostrar_mas_grande(self):
        """Muestra la nave mas grande"""
        self.lista.sort(key=lambda nave: nave.largo, reverse=True)
        print(self.lista[0])
    
    def mostrar_naves(self):
        """Muestra toda la informacion de las naves"""
        for nave in self.lista:
            print(nave)

def main():
    """Funcion principal"""
    lista = ListaNaves()
    with open("naves.csv", "w") as archivo:
        lector = csv.reader(archivo)
        for linea in csv.reader(archivo):
            lista.agregar_nave(Nave(linea[0], int(linea[1]), int(linea[2]), int(linea[3])))
    
    print("Listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente:")
    lista.ordenar_nombre()
    lista.mostrar_naves()
    print()
    print("Mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”:")
    lista.mostrar_halcon()
    lista.mostrar_estrella()
    print()
    print("Determinar cuáles son las cinco naves con mayor cantidad de pasajeros:")
    lista.mostrar_top()
    print()
    print("Indicar cuál es la nave que requiere mayor cantidad de tripulación:")
    lista.mostrar_tripulacion()
    print()
    print("Mostrar todas las naves que comienzan con AT:")
    lista.mostrar_at()
    print()
    print("Listar todas las naves que pueden llevar seis o más pasajeros:")
    lista.mostrar_pasajeros()
    print()
    print("Mostrar toda la información de la nave más pequeña y la más grande:")
    lista.mostrar_mas_pequeña()
    lista.mostrar_mas_grande()

if __name__ == "__main__":
    main()