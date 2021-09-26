class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        # Insert your hashing function code
        keystr = str(key)
        hashVal = 0
        for ch in str(keystr):
            hashVal += ord(ch)
            
        return (hashVal % self.size)

    def rehash(self,key):
        # Insert your secondary hashing function code
        return

    def put(self,key,data):
        # Insert your code here to store key and data 
        return

    def get(self,key):
        # Insert your code here to get data by key
        return

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'
# Store remaining input data

# print the slot values

# print the data values

# print the value for key 52