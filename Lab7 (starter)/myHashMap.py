"""
WRITE YOUR PROGRAM HEADER HERE

Adapted from UCSD CSE12
"""


class MyHashMap:
    def __init__(self, load_factor=0.75, initial_capacity=16):
        self.load_factor = load_factor
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    """
    Resizes the self.buckets array when the load_factor is reached.
    """
    def resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        old_size = self.size
        self.size = 0

        for bucket in old_buckets:
            for entry in bucket:
                self.put(entry.getKey(), entry.getValue())

        self.size = old_size

    """
    Adds the specified key, value pair to the MyHashMap if
    the key is not already in the MyHashMap. If adding a new key would
    surpass the load_factor, resize the MyHashMap before adding the key.
    Return true if successfully added to the MyHashMap.
    Raise an exception if the key is None.
    """
    def put(self, key, value):
        if key is None:
            raise Exception("Key cannot be None")

        if self.containsKey(key):
            return False

        if (self.size + 1) / self.capacity > self.load_factor:
            self.resize()

        keyhash = hash(key)
        index = keyhash % self.capacity
        self.buckets[index].append(MyHashMapEntry(key, value))
        self.size += 1
        return True

    """
    Replaces the value that maps to the given key if it is present.
    Input: key is the key whose mapped value is being replaced.
           newValue is the value to replace the existing value with.
    Return true if the key was in this MyHashMap and replaced successfully.
    Raise an exception if the key is None.
    """
    def replace(self, key, newValue):
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                entry.setValue(newValue)
                return True

        return False

    """
    Remove the entry corresponding to the given key.
    Return true if an entry for the given key was removed.
    Raise an exception if the key is None.
    """
    def remove(self, key):
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for i, entry in enumerate(bucket):
            if entry.getKey() == key:
                del bucket[i]
                self.size -= 1
                return True

        return False

    """
    Adds the key, value pair to the MyHashMap if it is not present.
    Otherwise, replace the existing value for that key with the given value.
    Raise an exception if the key is None.
    """
    def set(self, key, value):
        if key is None:
            raise Exception("Key cannot be None")

        if self.containsKey(key):
            self.replace(key, value)
        else:
            self.put(key, value)

    """
    Return the value of the specified key. If the key is not in the
    MyHashMap, return None.
    Raise an exception if the key is None.
    """
    def get(self, key):
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                return entry.getValue()

        return None

    """
    Return the number of key, value pairs in this MyHashMap.
    """
    def get_size(self):
        return self.size

    """
    Return true if the MyHashMap contains no elements, and
    false otherwise.
    """
    def isEmpty(self):
        return self.size == 0

    """
    Return true if the specified key is in this MyHashMap.
    Raise an exception if the key is None.
    """
    def containsKey(self, key):
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                return True

        return False

    """
    Return a list containing the keys of this MyHashMap.
    If it is empty, return an empty list.
    """
    def keys(self):
        key_list = []

        for bucket in self.buckets:
            for entry in bucket:
                key_list.append(entry.getKey())

        return key_list


class MyHashMapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def setValue(self, new_value):
        self.value = new_value


if __name__ == "__main__":
    pass