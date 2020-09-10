# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    # def move(self, direction):
    #     if direction not in self.location.exists():
    #         print("Can't move in that direction")
    #         return
    #     new_location = self.location.
    
    def __str__(self):
        return f"Name: {self.name}\nLocation: {self.location}\n"