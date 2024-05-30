#Clase que modela un conjunto de partículas, ésta se encarga del manejo
#del líder del enjambre.
class Enjambre:
    def __init__(self, poblacion, mejor_global, fitness):
        self.poblacion = poblacion  # list
        self.mejor_global = mejor_global  # tuple
        self.fitness = fitness  # function

    def optimizacion_enjambre_particulas(self):
        pass

