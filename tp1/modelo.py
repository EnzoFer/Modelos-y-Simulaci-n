def modelo(dt, t_fi, elon, velo, masa, t_in, k_re, k_am):

    """
    dt = Diferencial de tiempo
    t_fi = Tiempo final
    t_in = Tiempo inicial
    velo = velocidad
    masa = masa
    k_re = constante elastica del resorte
    k_am = constante de amortiguacion
    acel = aceleracion
    """

    f_ac = 0
    elon_list = []
    velo_list = []
    time_list = []

    for seg in range(t_in, t_fi + 1, dt):
        acel = f_ac / masa
        velo = velo + dt * acel
        elon = elon + dt * velo
        f_re = -1 * k_re * elon
        f_am = -1 * k_am * velo
        f_ac = f_re + f_am

        elon_list.append(elon)
        velo_list.append(velo)
        time_list.append(seg)

    list_dictionary = {'Elongacion': elon_list, 'Velocidad': velo_list, 'Segundo': time_list}
    return list_dictionary
