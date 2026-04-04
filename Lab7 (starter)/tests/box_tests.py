import pytest
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from box import Box
from myHashMap import MyHashMap


# add()

def test_add_nickname_that_does_not_exist():
    b = Box()
    nickname = "ZZZ_Fluffy_123"
    assert b.add(nickname, "cat") is True

    entry = b.findEntryByNickname(nickname)
    assert entry is not None
    assert entry.getNickname() == nickname
    assert entry.getSpecies() == "cat"


def test_add_nickname_that_already_exists():
    b = Box()
    nickname = "ZZZ_Fluffy_456"
    b.add(nickname, "cat")

    assert b.add(nickname, "dog") is False

    entry = b.findEntryByNickname(nickname)
    assert entry is not None
    assert entry.getNickname() == nickname
    assert entry.getSpecies() == "cat"


# find()

def test_find_nickname_and_species_that_exists():
    b = Box()
    nickname = "ZZZ_Buddy_123"
    b.add(nickname, "dog")

    entry = b.find(nickname, "dog")
    assert entry is not None
    assert entry.getNickname() == nickname
    assert entry.getSpecies() == "dog"


def test_find_nickname_and_species_that_does_not_exist():
    b = Box()
    nickname = "ZZZ_Buddy_456"
    b.add(nickname, "dog")

    assert b.find(nickname, "cat") is None
    assert b.find("ZZZ_Ghost_999", "dog") is None


# findAllNicknames()

def test_find_all_nicknames_of_populated_box():
    b = Box()
    name1 = "ZZZ_Milo_123"
    name2 = "ZZZ_Luna_456"

    b.add(name1, "cat")
    b.add(name2, "rabbit")

    names = b.findAllNicknames()
    assert names is not None
    assert name1 in names
    assert name2 in names


def test_find_all_nicknames_of_empty_box():
    b = Box()
    b.nicknameMap = MyHashMap()

    assert b.findAllNicknames() is None


# findEntryByNickname()

def test_find_entry_by_nickname_that_exists():
    b = Box()
    nickname = "ZZZ_Rocky_123"
    b.add(nickname, "dog")

    entry = b.findEntryByNickname(nickname)
    assert entry is not None
    assert entry.getNickname() == nickname
    assert entry.getSpecies() == "dog"


def test_find_entry_by_nickname_that_does_not_exist():
    b = Box()
    assert b.findEntryByNickname("ZZZ_Missing_123") is None


# removeByNickname()

def test_remove_by_nickname_that_exists():
    b = Box()
    nickname = "ZZZ_Nemo_123"
    b.add(nickname, "fish")

    assert b.removeByNickname(nickname) is True
    assert b.findEntryByNickname(nickname) is None


def test_remove_by_nickname_that_does_not_exist():
    b = Box()
    assert b.removeByNickname("ZZZ_Nobody_123") is False


# removeEntry()

def test_remove_entry_of_nickname_and_species_that_exists():
    b = Box()
    nickname = "ZZZ_Kiwi_123"
    b.add(nickname, "bird")

    assert b.removeEntry(nickname, "bird") is True
    assert b.findEntryByNickname(nickname) is None


def test_remove_entry_of_nickname_and_species_that_is_not_in_box():
    b = Box()
    nickname = "ZZZ_Kiwi_456"
    b.add(nickname, "bird")

    assert b.removeEntry(nickname, "cat") is False
    assert b.removeEntry("ZZZ_Ghost_456", "bird") is False