#Private attribute and method to access it

class Secret:
    def __init__(self, value):
        self.__hidden = value

    def get_hidden(self):
        return self.__hidden
    

