def main():
    cantidad_de_nombres = input()
    nombres = []
    for i in range(int(cantidad_de_nombres)):
        nombres.append(input())    
    letra_actual = ""
    count_dr = 0
    for nombre in nombres:
        for letra in nombre:
            if letra == 'D':
                letra_actual = 'D'
            elif letra == 'R' and letra_actual == 'D':
                letra_actual = 'R'
                count_dr += 1
    print(count_dr)
    
if __name__ == "__main__":
    main()