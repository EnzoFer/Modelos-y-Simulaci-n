from modelo import modelo
from diagrama import Diagrama

def solicitar_valores():
    dt = int(1)
    t_fi = int(input("Ingrese el tiempo final (t_fi): "))
    elon = float(input("Ingrese la elongación inicial (elon): "))
    velo = float(0)
    masa = float(input("Ingrese la masa (masa): "))
    t_in = int(0)
    k_re = float(input("Ingrese la constante resorte (k_re): "))
    k_am = float(input("Ingrese la constante amortiguación (k_am): "))
    return dt, t_fi, elon, velo, masa, t_in, k_re, k_am

def predeterminado():
    dt = int(1)
    t_fi = int(250)
    elon = float(0.25)
    velo = float(0)
    masa = float(100)
    t_in = int(0)
    k_re = float(3)
    k_am = float(1)
    return dt, t_fi, elon, velo, masa, t_in, k_re, k_am


def mostrar_menu():
    print("Menú de Oscilador Lineal")
    print("1. Simular y mostrar gráficos")
    print("2. Simular y mostrar gráficos con valores predeterminados")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            dt, t_fi, elon, velo, masa, t_in, k_re, k_am = solicitar_valores()
            oscilador = modelo(dt, t_fi, elon, velo, masa, t_in, k_re, k_am)
            resultados = modelo(dt, t_fi, elon, velo, masa, t_in, k_re, k_am)
            diagrama = Diagrama()
            diagrama.diagrama_fase(resultados['Elongacion'], resultados['Velocidad'])
            diagrama.diagrama_elongacion(resultados['Segundo'], resultados['Elongacion'])

        elif opcion == 2:
            dt, t_fi, elon, velo, masa, t_in, k_re, k_am = predeterminado()
            oscilador = modelo(dt, t_fi, elon, velo, masa, t_in, k_re, k_am)
            resultados = modelo(dt, t_fi, elon, velo, masa, t_in, k_re, k_am)
            diagrama = Diagrama()
            diagrama.diagrama_fase(resultados['Elongacion'], resultados['Velocidad'])
            diagrama.diagrama_elongacion(resultados['Segundo'], resultados['Elongacion'])
        
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
