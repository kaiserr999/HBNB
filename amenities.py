class Amenity:
    def __init__(self, name):
        self.__id = None
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Amenity name cannot be empty")
        if len(value) > 50:
            raise ValueError("Amenity name too long (max 50 characters)")
        self.__name = value
