'''
Seth Stoudenmier
2/29/16

Honor pledge: All work was done by myself.

Purpose: Purpose of this file is to create an Inventory objects that contains
many different Inventory Item objects. There are also a host of methods that
may be used to change or analyze the inventory.
'''

from InvItem import InvItem

class Inventory:

    '''
    Constructor for the inventory class.
    @param: capacity - the maximum capacity of the inventory
    '''
    def __init__(self, capacity=100):
        self.inv = []
        if (capacity < 1):
            self.capacity = 1
        else:
            self.capacity = capacity

    '''
    Check if the inventory is empty.
    @return: true if the inventory is empty; false otherwise
    '''
    def isEmpty(self):
        if (len(self.inv) == 0):
            return True
        else:
            return False

    '''
    Get the number of items in the inventory.
    @return: the number of items in the inventory
    '''
    def getNumItems(self):
        return len(self.inv)

    '''
    Case sensitive search for an item in the inventory.
    @param: name - the name of the item to search for
    @return: the number of items that fit the provided name
    '''
    def getNumItemsByName(self, name):
        temp = 0
        for i in self.inv:
            if (i.getName() == name):
                temp+=1
        return temp

    '''
    Gets the combined total weight of all items in the inventory.
    @return: the total weight of all items in the inventory
    '''
    def getTotalWeight(self):
        temp = 0
        for i in self.inv:
            temp+=i.getWeight()
        return temp

    '''
    Gets the capacity of the inventory.
    @return: the max capacity of the inventory
    '''
    def getCapacity(self):
        return self.capacity

    '''
    Sets the capacity of the inventory.
    @param: capacity - the new desired capacity for the inventory
    @return: returns true if the capacity was able to be set; returns false otherwise
    '''
    def setCapacity(self, capacity):
        if (self.getTotalWeight() >= capacity):
            self.capacity = capacity
            return True
        else:
            return False

    '''
    Determines if an item is able to fit in the inventory.
    @param: weight - the weight of the item that is wanting to be added
    @return: returns true if the item is able to fit; returns false otherwise
    '''
    def isFits(self, weight):
        return (self.getTotalWeight() + weight) <= self.getCapacity()

    '''
    Adds an item to the inventory if it will fit in the inventory.
    @param: invItem - an inventory item to be added
    @return: returns true if the item was able to be added; false otherwise
    '''
    def addItem(self, invItem):
        if (self.isFits(invItem.getWeight())):
            self.inv.append(invItem)
            return True
        else:
            return False

    '''
    Finds the index in the inventory of the first occurence of an item.
    @param: name - the name of an item to search for
    @return: the index of the item; returns -1 if item name not found
    '''
    def findIndex(self, name):
        for i in range(len(self.inv)):
            if (self.inv[i].getName() == name):
                return i
        return -1

    '''
    Check to see if the item name provided is in the inventory.
    @param: name - the name of the item to search for
    @return: true if the item name is in the inventory; false otherwise
    '''
    def isContains(self, name):
        if (self.findIndex(name) >= 0):
            return True
        else:
            return False

    '''
    Gets the item with a provided name from the inventory.
    @param: name - the name of an item to get
    @return: the item with the provided name; if item not in the inventory then
             value of None is returned
    '''
    def getItem(self, name):
        i = self.findIndex(name)
        if (i >= 0):
            return self.inv[i]
        else:
            return None

    '''
    Removes an item with the provided name from the inventory.
    @param: name - the name of an item to be removed
    @return: the first item that is found with the provided name; return value of
             None otherwise
    '''
    def removeItem(self, name):
        i = self.findIndex(name)
        if (i >= 0):
            return self.inv.pop(i)
        else:
            return None

    '''
    Deletes all items from the inventory.
    '''
    def clear(self):
        for i in range(len(self.inv)):
            del(self.inv[0])

    '''
    Prints all items in the inventory ordered by their weight.
    '''
    def printByWeight(self):
        def weightKey(invItem):
            return invItem.getWeight()
        temp = sorted(self.inv, key=weightKey)
        for i in temp:
            print("-------------------")
            print(i)

    '''
    Prints all items in the inventory ordered by their kind.
    '''
    def printByKind(self):
        def kindKey(invItem):
            return invItem.getKind()
        temp = sorted(self.inv, key=kindKey)
        for i in temp:
            print("-------------------")
            print(i)

            
'''
if __name__ == "__main__":
    inv = Inventory(12)
    inv.addItem(InvItem("HEALTH", "water", 5, 20))
    inv.addItem(InvItem("HEALTH", "steak", 2, 10))
    inv.addItem(InvItem("POTION", "restore", 2, 30))
    inv.addItem(InvItem("WEAPON", "staff", 3, 5))
    inv.addItem(InvItem("ARMOR", "wood shield", 4, 5))
    print(inv.getNumItems())
    print(inv.getTotalWeight())
    print(inv.isContains("staff"))
    print(inv.isContains("STAFF"))
    print(inv.isContains("wood shield"))
    print(inv.removeItem("water"))
    inv.addItem(InvItem("ARMOR", "wood shield", 4, 5))
    inv.printByKind()
'''
