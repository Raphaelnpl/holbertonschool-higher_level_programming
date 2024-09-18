class Square:
    """Représente un carré"""

    def __init__(self, size=0):
        """Initialise une instance de Square avec un attribut privé size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Retourne l'aire du carré"""
        return self.__size ** 2
