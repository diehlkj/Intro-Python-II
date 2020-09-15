# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory
    
    # def move(self, direction):
    #     if direction not in self.location.exists():
    #         print("Can't move in that direction")
    #         return
    #     new_location = self.location.
    
    def getItem(self, item):
        self.inventory.append(item)
        
    def dropItem(self, item):
        # ! Don't remove items from a list while enumerating over it.
        # ! This will cause some items to be skipped. Instead, rebuild the list minus item.
        # ? https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
        # ? https://stackoverflow.com/questions/38546951/remove-element-from-list-when-using-enumerate-in-python
        # * The remove() method will remove the first instance of a value in a list.
        # ? any() method https://stackoverflow.com/questions/9371114/check-if-list-of-objects-contain-an-object-with-a-certain-attribute-value
        
        if any(x.name.lower() == item for x in self.inventory):
            # Gets specified item and appends it to room inv
            toDrop = [thing for thing in self.inventory if  thing.name.lower() == item]
            # Remakes inv list without specified item
            self.inventory = [thing for thing in self.inventory if not thing.name.lower() == item]
            print(f"Dropped '{item}' from inventory.")
            
            return toDrop
        else:
            print(f"You dont have '{item}' in inventory")
    
    def __str__(self):
        return f"Name: {self.name}\nLocation: {self.location}\n"