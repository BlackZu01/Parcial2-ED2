from package.ponderado import GrafoPonderado
from package.undirected_graph import UndirectedGraph
from pprint import pprint

grafo = {

}

grafo = UndirectedGraph(grafo)

grafo.addMultipleVertex(['0', '1', '2', '3'])

# Ejemplo 1 del PDF
grafo.addEdge('0', '1', 3)
# grafo.addEdge('0', '4', 8)

grafo.addEdge('1', '2', 1)
grafo.addEdge('1', '3', 4)

grafo.addEdge('2', '3', 1)

# print(grafo.cities(4))

print('[+] La ciudad con el menor número de ciudades a las que se puede llegar a través de alguna ruta es: ')
print(grafo.ciudad_menor(4))
