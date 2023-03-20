
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
#nombre, largo, tripulacion, pasajeros
lista = [
    ["Halcón Milenario", 34.37, 4, 6],
    ["Estrella de la Muerte", 120000, 342953, 843342],
    ["AT-AT", 20, 5, 40],
    ["AT-ST", 2, 2, 0],
    ["AT-TE", 5, 5, 0],
    ["AT-PT", 4, 4, 0],
    ["AT-AT Walker", 20, 5, 40],
    ["AT-ST Walker", 2, 2, 0],
    ["AT-TE Walker", 5, 5, 0],
    ["AT-PT Walker", 4, 4, 0],
    ["AT-AT Walker", 20, 5, 40],
    ["AT-ST Walker", 2, 2, 0],
    ["AT-TE Walker", 5, 5, 0],
    ["AT-PT Walker", 4, 4, 0],
    ["X-Wing", 12.5, 1, 0],
    ["Y-Wing", 14, 1, 0],
    ["A-Wing", 9.6, 1, 0],
    ["B-Wing", 16.9, 1, 0],
    ["TIE Fighter", 9.6, 1, 0],
    ["TIE Interceptor", 5.47, 1, 0],
    ["TIE Bomber", 7.92, 1, 0],
    ["TIE Advanced x1", 9.2, 1, 0],
    ["TIE Defender", 7.92, 1, 0],
    ["TIE Phantom", 9.6, 1, 0],
    ["TIE Reaper", 9.6, 1, 0],
    ["TIE Silencer", 9.6, 1, 0],
    ["TIE Striker", 9.6, 1, 0],
    ["TIE Punisher", 9.6, 1, 0],
    ["TIE Inquisitor", 9.6, 1, 0],
    ["TIE Advanced v1", 9.6, 1, 0],
    ["TIE Advanced v2", 9.6, 1, 0],
    ["TIE Advanced v3", 9.6, 1, 0],
    ["TIE Advanced v4", 9.6, 1, 0],
    ["TIE Advanced v5", 9.6, 1, 0],
    ["TIE Advanced v6", 9.6, 1, 0],
    ["TIE Advanced v7", 9.6, 1, 0],
    ["TIE Advanced v8", 9.6, 1, 0],
    ["TIE Advanced v9", 9.6, 1, 0],
    ["TIE Advanced v10", 9.6, 1, 0],
    ["TIE Advanced v11", 9.6, 1, 0],
    ["TIE Advanced v12", 9.6, 1, 0],
    ["TIE Advanced v13", 9.6, 1, 0],
    ["TIE Advanced v14", 9.6, 1, 0],
    ["TIE Advanced v15", 9.6, 1, 0],
    ["TIE Advanced v16", 9.6, 1, 0],
    ["TIE Advanced v17", 9.6, 1, 0],
    ["TIE Advanced v18", 9.6, 1, 0],
    ["TIE Advanced v19", 9.6, 1, 0],
    ["TIE Advanced v20", 9.6, 1, 0],
    ["CR90 corvette", 150, 30, 600],
    ["Naboo Royal Starship", 76, 8, 300],
    ["J-type diplomatic barge", 39, 5, 10],
    ["AA-9 Coruscant freighter", 390, 165, 3000],
    ["Jedi starfighter", 8, 1, 0],
    ["H-type Nubian yacht", 47, 8, 200],
    ["Republic Cruiser", 115, 16, 16],
    ["Droid control ship", 317, 175, 0],
    ["Naboo fighter", 11, 1, 0],
    
    
]