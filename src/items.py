class Item():
    def __init__(self, name, description, value, iType):
        self.name = name
        self.description = description
        self.value = value
        self.iType = iType

class Weapon(Item):
    def __init__(self, name, description, value, iType, damage):
        super().__init__(name, description, value, iType)
        self.damage = damage

# class Utils(Items):
#     def __init__(self, name, description, value, type, damage):
#         super().__init__(name, description, value, type)