import os, sys

sys.path.append(os.path.dirname(__file__))

from myHashMap import MyHashMap
from entry import Entry


class Box:

    def __init__(self):
        self.nicknameMap = MyHashMap()
        self.populateBox()

    def populateBox(self, inputFile='entries.txt'):
        with open(inputFile, 'r') as f:
            for line in f:
                nickname, species = line.split()
                self.add(nickname, species)

    def add(self, nickname, species):
        if self.nicknameMap.containsKey(nickname):
            return False

        entry = Entry(nickname, species)
        return self.nicknameMap.put(nickname, entry)

    def find(self, nickname, species):

        entry = self.nicknameMap.get(nickname)

        if entry is None:
            return None

        if entry.getSpecies() == species:
            return entry

        return None

    def findAllNicknames(self):

        if self.nicknameMap.isEmpty():
            return None

        return self.nicknameMap.keys()

    def findEntryByNickname(self, nickname):

        return self.nicknameMap.get(nickname)

    def removeByNickname(self, nickname):

        return self.nicknameMap.remove(nickname)

    def removeEntry(self, nickname, species):

        entry = self.nicknameMap.get(nickname)

        if entry is None:
            return False

        if entry.getSpecies() != species:
            return False

        return self.nicknameMap.remove(nickname)


if __name__ == '__main__':
    Box()