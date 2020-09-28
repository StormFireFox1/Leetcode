from collections import defaultdict
from random import choice

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # collection is the array storing each element
        self.collection = []
        # indices is the hashtable described in the solution
        self.indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.collection.append(val)
        self.indices[val].add(len(self.collection) - 1)
        return len(self.indices[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.indices[val]:
            indexOfVal = self.indices[val].pop()
            lastElement = self.collection[-1]
            # Swap them!
            self.collection[indexOfVal] = lastElement
            if self.indices[lastElement]:
                # Add the new index for the last element
                self.indices[lastElement].add(indexOfVal)
                # Remove the old index
                self.indices[lastElement].discard(len(self.collection) - 1)
                # Note the add and pop, because self.indices contains Sets, not Lists
            self.collection.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.collection)
