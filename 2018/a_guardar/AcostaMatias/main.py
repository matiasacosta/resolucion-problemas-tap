from Caja import Caja

if __name__ == "__main__":
    # Controlamos la entrada de datos
    caja = Caja(['#.##', '..##', '..##', '.E.C'])
    print(caja.get_posicion_inicial())

    def descubir_caminos(posicion):
    for movimiento in ['U', 'D', 'L', 'R']:
        nueva_posicion = moverme(movimiento, posicion)
        if nueva_posicion and nueva_posicion not in vertices:
            vertices.append(nueva_posicion)
            descubir_caminos(nueva_posicion)
    