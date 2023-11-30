class Player:
    def __init__(self, name, age, level):
        self.__name = name
        self.__age = age
        self.__level = level
    
    def tell_name(self):
        return self.__name
    def tell_age(self):
        return self.__age
    def tell_level(self):
        return self.__level
    
    