import random


class HashTable:
    """Hash table with chaining and nonnegative integer keys."""

    def __init__(self, capacity=8):
        if capacity < 1:
            raise ValueError("Capacity must be at least 1")

        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

        # Prime defining the supported key range.
        self.p = 2**61 - 1
        self.a = random.randrange(1, self.p)
        self.b = random.randrange(self.p)

    def _hash(self, key):
        if not isinstance(key, int) or not 0 <= key < self.p:
            raise ValueError(f"Key must be an integer from 0 to {self.p - 1}")

        return ((self.a * key + self.b) % self.p) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        # Update an existing key.
        for position, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[position] = (key, value)
                return

        # Resize before adding a new key if necessary.
        if (self.size + 1) / self.capacity > 0.75:
            self._resize()
            index = self._hash(key)

        self.buckets[index].append((key, value))
        self.size += 1

    def search(self, key):
        index = self._hash(key)

        for existing_key, value in self.buckets[index]:
            if existing_key == key:
                return value

        raise KeyError(key)

    def delete(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for position, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[position]
                self.size -= 1
                return

        raise KeyError(key)

    def _resize(self):
        old_buckets = self.buckets

        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]

        # Recalculate every key's bucket using the new capacity.
        for bucket in old_buckets:
            for key, value in bucket:
                index = self._hash(key)
                self.buckets[index].append((key, value))

    def load_factor(self):
        return self.size / self.capacity


if __name__ == "__main__":
    table = HashTable()

    table.insert(10, "Apple")
    table.insert(20, "Banana")
    table.insert(30, "Cherry")

    print("Key 20:", table.search(20))

    table.insert(20, "Blueberry")
    print("Updated key 20:", table.search(20))

    table.delete(10)
    print("Number of items:", table.size)
    print("Load factor:", table.load_factor())