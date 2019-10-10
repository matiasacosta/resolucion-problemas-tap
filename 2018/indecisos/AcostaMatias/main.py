if __name__ == "__main__":
    cantidad_legisladores = int(input())
    legisladores = input()
    contadores = [0,0,0]
    for c in legisladores:
        if c == 'P':
            contadores[0] += 1
        elif c == 'N':
            contadores[1] += 1
        elif c == 'I':
            contadores[2] += 1

    if contadores[0] > cantidad_legisladores / 2:
        print("SI")
    elif contadores[0] > cantidad_legisladores / 2:
        print("NO")
    else:
        print("INDECISOS")
