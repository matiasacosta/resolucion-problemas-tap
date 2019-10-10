if __name__ == "__main__":
    cantidad_legisladores = input()
    legisladores = input()
    contadores = []
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
    elif contadores[0] >= cantidad_legisladores / 2:
        print("INDECISOS")
