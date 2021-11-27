class Stack:
    __slots__ = ['__size','__top']

    def __init__(self):

        self.__size = 0
        self.__top = None
    
    def get_size(self):
        return self.__size
    
    def get_is_empty(self):
        return self.__top == None
    
    def is_empty(self):
        