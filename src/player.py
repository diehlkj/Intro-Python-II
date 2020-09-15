# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory
    
    def getItem(self, itemName):
        if any(item.name.lower() == itemName for item in self.location.inventory):
            # Gets specified item and appends it to room inv
            toGet = [item for item in self.location.inventory if  item.name.lower() == itemName]
            self.inventory.append(toGet[0])
            
            # Remakes inv list without specified item
            self.location.inventory = [item for item in self.location.inventory if not item.name.lower() == itemName]
            print(f"Added '{toGet[0].name}' to inventory.")
            
        else:
            print(f"There is no '{itemName}' in the room")
        
    def dropItem(self, itemName):
        # ! Don't remove items from a list while enumerating over it.
        # ! This will cause some items to be skipped. Instead, rebuild the list minus item.
        # ? https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
        # ? https://stackoverflow.com/questions/38546951/remove-element-from-list-when-using-enumerate-in-python
        # * The remove() method will remove the first instance of a value in a list.
        # ? any() method https://stackoverflow.com/questions/9371114/check-if-list-of-objects-contain-an-object-with-a-certain-attribute-value
        
        if any(item.name.lower() == itemName for item in self.inventory):
            # Gets specified item and appends it to room inv
            toDrop = [item for item in self.inventory if  item.name.lower() == itemName]
            self.location.inventory.append(toDrop[0])
            
            # Remakes inv list without specified item
            self.inventory = [item for item in self.inventory if not item.name.lower() == itemName]
            print(f"Dropped '{toDrop[0].name}' from inventory.")
            
        else:
            print(f"You dont have '{itemName}' in inventory")
    
    def __str__(self):
        return f"Name: {self.name}\nLocation: {self.location}\n"