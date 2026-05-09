class Node():
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class HashTable:
    def __init__(self):
        self.hash_table = []
        self.table_len = 0
        self.table_capacity = 0


    def hash_function(self, key) -> int:
        pass

    
    def hash_to_index(self, hash) -> int:

    
    def insert_key_val(self, key, val): 
        pair_node = Node(key, val)
        hash = self.hash_function(key)
        index = self.hash_to_index(hash)
        pass


    def delete_key_val(self, key)
        pass


    def increase_capacity(self, )
