class Character:

    def __init__(self,name):
        self.name = name    #public
        self._damage = 10   #protected
        self.__hp = 100     #private
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        self.__hp = value    


    def get_hp(self):
        return self.__hp
    
    def set_hp(self,hp):
        if 0<hp<100:
            self.__hp = hp


    def __str__(self):
        return f"{self.name},{self._damage},{self.__hp}"
    
    def public(self):
        pass

    def _protected(self):
        pass

    def __private(self):
        pass


char = Character("Jack")
char.hp = 800
print(char.hp)