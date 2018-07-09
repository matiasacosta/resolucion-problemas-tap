def get_colision(viaje1,viaje2):
    """
    Funcion que recibe dos tuplas del tipo (numero_origen,numero_destio)
    que corresponden a dos viajes y retorna si existe colision entre dichos viajes
    """
    return (viaje1[0] > viaje2[0] and viaje1[1] < viaje2[1]) or \
     (viaje1[0] < viaje2[0] and viaje1[1] > viaje2[1])
    
def get_cant_turnos(nro_servicios_tren,recorrido_trenes):
    """
    Funcion que devuelve la cantidad minima de viajes que se deben realizar sin que existan colisiones
    """
    cant_viajes = [] # Estructura que contendrá listas con los viajes que se pueden realizar en simultaneo
    colisionan = False
    for i in range(nro_servicios_tren): #Itero la lista de viajes
        viaje_agregado = False
        if i == 0: #Si es el primer viaje lo agrego a una lista para poder comparar luego
            cant_viajes.append([(i+1,recorrido_trenes[i])])
        else:
            for turno_viaje in cant_viajes: #Itero por cada turno de viajes creados
                for viaje in turno_viaje: #Itero por cada viaje para detectar colision con el viaje actual
                    colisionan = get_colision((i+1,recorrido_trenes[i]),viaje)
                    if colisionan: #En el caso que exista colision paso a verificar otro turno o lo creo posteriormente
                        break
                if not colisionan:# En el caso de no colisionar agrego el viaje al turno
                    turno_viaje.append((i+1,recorrido_trenes[i]))
                    viaje_agregado = True
                    break
            if not viaje_agregado: #Si no se agrego el viaje luego de la iteracion anterior debo crear un nuevo turno.
                cant_viajes.append([(i+1,recorrido_trenes[i])])

    return len(cant_viajes)#Finalmente devuelvo la cantidad de turnos generados.
    
       


        