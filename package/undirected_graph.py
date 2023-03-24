from .ponderado import GrafoPonderado

class UndirectedGraph(GrafoPonderado):
    def addEdge(self, vertex: str, edge: str, peso: int) -> None:
        # Condicion necesarioa en caso tal de que los vertices que estemos tratando de unir ya esten en el grafo
        is_in = (vertex not in self.g_dict.keys()) or (edge not in self.g_dict.keys())

        if is_in:
            raise KeyError('The two vertex must be in the graph')
        # Como es no dirigido, creamos las dos conexiones de inmediato
        self.g_dict[vertex][edge] = peso
        self.g_dict[edge][vertex] = peso

                
    def dijkstra(self, origen):
        # Creamos un diccionario para el grafo
        distancias = {v: float('inf') for v in self.g_dict}
        distancias[origen] = 0
        visitados = set()
        # AA partir de aqui mientras que los visitados no superen al número de vertices que hayan en el grafo, continuamos
        while len(visitados) < len(self.g_dict):
            actual = None
            distancia_actual = float('inf')
            for vertice in self.g_dict:
                # Si nuestro vertice actual no esta en los visitados, procedemos a hacer los calculos
                if vertice not in visitados and distancias[vertice] < distancia_actual:
                    actual = vertice
                    distancia_actual = distancias[vertice]
            # Si ya terminamos de recorrer los vecinos del vertice, nos detenemos
            if actual is None:
                break
            # Guardamos el vertice ya que lo recorrimos
            visitados.add(actual)
            # Aca nos vamos a los vecinos del vertice y hacemos los respectivos calculos
            for adyacente, peso in self.g_dict[actual].items():
                nueva_dist = distancias[actual] + peso
                if nueva_dist < distancias[adyacente]:
                    distancias[adyacente] = nueva_dist
        # Retornamos un diccionario con los key (ciudades) y el peso minimo que hay de nuestro origen a todos los vertices del grafo
        return distancias
                
    def cities(self, MaxDistance: int):
        vertices = self.g_dict.keys()
        ciudades = {}
        
        # Creamos el diccionario para guardar las distancias a lo mas MaxDistance con sus distancias
        for i in vertices:
            ciudades[i] = []

        for vertex in vertices:
            for adyacent in vertices:
                # Sí el valor retornado como distancia minima es a lo mas MaxDistance entonces lo guardamos en el diccionario
                if self.dijkstra(vertex)[adyacent] <= MaxDistance and vertex != adyacent:
                # if self.DFS(vertex, adyacent, paths, valor)[1] <= MaxDistance and vertex != adyacent:
                    ciudades[vertex].append(adyacent)
                #     ciudades[vertex].append(adyacent)
        return ciudades
    
    def ciudad_menor(self, MaxDistance):
        # Traigo el diccionario creado anteriormente con cada una de las distancias cuyo peso es a lo más MaxDistance
        ciudades = self.cities(MaxDistance)
        # Los vertices 
        vertices = list(self.g_dict.keys())
        # Iniciamos un menor
        menor = len(ciudades[vertices[0]])
        # Aqui guardaremos las ciudades adyacentes que tengan menor número de elementos
        ciudades_ady = {}
                                
        # Pregunta basica de comparacion para buscar menores 
        for ciudad in ciudades:
            if menor >= len(ciudades[ciudad]):
                menor = len(ciudades[ciudad])
                ciudades_ady[ciudad] = ciudades[ciudad]

        # Este sera el key menor que queremos retornar
        menor_ret = int(list(ciudades.keys())[0])
        for i in ciudades_ady:
            if menor_ret > int(i):
                menor_ret = int(i)
        # Retornamos un diccionario con key de la ciudad menor que tiene distancias a lo mas MaxDistance
        return {f'{menor_ret}' : ciudades_ady[str(menor_ret)]}