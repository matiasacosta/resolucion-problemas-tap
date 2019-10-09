from Caja import Caja

if __name__ == "__main__":
    # Controlamos la entrada de datos
    caja = Caja(['#.##', '..##', '..##', '.E.C'])
    vertices = []
    caja.descubrir_caminos(caja.posicion_actual, vertices)
    print(vertices)
    for vertice in caja.grafo:
        print(f"Soy el vertice {vertice} y estoy conectado a " + " ".join(str(v) for v in vertice.obtener_conexiones()))