#Clase que modela un conjunto de partículas, ésta se encarga del manejo
#del líder del enjambre.
import copy

from src.particula.particula import Particula


class Enjambre:
    """
    Modela un ejambre (conjunto de partículas), se lleva acabo la ejecución del algoritmo
    de optimización por enjambre de partículas.

    Atributos:
        poblacion (lista): Lista de partículas dentro del enjambre.

        mejor_globla(tupla): Partícula con la mejor aptitud en el enjambre.

        fitness(function): Función evaluación.
    """
    def __init__(self, tam_poblacion,posicion_inicial, funcion_fitness):
        self.poblacion = [Particula(posicion_inicial, funcion_fitness) for _ in range(tam_poblacion)]
        self.mejor_global = max(self.poblacion, key=lambda p: p.fitness)
        self.fitness = funcion_fitness  # function

    def optimizacion_enjambre_particulas(self,limite_inferior, limite_superior, cantidad_iteraciones):
        contador_nejora =0 #Contador

        for _ in range(cantidad_iteraciones):
            for particula in self.poblacion:
                particula.actualiza_estado(limite_inferior, limite_superior, self.mejor_global.posicion)

                #Verifica si la aptitud de la particula actual es mejor que la global
                if particula.fitness > self.mejor_global.fitness:
                    self.mejor_global = copy.deepcopy(particula)
                    contador_nejora = 0 #Reiniciar el contador si se encuentra una mejor aptitud
                else:
                    contador_nejora += 1

            #Criterio de paro:
            if contador_nejora >= 35:
                break
        return  self.mejor_global
