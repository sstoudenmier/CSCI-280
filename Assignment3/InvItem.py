'''
Seth Stoudenmier
2/24/16

Honor pledge: All work was done by myself.

Purpose: Purpose of this file is to create an Inventory Item object with many
different attributes and its corresponding functions.
'''

class InvItem:
    def __init__(self, kind="UNDEF", name="NONE", weight=0, value=0):
        self.kind = kind
        self.name = name
        self.weight = weight
        self.value = value
        self.kindTypes = ["WEAPON", "HEALTH", "CRAFTS", "ARMOR"]

    '''
    Set the kind of the inventory item.
    @param: k - the kind of the item
    '''
    def setKind(self, k):
        for i in self.kindTypes:
            if (i == k):
                self.kind = k
                break
            else:
                self.kind = "UNDEF"

    '''
    Set the weight of the inventory item.
    @param: w - the weight of the item
    '''
    def setWeight(self, w):
        if (w > 0):
            self.weight = w
        else:
            print("Weight must be greater than 0!")

    '''
    Set the name of the inventory item.
    @param: n - the name of the item
    '''
    def setName(self, n):
        self.name = n

    '''
    Set the value of the inventory item.
    @param: v - the value of the item
    '''
    def setValue(self, v):
        self.value = v

    '''
    Get the kind of the inventory item.
    @return: the kind of the inventory item
    '''
    def getKind(self):
        return self.kind

    '''
    Get the weight of the inventory item.
    @return: the weight of the inventory item
    '''
    def getWeight(self):
        return self.weight

    '''
    Get the name of the inventory item.
    @return: the name of the inventory item
    '''
    def getName(self):
        return self.name

    '''
    Get the value of the inventory item.
    @return: the value of the inventory item
    '''
    def getValue(self):
        return self.Value

    '''
    The toString method for the Inventory Item class.
    @return: the string representation of the Inventory Item class
    '''
    def __str__(self):
        return "name: " + self.name + "\nkind: " + self.kind + "\nweight: " +  \
        str(self.weight) + "\nvalue: " + str(self.value)
