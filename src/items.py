class Item():
    def __init__(self, name, description, value, iType):
        self.name = name
        self.description = description
        self.value = value
        self.iType = iType
        
    def __str__(self):
        return f"{self.name}\n{self.description}\n{self.value}\n"

class Weapon(Item):
    def __init__(self, name, description, value, iType, damage):
        super().__init__(name, description, value, iType)
        self.damage = damage

# class Utils(Items):
#     def __init__(self, name, description, value, type, damage):
#         super().__init__(name, description, value, type)