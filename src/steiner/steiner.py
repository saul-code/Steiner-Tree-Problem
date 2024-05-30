#La clase modela el problema del árbol de Steiner euclideano mínimo, maneja
#el cálculo del peso de los árboles Steiner.
import networkx as nx

class Steiner:
    def __init__(self, puntos):
        self.puntos = puntos  # list
        self.arbol = nx.Graph()  # nx.Graph
        self.peso = None  # float

    def calcula_arbol_euclidianio_minimo(self):
        pass

    def calcula_peso_total_arbol(self):
        pass

    def calcula_arbol_con_punto(self, punto):
        pass

    def obten_limite_superior(self):
        pass

    def obten_limite_inferior(self):
        pass

    def fitness_problema_steiner(self):
        pass

    def optimizacion_particulas_steiner(self):
        pass

