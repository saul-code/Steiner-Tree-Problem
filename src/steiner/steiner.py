#La clase modela el problema del árbol de Steiner euclideano mínimo, maneja
#el cálculo del peso de los árboles Steiner.
import networkx as nx
import numpy as np
from scipy.spatial.distance import  euclidean


class Steiner:
    """
    Modela el problema del arbol de steiner euclidiano minimo.

    Atributos:

        puntos(Lista): Lista de puntos pertenecientes al conjunto inicial del problema.

        arbol(lista): Lista de aristas del arbol euclidiano de peso minimo.

        peso(int): Valor numerico del peso total del arbol.
    """
    def __init__(self, puntos):
        self.puntos = puntos  # list
        self.arbol = nx.Graph()  # nx.Graph
        self.peso = None  # float

    def calcula_arbol_euclidianio_minimo(self):
        G = nx.Graph()
        for i, p1 in enumerate(self.puntos):
            for j, p2 in enumerate(self.puntos):
                if i < j:
                    G.add_edge(i, j, weight=euclidean(p1, p2))

        T = nx.minimum_spanning_tree(G)
        self.arbol = T
        self.peso = self.calcula_peso_total_arbol()

    def calcula_peso_total_arbol(self):
        peso_total = 0
        for (u, v, d) in self.arbol.edges(data=True):
            peso_total += d['weight']
        self.peso = peso_total
        return peso_total

    def calcula_arbol_con_punto(self, punto):
        puntos_nuevos = self.puntos + [punto]
        steiner = Steiner(puntos_nuevos)
        steiner.calcula_arbol_euclidianio_minimo()
        return steiner.arbol


    def obten_limite_superior(self):
        return np.max(self.puntos, axis=0).tolist()

    def obten_limite_inferior(self):
        return  np.min(self.puntos, axis=0).tolist()

    def fitness_problema_steiner(self,punto):
        steiner = Steiner(self.puntos + [punto])
        steiner.calcula_arbol_euclidianio_minimo()
        return steiner.peso

    def optimizacion_particulas_steiner(self,iteracion_max, cantidad_enjambres, tam_poblacion, no_max_puntos ):
        limite_inferior = self.obten_limite_inferior()
        limite_superior = self.obten_limite_superior()
        puntos_steiner = []

        while len(puntos_steiner) < no_max_puntos and len(puntos_steiner) < cantidad_enjambres:
            coordenadas_iniciales = [
                [np.random.uniform(limite_inferior[i], limite_superior[i]) for i in range(len(limite_inferior))]
                for _ in range(tam_poblacion)
            ]

            for coordenadas in coordenadas_iniciales:
                nuevo_arbol = self.calcula_arbol_con_punto(coordenadas)
                nuevo_peso = self.fitness_problema_steiner(coordenadas)

                if nuevo_peso < self.peso:
                    puntos_steiner.append(coordenadas)
                    self.puntos.append(coordenadas)
                    self.calcula_arbol_euclidianio_minimo()
                    break

        return self.puntos, self.arbol, self.peso

