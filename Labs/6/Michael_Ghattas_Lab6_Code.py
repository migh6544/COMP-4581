##
# Michael Ghattas
# COMP 4581 - Lab 6
# Feb/17/2025
##



class MyHashtable:
    def __init__(self, size):  # Creates an empty hashtable
        self.size = size
        self.table = [None] * size  # Table initialized with None
        self.status = ["empty"] * size  # Status table

    def __str__(self):  # For print debugging
        return str(self.table)

    def _hash(self, elem):
        """Computes hash index based on the first character's ASCII value."""
        return ord(elem[0]) % self.size

    def insert(self, elem):
        """Inserts an element using open addressing with linear probing."""
        index = self._hash(elem)

        # Linear probing: search for an empty or deleted slot
        while self.status[index] == "filled":
            index = (index + 1) % self.size  # Wrap around using modulo
        
        self.table[index] = elem
        self.status[index] = "filled"

    def member(self, elem):
        """Checks if an element exists in the table using linear probing."""
        index = self._hash(elem)

        # Linear probing: search for the element or an empty slot
        while self.status[index] != "empty":
            if self.table[index] == elem:
                return True  # Found
            index = (index + 1) % self.size  # Move to the next slot
        
        return False  # Not found

    def delete(self, elem):
        """Deletes an element from the table using linear probing."""
        index = self._hash(elem)

        # Linear probing: search for the element
        while self.status[index] != "empty":
            if self.table[index] == elem:
                self.table[index] = None
                self.status[index] = "deleted"  # Mark as deleted
                return
            index = (index + 1) % self.size  # Move to the next slot

# Testing Code
s = MyHashtable(10)
s.insert("amy")    # Hash(amy) = 97 % 10 = 7
s.insert("chase")  # Hash(chase) = 99 % 10 = 9
s.insert("chris")  # Hash(chris) = 99 % 10 = 9

print(s.member("amy"))   # True
print(s.member("chris")) # True
print(s.member("alyssa"))# False

s.delete("chase")
print(s.member("chris")) # True

print(s)  # Debugging output of the hash table



##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##