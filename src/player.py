class Player:
    def __init__(self):
        self.inventory = []

    def AddItem(self, item:str):
        self.inventory.append(item)

    def HasItem(self, item:str):
        return item in self.inventory

    def GameOver(self):
        self.inventory = []