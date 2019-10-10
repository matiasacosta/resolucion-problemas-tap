from .Vertice import Vertice
from collections import deque

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, clave):
        nuevo_vertice = Vertice(clave)
        self.vertices[clave] = nuevo_vertice
        return nuevo_vertice
            
    def obtener_vertice(self, clave):
        if clave in self.vertices:
            return self.vertices[clave]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices

    def agregar_arista(self,clave_v1,clave_v2,costo=0):
        self.vertices[clave_v1].agregar_conexion(self.vertices[clave_v2], costo)

    def obtener_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def dijkstra(self, origen, destino):
        
        distancias = {vertice: 1000 for vertice in self.obtener_vertices()}
        vertices_previos = {
            vertice: None for vertice in self.obtener_vertices()
        }
        distancias[origen] = 0
        vertices = list(self.obtener_vertices()).copy()

        while vertices:
            vertice_actual = min(vertices, key=lambda vertice: distancias[vertice])

            if distancias[vertice_actual] == 1000:
                break

            for vecino, costo in self.obtener_vertice(vertice_actual).conectado_a.items():
                ruta_alternativa = distancias[vertice_actual] + costo
                
                if ruta_alternativa < distancias[vecino.id]:
                    distancias[vecino.id] = ruta_alternativa
                    vertices_previos[vecino.id] = vertice_actual

            vertices.remove(vertice_actual)

        path, vertice_actual = deque(), destino
        while vertices_previos[vertice_actual] is not None:
            path.appendleft(vertice_actual)
            vertice_actual = vertices_previos[vertice_actual]
        if path:
            path.appendleft(vertice_actual)
        return path