
# ! Don't remove items from a list while enumerating over it.
# ! This will cause some items to be skipped. Instead, rebuild the list minus item.
# ? https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
# ? https://stackoverflow.com/questions/38546951/remove-element-from-list-when-using-enumerate-in-python
# * The remove() method will remove the first instance of a value in a list.
# ? any() method https://stackoverflow.com/questions/9371114/check-if-list-of-objects-contain-an-object-with-a-certain-attribute-value

class Player():
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory
        self.last_item = ""
    
    def getItem(self, itemName):
        if itemName == "it":
            itemName = self.last_item
        
        if any(item.name.lower() == itemName for item in self.location.inventory):
            # Gets specified item and appends it to room inv
            toGet = [item for item in self.location.inventory if  item.name.lower() == itemName]
            self.inventory.append(toGet[0])
            
            # Remakes inv list without specified item
            self.location.inventory = [item for item in self.location.inventory if not item.name.lower() == itemName]
            self.last_item = itemName
            toGet[0].onTake()
            
        else:
            print(f"\nThere is no '{itemName}' in the room")
        
    def dropItem(self, itemName):
        if itemName == "it":
            itemName = self.last_item
            
        if any(item.name.lower() == itemName for item in self.inventory):
            # Gets specified item and appends it to room inv
            toDrop = [item for item in self.inventory if  item.name.lower() == itemName]
            self.location.inventory.append(toDrop[0])
            
            # Remakes inv list without specified item
            self.inventory = [item for item in self.inventory if not item.name.lower() == itemName]
            toDrop[0].onDrop()
            
        else:
            print(f"\nYou dont have '{itemName}' in inventory")
    
    def __str__(self):
        return f"\nName: {self.name}\nLocation: {self.location}"