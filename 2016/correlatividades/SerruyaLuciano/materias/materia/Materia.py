class Materia:
    def __init__(self, _id):
        self.id = _id
        self.aprobada = False
        self.correlativas = []

    def aprobar(self):
        self.aprobada = True

    def agregar_correlativa(self, materia):
        self.correlativas.append(materia)

    def sos_materia(self, _id):
        return self.id == _id

    def sos_registrable(self):
        #Si no tengo correlativas, soy registrable si estoy aprobada
        if not self.correlativas:
            return self.aprobada

        #si tengo correlativas, soy registrable si estoy aprobada
        #y mis correlativas estan aprobadas
        return self.aprobada and all(map(
            lambda materia: materia.sos_registrable(),
        self.correlativas))
