from AcostaMatias.resolucion.caja import Caja, resolucion

if __name__ == "__main__":
    # Controlamos la entrada de datos
    tamanio_grilla = input()
    tamanio_grilla = tamanio_grilla.split(' ')
    altura_grilla, ancho_grilla = int(tamanio_grilla[0]), int(tamanio_grilla[1])
    grilla = []
    for i in range(altura_grilla):
        fila_grilla = input()
        grilla.append(fila_grilla)
    camino = resolucion(grilla)
    if camino:
        print(len(camino))
        print(camino)
    else:
        print(-1)
