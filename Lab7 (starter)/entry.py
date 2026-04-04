class Entry():

    def __init__(self, nickname, species):
        self.__nickname = nickname
        self.__species = species

    def getNickname(self):
        return self.__nickname

    def getSpecies(self):
        return self.__species

    def __str__(self):
        return "Nickname: {} - Species: {}".format(
            self.__nickname,
            self.__species
        )