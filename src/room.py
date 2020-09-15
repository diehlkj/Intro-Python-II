# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, title, description, inventory=[]):
        self.name = name
        self.title = title
        self.description = description
        self.inventory = inventory
    
    # def n_to(self):
        
    # def s_to(self):
        
    # def e_to(self):
        
    # def w_to(self):
        
    def __str__(self):
        return f"{self.name}\n{self.description}\n{self.inventory}\n"