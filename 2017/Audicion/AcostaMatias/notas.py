#!/usr/bin/python3

def darNotaAbuelita(corrimiento, nota_abuelita):
    notas = ["DO","DO#","RE","RE#","MI","FA","FA#","SOL","SOL#","LA","LA#","SI"]

    #Resta el corrimiento al indice donde se encuentra la nota de la abuelita
    return notas[notas.index(nota_abuelita)-int(corrimiento)]

if  __name__ == "__main__" :
    cadena_de_entrada = input()
    arreglo_de_palabras = cadena_de_entrada.split(" ",2)
    corrimiento = arreglo_de_palabras[0]
    nota_abuelita = arreglo_de_palabras[1]
    print(darNotaAbuelita(corrimiento, nota_abuelita))


