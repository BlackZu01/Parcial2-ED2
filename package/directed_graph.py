import numpy as np

class DirectedGraph:
    def __init__(self, g_dict: dict=None) -> None:
        if g_dict is None:
            self.g_dict = g_dict
        self.g_dict = g_dict
        self.adj_m = None

    @property
    def nVertex(self) -> int:
        return len(list(self.g_dict.keys()))
    
    @property
    def info(self) -> dict:
        return self.g_dict

    @property 
    def vertices(self):
        return [vertex for vertex in self.g_dict.keys()]

    def neighbors(self, vertex: str):
        return self.g_dict[vertex]

    def addVertex(self, data: int) -> None:
        if data not in self.g_dict.keys():
            self.g_dict[data] = list()
            return 
        raise ValueError('The vertex {data} is already in the Graph')
    
    def addMultipleVertex(self, vertex_list: list):
        for i in vertex_list:
            self.addVertex(i)
    
    def addEdge(self, vertex: str, edge: str) -> None:
        self.g_dict[vertex].append(edge)

    def addEdges(self, vertex: str, edges: tuple=()) -> None:
        for edge in edges:
            self.g_dict[vertex].append(edge)

    def generateAdjMat(self) -> None:
        self.adj_m = np.zeros((self.nVertex, self.nVertex), dtype=int)
        vertex = list(self.g_dict.keys())

        for k in range(self.adj_m.shape[0]):
            for j in range(self.adj_m.shape[1]):
                for i in range(len(self.g_dict[vertex[k]])):
                    if vertex[j] == self.g_dict[vertex[k]][i]:
                        self.adj_m[k][j] = 1

    def confirmar_reunion(self):
        # Verificamos si hay alguna persona que no tenga favoritos revisando en los adyacentes de los vertices del grafo
        for value in self.g_dict.values():
            if not value:
                return '[+] No se puede dar la reunion puesto que alguien no tiene favorito'
            
        # Sino, entonces verificamos que una persona no sea la favorita de más de 2 personas
        for i in self.g_dict.keys():
            # Va a contar el número de apariciones de un vertice en los adyacentes de los demás vertices
            contador=0 
            for j in self.g_dict.keys():
                # Este for se mueve en los vertices adyacentes de cada vertice
                for k in range(len(self.g_dict[j])):
                    # Sí el vertice que i en el que estamos parados es igual a algun adycente de los demas vertices, añadimos un punto al contador
                    if i == self.g_dict[j][k]:
                        contador += 1
                    # Verificamos inmediatamente si el contador se pasó
                    if contador > 2:
                        return '[+] No se puede dar la reunion puesto que alguien no puede ser el favorito de más de 2 personas'
        return '[+] Se puede dar la reunion !!'

    def DFS(self, current: str, end:str, path: list):
        # Agregamos incialmente al nodo donde estamos empezando
        path.append(current)

        if current == end:
            return path 

        for vertex in self.neighbors(current):
            if vertex not in path:
                new_path = self.DFS(vertex, end, path)
                if new_path:
                    return new_path 
                
    def tiene_ciclo(self):
        """
        Determina si el grafo tiene al menos un ciclo.

        Returns:
            bool: True si el grafo tiene al menos un ciclo, False en caso contrario.
        """
        visitado = set()
        pila = set()
        for vertice in self.g_dict.keys():
            if vertice not in visitado:
                if self._dfs_tiene_ciclo(vertice, visitado, pila):
                    return True
        return False

    def _dfs_tiene_ciclo(self, vertice, visitado, pila):
        visitado.add(vertice)
        pila.add(vertice)
        for vecino in self.g_dict[vertice]:
            if vecino not in visitado:
                if self._dfs_tiene_ciclo(vecino, visitado, pila):
                    return True
            elif vecino in pila:
                return True
        pila.remove(vertice)
        return False

    def ciclos(self):
        ciclos_encontrados = []

        # Función auxiliar para realizar una búsqueda en profundidad y encontrar ciclos
        def encontrar_ciclos(vertice, visitados, en_pila, camino_actual):
            visitados.add(vertice)
            en_pila.add(vertice)
            camino_actual.append(vertice)

            # Explorar todos los vecinos del vértice actual
            for vecino in self.g_dict[vertice]:
                # Si el vecino no ha sido visitado, seguir explorando
                if vecino not in visitados:
                    encontrar_ciclos(vecino, visitados, en_pila, camino_actual)
                # Si el vecino ya está en la pila, se ha encontrado un ciclo
                elif vecino in en_pila:
                    ciclo = camino_actual[camino_actual.index(vecino):]
                    ciclos_encontrados.append(ciclo)

            # Eliminar el vértice actual de la pila y el camino actual
            en_pila.remove(vertice)
            camino_actual.pop()

        # Recorrer todos los vértices del grafo
        for vertice in self.g_dict:
            visitados = set()
            en_pila = set()
            camino_actual = []

            encontrar_ciclos(vertice, visitados, en_pila, camino_actual)

        return ciclos_encontrados
