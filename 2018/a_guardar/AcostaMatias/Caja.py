import re

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
        self.posicion_actual = self.get_posicion_inicial()
        self.camino = ''

    def get_posicion_inicial(self):
        """
        Se establece la posicion inicial
        """
        # La posicion inicial de la caja se representa con la C
        for i in range(len(self.grilla)):
            match_obj = re.search(r'.*C.*',self.grilla[i])
            if match_obj:
                j = self.grilla[i].index('C')
                return (i, j, '-', '-')

    def get_orientacion(self):
        """
        funcion que retorna si la caja esta parada o acostada
        """
        if self.posicion_actual[2] == '-' and self.posicion_actual[3] == '-':
            return "Parada"
        elif self.posicion_actual[0] == self.posicion_actual[2]:
            return "Horizontal"
        elif self.posicion_actual[1] == self.posicion_actual[3]:
            return "Vertical"
        else:
            return -1

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

    def moverse_arriba(self):
        orientacion = self.get_orientacion()
        if orientacion == 'Parada':
            nueva_posicion = (
                self.posicion_actual[0]-2,
                self.posicion_actual[1],
                self.posicion_actual[0]-1,
                self.posicion_actual[1]
            )
        elif orientacion == 'Horizontal':
            nueva_posicion = (
                self.posicion_actual[0]-1,
                self.posicion_actual[1],
                self.posicion_actual[2]-1,
                self.posicion_actual[3],
            )
        elif orientacion == 'Vertical':
            nueva_posicion = (
                self.posicion_actual[0]-1,
                self.posicion_actual[1],
                '-',
                '-'
            )
        if self.movimiento_valido(nueva_posicion):
            return nueva_posicion
        else:
            return False

    def moverse_abajo(self):
        orientacion = self.get_orientacion()
        if orientacion == 'Parada':
            nueva_posicion = (
                self.posicion_actual[0]+1,
                self.posicion_actual[1],
                self.posicion_actual[0]+2,
                self.posicion_actual[1]
            )
        elif orientacion == 'Horizontal':
            nueva_posicion = (
                self.posicion_actual[0]+1,
                self.posicion_actual[1],
                self.posicion_actual[2]+1,
                self.posicion_actual[3],
            )
        elif orientacion == 'Vertical':
            nueva_posicion = (
                self.posicion_actual[0]+2,
                self.posicion_actual[1],
                '-',
                '-'
            )
        if self.movimiento_valido(nueva_posicion):
            return nueva_posicion
        else:
            return False

    def moverse_izquierda(self):
        orientacion = self.get_orientacion()
        if orientacion == 'Parada':
            nueva_posicion = (
                self.posicion_actual[0],
                self.posicion_actual[1]-2,
                self.posicion_actual[0],
                self.posicion_actual[1]-1
            )
        elif orientacion == 'Horizontal':
            nueva_posicion = (
                self.posicion_actual[0],
                self.posicion_actual[1]-1,
                '-',
                '-'
            )
        elif orientacion == 'Vertical':
            nueva_posicion = (
                self.posicion_actual[0],
                self.posicion_actual[1]-1,
                self.posicion_actual[2],
                self.posicion_actual[3]-1
            )
        if self.movimiento_valido(nueva_posicion):
            return nueva_posicion
        else:
            return False

    def moverse_derecha(self):
        orientacion = self.get_orientacion()
        if orientacion == 'Parada':
            nueva_posicion = (
                self.posicion_actual[0],
                self.posicion_actual[1]+1,
                self.posicion_actual[0],
                self.posicion_actual[1]+2
            )
        elif orientacion == 'Horizontal':
            nueva_posicion = (
                self.posicion_actual[0],
                self.posicion_actual[1]+2,
                '-',
                '-'
            )
        elif orientacion == 'Vertical':
            nueva_posicion = (
                self.posicion_actual[0],
                self.posicion_actual[1]+1,
                self.posicion_actual[2],
                self.posicion_actual[3]+1
            )
        if self.movimiento_valido(nueva_posicion):
            return nueva_posicion
        else:
            return False

    def moverse(self, movimiento):
        """
        Los valores posibles del movimiento son:
        - U(up)
        - D(down)
        - L(left)
        - R(right)
        """
        if movimiento == 'U':
            resultado = self.moverse_arriba()
        elif movimiento == 'D':
            resultado = self.moverse_abajo()
        elif movimiento == 'L':
            resultado = self.moverse_izquierda()
        elif movimiento == 'R':
            resultado = self.moverse_derecha()
        if resultado:
            self.camino = self.camino + movimiento
            self.posicion_actual = resultado
            return True
        else:
            return False

        