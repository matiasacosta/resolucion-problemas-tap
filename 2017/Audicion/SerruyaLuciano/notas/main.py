from notas import get_nota

def main():
    while True:
        entrada = input()
        entrada = entrada.split()
        offset = int(entrada[0])
        nota = entrada[1]

        print(get_nota(offset, nota))

if __name__ == "__main__":
    main()
