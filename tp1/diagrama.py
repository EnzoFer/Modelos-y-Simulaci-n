import matplotlib.pyplot as plt

class Diagrama():

    def diagrama_fase(self, elon_list, velo_list):
        plt.figure()
        plt.plot(elon_list, velo_list, color = "green")
        plt.xlabel('Elongacion')
        plt.ylabel('Velocidad')
        plt.title('Diagrama de Fase')
        plt.show(block=False)

    def diagrama_elongacion(self, time_list, elon_list):
        plt.figure()
        plt.plot(time_list, elon_list, color='red')
        plt.xlabel('Tiempo')
        plt.ylabel('Elongación')
        plt.title('Diagrama de Elongación')
        plt.show(block=False)
