NOTAS = [
    "DO", "DO#", "RE", "RE#", "MI", "FA", "FA#", "SOL", "SOL#", "LA", "LA#", "SI"
]

def get_nota(offset, nota):
    return NOTAS[NOTAS.index(nota) - offset]
