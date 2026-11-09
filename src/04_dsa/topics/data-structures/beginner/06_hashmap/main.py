"""
 * +-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
 * |                                                                                                                                                                   |
 * | 🟡 A hashmap, is a data structure what gives constant "o(1)" time complexity on all operations like "insert", "delete", "update", "read".                         |
 * |                                                                                                                                                                   |
 * | 🟡 Hashmap uses array data structure along with hash function to implement it, "hash function" gives unique index but it's not always a case.                     |
 * |                                                                                                                                                                   |
 * | 🟡 Collision, it's happen when hash function gives index which already filled with some-other data, on these case we simply used few techniques to handle it.      |
 * |                                                                                                                                                                   |
 * |    🔵 "Open Addressing", In this technique hashmap only uses single array, when collision happens then it try to find next empty slot and put into there.         |
 * |    🔵 "Closed Addressing", Still using single array, but this time when collision happens we replace that index with "linkedlist", and insert into the list.      |
 * |                                                                                                                                                                   |
 * | 🟡 Load Factor, "items stored / array size", when it crosses certain limit like "0.7", the array resizes and every item rehashed.                                 |
 * |                                                                                                                                                                   |
 * +-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
 """

class HashMap:
    def __init__(self):
        self._data = {}
    def insert(self, key, value):
        self._data[key] = value
    def get(self, key, default=None):
        return self._data.get(key, default)
    def delete(self, key):
        return self._data.pop(key, None)
