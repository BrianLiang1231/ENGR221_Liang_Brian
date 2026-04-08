


class MyHashMap:
    def __init__(self, load_factor=0.75, initial_capacity=16):
        self.load_factor = load_factor
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    
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

    
    def set(self, key, value):
        if key is None:
            raise Exception("Key cannot be None")

        if self.containsKey(key):
            self.replace(key, value)
        else:
            self.put(key, value)

   
    def get(self, key):
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                return entry.getValue()

        return None

   
    def get_size(self):
        return self.size

    
    def isEmpty(self):
        return self.size == 0

   
    def containsKey(self, key):
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                return True

        return False

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
