"""
Especificar los tipos de objetos para crear usando una instancia prototípica,
y cree nuevos objetos copiando este prototipo.
* Copia de objetos con los mismos valores
"""

import copy


class Prototype:
    """
    Example class to be copied.
    """

    pass


def main():
    prototype = Prototype()
    prototype_copy = copy.deepcopy(prototype)


if __name__ == "__main__":
    main()