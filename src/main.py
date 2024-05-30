from particula.particula import Particula
from enjambre.enjambre import Enjambre
from steiner.steiner import Steiner

def main():
    # Puntos iniciales del problema
    puntos = [[0, 0], [.5, 1], [.7, 0], [1, 1]]

    # Crear una instancia de Steiner
    steiner = Steiner(puntos)
    steiner.calcula_arbol_euclidianio_minimo()

    print("Peso del árbol:", steiner.peso)
    print("Árbol:", steiner.arbol.edges(data=True))

    # Optimización de partículas Steiner
    iteracion_max = 100
    cantidad_enjambres = 5
    tam_poblacion = 10
    no_max_puntos = 3

    puntos_steiner, arbol, peso = steiner.optimizacion_particulas_steiner(iteracion_max, cantidad_enjambres,
                                                                          tam_poblacion, no_max_puntos)
    print("Puntos Steiner:", puntos_steiner)
    print("Peso del árbol con puntos Steiner:", peso)


if __name__ == "__main__":
    main()

