from Caja import Caja

if __name__ == "__main__":
    # Controlamos la entrada de datos
    caja = Caja(['#.##', '..##', '..##', '.E.C'])
    print(caja.get_posicion_inicial())
    