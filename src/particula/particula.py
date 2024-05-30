#La clase modela una partícula dentro de un enjambre, cuenta con las
#funciones necesarias para el modelado del ciclo de vida de una partícula
import random
class Particula:
    """
    Modela el comportamiento de una partícula para el algoritmo PSO.
    Atributos:
        posicion_inicial (tupla): posicion inicial de la particula.
        velocidad (list):Lista con la velocidad de la partícula, (cada elemento xi dentro de la tupla representa la velocidad de la partícula en la dimensión i.)
        empeora (int): Veces que empeora la aptitud de la partícula.
        fitness (int): Valor de la aptitud de la partícula.
        mejor_fitness(tupla): Tupla con la mejor posicion y aptitud en el ciclo de vida de las particulas.
        funcion_fitness (function): funcion de distancia con la que se evaluara(normalmente la distancia euclidiana)
    """
    def __init__(self, posicion_inicial, funcion_fitness,velocidad=None, empeora=0):
        self.posicion = posicion_inicial  # list
        self.velocidad = [random.random for _ in range(len(posicion_inicial))] if velocidad is None else velocidad  # list
        self.empeora = empeora  # int
        self.funcion_fitness = funcion_fitness  # function
        self.fitness = self.funcion_fitness(self.posicion, [0]*len(self.posicion))  # float
        self.mejor_fitness = (self.fitness,self.posicion)  # tuple

    def actualiza_posicion(self,limite_superior,limite_inferior):
        """
        Actualiza la posicion de las particulas.
        :param limite_superior: espacio de busqueda.
        :param limite_inferior: espacio de busqueda.
        :return:
        """
        self.posicion = [self.posicion[i] + self.velocidad[i] for i in range(len(self.posicion))]
        for i in range(len(self.posicion)):
            if self.posicion[i]>limite_superior[i]:
                self.posicion[i] = limite_superior[i]
            elif self.posicion[i]<limite_inferior[i]:
                self.posicion[i] = limite_inferior[i]

    def actualiza_velocidad(self,posicion_mejor_global,w=0.5,c1=1.25,c2=1.75):
        """
        Actualiza las particulas en base a las otras particulas.
        :param posicion_mejor_global:
        :param w: Constante de inercia.
        :param c1: Constante cognitiva.
        :param c2: Constante social.
        :return:
        """
        r1 = [random.random() for _ in range(len(self.posicion))]
        r2 = [random.random() for _ in range(len(self.posicion))]
        self.velocidad = [
            w * self.velocidad[i] +
            c1 * r1[i] * (self.mejor_fitness[1][i] - self.posicion[i])+
            c2 * r2[i] * (posicion_mejor_global[i]-self.posicion[i])
            for i in range(len(self.posicion))
        ]

    def actualiza_fitness(self):
        """
        Actualiza su aptitud de la particula en base a su posicion y la funcion fitness.
        :return:
        """
        nueva_fitness = self.funcion_fitness(self.posicion,[0]*len(self.posicion))
        if nueva_fitness > self.fitness:
            self.empeora = 0
            if nueva_fitness > self.mejor_fitness[0]:
                self.mejor_fitness = (nueva_fitness, self.posicion)
        else:
            self.empeora += 1
        self.fitness = nueva_fitness

    def debo_reiniciar(self):
        """
        Evalua si la particula debe reiniciar o no.
        :return: false o true
        """
        return self.fitness >=20

    def actualiza_estado(self,limite_inferior,limite_superior,posicion_mejor_global):
        """
        Actualiza el estado de una particula en cada generacion.
        :param limite_inferior:
        :param limite_superior:
        :param posicion_mejor_global:
        :return:
        """
        self.actualiza_velocidad(posicion_mejor_global)
        self.actualiza_posicion(limite_superior, limite_inferior)
        self.actualiza_fitness()
        if self.debo_reiniciar():
            self.posicion = [random.uniform(limite_inferior[i], limite_superior[i]) for i in range(len(self.posicion))]
            self.velocidad = [random.random() for _ in range(len(self.posicion))]
            self.empeora = 0
            self.fitness = self.funcion_fitness(self.posicion, [0] * len(self.posicion))
            self.mejor_fitness = (self.fitness, self.posicion)