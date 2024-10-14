from dir import ASSET_DIR
import os
from player import Player

class Option:
    def __init__(self, optionDescription, nextLevel):
        self.description = optionDescription
        self.nextLevel = nextLevel
        self.shouldDisplayLambda = lambda player : True
        self.applyOptionLambda = lambda player : None

class Level:
    def __init__(self, levelName: str, levelDescription: str, levelImageFileName: str):
        self.name = levelName
        self.description = levelDescription
        self.imagePath = os.path.join(ASSET_DIR, levelImageFileName)
        self.options = []

    def AddOption(self, newOption):
        self.options.append(newOption)

    def GetOptions(self, player: Player):
        outOptions = []
        for option in self.options:
            if option.shouldDisplayLambda(player):
                outOptions.append(option)

        return outOptions