import re
from Grafo import Grafo

class Caja:

    def __init__(self, grilla):
        """
        Se ingresa la grilla como una lista de lista
        y se inicializa posicion_actual
        que es un tupla que tendra valor (i,j,i1,j1) en el caso
        que la caja este acostada e (i,j,-,-) en el caso
        que la caja este parada
        """
        self.grilla = grilla
        self.posicion_actual = self.get_posicion('C')
        self.camino = ''
        self.grafo = Grafo()

    def get_posicion(self, tipo='C'):
        """
        Se establece la posicion solicitada, puede ser: 
        - C para la inicial
        - E para el final
        """
        a_buscar = f'.*{tipo}.*'
        for i in range(len(self.grilla)):
            match_obj = re.search(a_buscar,self.grilla[i])
            if match_obj:
                j = self.grilla[i].index(tipo)
                return (i, j, '-', '-')


    def get_orientacion(self, posicion=None):
        """
        funcion que retorna si la caja esta parada o acostada
        """
        if not posicion: posicion=self.posicion_actual
        if posicion[2] == '-' and posicion[3] == '-':
            return "Parada"
        elif posicion[0] == posicion[2]:
            return "Horizontal"
        elif posicion[1] == posicion[3]:
            return "Vertical"
        else:
            return False

    def movimiento_valido(self, posicion_final):
        """
        funcion que dado una tupla con una nueva posicion
        devuelve False si esta deshabilitado y True si no
        """
        try:
            if -1 in posicion_final:
                return False
            lugar_solicitado = self.grilla[posicion_final[0]][posicion_final[1]]
            if lugar_solicitado == '.' or lugar_solicitado == 'E' or lugar_solicitado == 'C':
                if '-' in posicion_final:
                    return True
                else:
                    lugar_solicitado = self.grilla[posicion_final[2]][posicion_final[3]]
                    return lugar_solicitado == '.' or lugar_solicitado == 'E' or lugar_solicitado == 'C'
            else:
                return False
        except IndexError: # Se pregunta por un lugar fuera del tablero
            return False

    def moverse_arriba(self, posicion=None):
        orientacion = self.get_orientacion(posicion)
        if not posicion: posicion = self.posicion_actual
        if orientacion == 'Parada':
            nueva_posicion = (
                posicion[0]-2,
                posicion[1],
                posicion[0]-1,
                posicion[1]
            )
        elif orientacion == 'Horizontal':
            nueva_posicion = (
                posicion[0]-1,
                posicion[1],
                posicion[2]-1,
                posicion[3],
            )
        elif orientacion == 'Vertical':
            nueva_posicion = (
                posicion[0]-1,
                posicion[1],
                '-',
                '-'
            )
        if self.movimiento_valido(nueva_posicion):
            return nueva_posicion
        else:
            return False

    def moverse_abajo(self, posicion=None):
        orientacion = self.get_orientacion(posicion)
        if not posicion: posicion=self.posicion_actual
        if orientacion == 'Parada':
            nueva_posicion = (
                posicion[0]+1,
                posicion[1],
                posicion[0]+2,
                posicion[1]
            )
        elif orientacion == 'Horizontal':
            nueva_posicion = (
                posicion[0]+1,
                posicion[1],
                posicion[2]+1,
                posicion[3],
            )
        elif orientacion == 'Vertical':
            nueva_posicion = (
                posicion[0]+2,
                posicion[1],
                '-',
                '-'
            )
        if self.movimiento_valido(nueva_posicion):
            return nueva_posicion
        else:
            return False

    def moverse_izquierda(self, posicion=None):
        orientacion = self.get_orientacion(posicion)
        if not posicion: posicion=self.posicion_actual
        if orientacion == 'Parada':
            nueva_posicion = (
                posicion[0],
                posicion[1]-2,
                posicion[0],
                posicion[1]-1
            )
        elif orientacion == 'Horizontal':
            nueva_posicion = (
                posicion[0],
                posicion[1]-1,
                '-',
                '-'
            )
        elif orientacion == 'Vertical':
            nueva_posicion = (
                posicion[0],
                posicion[1]-1,
                posicion[2],
                posicion[3]-1
            )
        if self.movimiento_valido(nueva_posicion):
            return nueva_posicion
        else:
            return False

    def moverse_derecha(self, posicion=None):
        orientacion = self.get_orientacion(posicion)
        if not posicion: posicion=self.posicion_actual
        if orientacion == 'Parada':
            nueva_posicion = (
                posicion[0],
                posicion[1]+1,
                posicion[0],
                posicion[1]+2
            )
        elif orientacion == 'Horizontal':
            nueva_posicion = (
                posicion[0],
                posicion[1]+2,
                '-',
                '-'
            )
        elif orientacion == 'Vertical':
            nueva_posicion = (
                posicion[0],
                posicion[1]+1,
                posicion[2],
                posicion[3]+1
            )
        if self.movimiento_valido(nueva_posicion):
            return nueva_posicion
        else:
            return False

    def moverse(self, movimiento, posicion=None):
        """
        Los valores posibles del movimiento son:
        - U(up)
        - D(down)
        - L(left)
        - R(right)
        """
        if not posicion: posicion=self.posicion_actual
        if movimiento == 'U':
            resultado = self.moverse_arriba(posicion)
        elif movimiento == 'D':
            resultado = self.moverse_abajo(posicion)
        elif movimiento == 'L':
            resultado = self.moverse_izquierda(posicion)
        elif movimiento == 'R':
            resultado = self.moverse_derecha(posicion)
        if resultado:
            self.camino = self.camino + movimiento
            self.posicion_actual = resultado
            return resultado
        else:
            return False

    def descubrir_caminos(self, posicion, vertices):
        for movimiento in ['U', 'D', 'L', 'R']:
            nueva_posicion = self.moverse(movimiento, posicion)
            if nueva_posicion and nueva_posicion not in vertices:
                vertices.append(nueva_posicion)
                self.descubrir_caminos(nueva_posicion, vertices)
        return vertices