class Vertice:

    def __init__(self, clave):
        self.id = clave
        self.conectado_a = {}

    def agregar_conexion(self, vertice_b, ponderacion=0):
        self.conectado_a[vertice_b] = ponderacion

    def obtener_conexiones(self):
        return self.conectado_a.keys()

    def obtener_id(self):
        return self.id
    
    def obtener_ponderacion(self,vertice_b):
        return self.conectado_a[vertice_b]

    def __str__(self):
        return f"{self.id}"