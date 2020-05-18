class HashTable:
    def __init__(self, size):
        self.table = [0 for i in range(size)]
        self.keys =[]

    def get(self, key):
        return self.table[self.key_to_add(key)]

    def key_to_add(self, key):
        hash_value = hash(key)
        return hash_value % 8

    def add(self, key, value):
        address = self.key_to_add(key)
        self.keys.append(key)
        self.table[address] = value

    def desc(self):
        for key_i in self.keys:
            print(key_i, self.table[self.key_to_add(key_i)] )

