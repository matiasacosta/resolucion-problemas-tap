from Vertice import Vertice

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
