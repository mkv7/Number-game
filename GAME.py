class Game:

    def __init__(self, status, level):
        self.__status = status
        self.__level = level

    def current_status(self):
        return self.__status
    
    def current_level(self):
        return self.__level