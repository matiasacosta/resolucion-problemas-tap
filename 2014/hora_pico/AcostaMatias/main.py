from hora_pico import get_cant_turnos

def main():
    viajes = []
    cantidad_de_trenes = int(input())
    viajes = list(map(int, input().split(' ')))
    print(get_cant_turnos(cantidad_de_trenes,viajes))

if __name__ == "__main__":
    main()