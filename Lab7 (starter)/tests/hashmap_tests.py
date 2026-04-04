import pytest
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from myHashMap import MyHashMap


# put()

def test_put_into_empty_hashmap():
    m = MyHashMap()
    assert m.put("a", 10) is True
    assert m.get("a") == 10
    assert m.get_size() == 1


def test_put_into_nonempty_without_surpassing_load_factor():
    m = MyHashMap()
    m.put("a", 1)
    m.put("b", 2)
    assert m.put("c", 3) is True
    assert m.get("a") == 1
    assert m.get("b") == 2
    assert m.get("c") == 3
    assert m.get_size() == 3


def test_put_into_nonempty_and_surpass_load_factor():
    m = MyHashMap(load_factor=0.75, initial_capacity=4)
    m.put("a", 1)
    m.put("b", 2)
    m.put("c", 3)
    old_capacity = m.capacity

    assert m.put("d", 4) is True
    assert m.capacity > old_capacity
    assert m.get("a") == 1
    assert m.get("b") == 2
    assert m.get("c") == 3
    assert m.get("d") == 4
    assert m.get_size() == 4


def test_put_a_key_that_already_exists():
    m = MyHashMap()
    m.put("a", 10)
    assert m.put("a", 99) is False
    assert m.get("a") == 10
    assert m.get_size() == 1


# replace()

def test_replace_key_already_present():
    m = MyHashMap()
    m.put("a", 10)
    assert m.replace("a", 20) is True
    assert m.get("a") == 20


def test_replace_key_not_present():
    m = MyHashMap()
    assert m.replace("a", 20) is False
    assert m.get("a") is None


# remove()

def test_remove_key_present():
    m = MyHashMap()
    m.put("a", 10)
    assert m.remove("a") is True
    assert m.get("a") is None
    assert m.get_size() == 0


def test_remove_key_not_present():
    m = MyHashMap()
    assert m.remove("a") is False
    assert m.get_size() == 0


# set()

def test_set_key_already_present():
    m = MyHashMap()
    m.put("a", 10)
    m.set("a", 50)
    assert m.get("a") == 50
    assert m.get_size() == 1


def test_set_key_not_present():
    m = MyHashMap()
    m.set("a", 50)
    assert m.get("a") == 50
    assert m.get_size() == 1


# get()

def test_get_key_present():
    m = MyHashMap()
    m.put("a", 10)
    assert m.get("a") == 10


def test_get_key_not_present():
    m = MyHashMap()
    assert m.get("a") is None


# get_size()

def test_get_size_empty():
    m = MyHashMap()
    assert m.get_size() == 0


def test_get_size_few_items():
    m = MyHashMap()
    m.put("a", 1)
    assert m.get_size() == 1


def test_get_size_many_items():
    m = MyHashMap()
    for i in range(100):
        m.put(f"key{i}", i)
    assert m.get_size() == 100


# isEmpty()

def test_is_empty_on_empty_hashmap():
    m = MyHashMap()
    assert m.isEmpty() is True


def test_is_empty_on_nonempty_hashmap():
    m = MyHashMap()
    m.put("a", 1)
    assert m.isEmpty() is False


# containsKey()

def test_contains_key_that_exists():
    m = MyHashMap()
    m.put("a", 1)
    assert m.containsKey("a") is True


def test_contains_key_that_does_not_exist():
    m = MyHashMap()
    assert m.containsKey("a") is False


# keys()

def test_keys_empty_hashmap():
    m = MyHashMap()
    assert m.keys() == []


def test_keys_nonempty_hashmap():
    m = MyHashMap()
    m.put("a", 1)
    m.put("b", 2)
    result = m.keys()
    assert "a" in result
    assert "b" in result
    assert len(result) == 2