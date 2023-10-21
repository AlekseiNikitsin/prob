class R:

    #определяем инициализатор
    def __init__(self):
        self.public = "это public поле "
        self._protected = "это protected поле "
        self.__private = "это private поле "
    def pablic_met(self): print("это public метод")
    def _protected_met(self): print("это protected метод")
    def __private_met(self): print("это private метод")
obg = R()
print(obg.public)
obg.pablic_met()
print(obg._protected)
obg._protected_met()
print(obg.__private_met)
obg.__private_met
