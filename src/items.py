class Item():
    def __init__(self, name, description, value, iType):
        self.name = name
        self.description = description
        self.value = value
        self.iType = iType
    
    def onTake(self):
        print(f"\nAdded '{self.name}' to inventory.")
    
    def onDrop(self):
        print(f"\nDropped '{self.name}' from inventory.")
    
    def __str__(self):
        return f"\n{self.name}\n{self.description}\n{self.value}"

class Weapon(Item):
    def __init__(self, name, description, value, iType, damage):
        super().__init__(name, description, value, iType)
        self.damage = damage
    
    def __str__(self):
        return f"\n{self.name}\n{self.description}\n{self.value}\n{self.damage}"