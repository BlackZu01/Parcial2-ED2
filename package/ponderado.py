from .directed_graph import DirectedGraph
from pprint import pprint

class GrafoPonderado(DirectedGraph):
    def addVertex(self, data: int) -> None:
        self.g_dict[data] = {}

    def addEdge(self, vertex: str, edge: str, peso: int) -> None:
        self.g_dict[vertex][edge] = peso

    # def floyd_warshall(self):
    #     distancias = {}
    #     for vertice1 in self.g_dict:
    #         distancias[vertice1] = {}
    #         for vertice2 in self.g_dict:
    #             if vertice1 == vertice2:
    #                 distancias[vertice1][vertice2] = 0
    #             elif vertice2 in self.g_dict[vertice1]:
    #                 distancias[vertice1][vertice2] = self.g_dict[vertice1][vertice2]
    #             else:
    #                 distancias[vertice1][vertice2] = float('inf')

    #     for intermedio in self.g_dict:
    #         for origen in self.g_dict:
    #             for destino in self.g_dict:
    #                 nueva_distancia = distancias[origen][intermedio] + distancias[intermedio][destino]
    #                 if nueva_distancia < distancias[origen][destino]:
    #                     distancias[origen][destino] = nueva_distancia

    #     return distancias
    def floyd_warshall(self):
        """
        Aplica el algoritmo de Floyd-Warshall para calcular todos los caminos más cortos y costos mínimos entre todos los pares de vértices.
        """
        # Inicializa los diccionarios de distancias y caminos mínimos
        distancias = {(origen, destino): peso for origen in self.g_dict for destino, peso in self.g_dict[origen].items()}
        caminos_minimos = {(origen, destino): [origen, destino] if origen != destino and (origen, destino) in self.g_dict else [] for origen in self.g_dict for destino in self.g_dict}

        # Ciclo principal del algoritmo
        for intermedio in self.g_dict:
            for origen in self.g_dict:
                for destino in self.g_dict:
                    # Calcula la distancia entre origen y destino a través de un vértice intermedio
                    nueva_distancia = distancias.get((origen, intermedio), float('inf')) + distancias.get((intermedio, destino), float('inf'))
                    # Si la distancia es menor a la que ya está almacenada, la actualiza
                    if nueva_distancia < distancias.get((origen, destino), float('inf')):
                        distancias[(origen, destino)] = nueva_distancia
                        # Actualiza el camino mínimo
                        caminos_minimos[(origen, destino)] = caminos_minimos[(origen, intermedio)][:-1] + caminos_minimos[(intermedio, destino)]

        return distancias, caminos_minimos

    # def dijkstra(self, origen):
    #     distancias = {v: float('inf') for v in self.g_dict}
    #     distancias[origen] = 0
    #     visitados = set()
    #     while len(visitados) < len(self.g_dict):
    #         actual = None
    #         distancia_actual = float('inf')
    #         for vertice in self.g_dict:
    #             if vertice not in visitados and distancias[vertice] < distancia_actual:
    #                 actual = vertice
    #                 distancia_actual = distancias[vertice]
    #         if actual is None:
    #             break
    #         visitados.add(actual)
    #         for adyacente, peso in self.g_dict[actual].items():
    #             nueva_dist = distancias[actual] + peso
    #             if nueva_dist < distancias[adyacente]:
    #                 distancias[adyacente] = nueva_dist
    #     return distancias

    def dijkstra(self, origen, destino):
        """
        Implementación del algoritmo de Dijkstra para encontrar el camino más corto desde un vértice de origen hasta un vértice de destino.

        :param origen: El vértice de origen.
        :param destino: El vértice de destino.
        :return: Una tupla que contiene la distancia mínima desde el origen hasta el destino y una lista que representa el camino mínimo desde el origen hasta el destino.
        """
        # Inicializar las distancias a infinito para todos los vértices excepto el origen
        distancias = {vertice: float('inf') for vertice in self.g_dict}
        distancias[origen] = 0

        # Inicializar el conjunto de vértices visitados y el diccionario de padres
        visitados = set()
        padres = {}

        # Mientras queden vértices no visitados, seleccionar el siguiente vértice con la menor distancia
        while len(visitados) < len(self.g_dict):
            vertice_actual = min((v, distancias[v]) for v in self.g_dict if v not in visitados)[0][0]
            visitados.add(vertice_actual)

            # Actualizar las distancias a los vecinos no visitados del vértice actual
            for vecino, peso in self.g_dict[vertice_actual].items():
                nueva_distancia = distancias[vertice_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    padres[vecino] = vertice_actual

        # Si se encontró un camino desde el origen hasta el destino, construir el camino mínimo
        if destino in padres:
            camino = [destino]
            vertice = destino
            while vertice != origen:
                vertice = padres[vertice]
                camino.append(vertice)
            camino.reverse()
            return distancias[destino], camino
        else:
            # Si no hay camino desde el origen hasta el destino, retornar None
            return float('inf'), []

# grafo.addEdge('A', 'B', 1)
# grafo.addEdge('A', 'C', 2)
# grafo.addEdge('C', 'E', 3)
# grafo.addEdge('B', 'D', 2)
# grafo.addEdge('D', 'F', 7)
# grafo.addEdge('E', 'F', 1)
# grafo.addEdge('B', 'C', 1)
# grafo.addEdge('B', 'E', 3)
# grafo.addEdge('D', 'E', 2)
# grafo.addEdge('D', 'C', 4)