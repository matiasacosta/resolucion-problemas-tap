from materia.Materia import Materia

def get_materia(materias, _id):
    def _filter_materias_by_id(materia):
        return materia.sos_materia(_id)

    _materias = list(filter(_filter_materias_by_id, materias))
    # Devolvemos _materias[0] si es que _materias tiene algun elemento
    # si no False
    return _materias and _materias[0] or False
    # return _materias[0] if _materias else False

    # El equivalente con 'for' del codigo de arriba
    # for materia in materias:
        # if materia.sos_materia(_id):
            # return materia

    # return False

def get_cant_registrables(materias):
    # dame las materias registrables
    materias_registrables = filter(lambda materia: materia,
        map(lambda materia: materia.sos_registrable(), materias))

    # devolvemos la cantidad de materias registrables
    return len(list(materias_registrables))

def main():
    #procesamos primer linea
    _input = input().split()
    cant_materias = int(_input[0])
    cant_correlatividades = int(_input[1])

    materias = []

    #ahora procesamos las materias y sus correlativas
    for i in range(cant_correlatividades):
        _input = input().split()
        id_materia_correlativa = int(_input[0])
        materia_correlativa = get_materia(materias, id_materia_correlativa) or Materia(id_materia_correlativa)

        if materia_correlativa not in materias:
            materias.append(materia_correlativa)

        id_materia = int(_input[1])
        materia = get_materia(materias, id_materia) or Materia(id_materia)

        if materia not in materias:
            materias.append(materia)

        materia.agregar_correlativa(materia_correlativa)

    #procesamos ultima linea
    _input = input().split()
    for id_materia in _input:
        materia = get_materia(materias, int(id_materia))
        materia.aprobar()
        print(get_cant_registrables(materias))


if __name__ == "__main__":
    main()
