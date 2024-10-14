from PySide6.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from levelWidget import LevelWidget
from level import Level, Option
from player import Player

class VisualNoveApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visual Novel")
        self.masterLayout = QVBoxLayout()
        self.setLayout(self.masterLayout)

        self.levelWidget = LevelWidget()
        self.masterLayout.addWidget(self.levelWidget)

    def StartGame(self, level: Level):
        player = Player()
        self.levelWidget.SetPlayer(player)
        self.levelWidget.ConfigureWithLevel(level)


if __name__ == "__main__":
    levelDungen = Level("Dungen", "you Art at the dungen entrance, there are 2 doors you can try:", "dungen.png")  
    levelLeftDoor = Level("Left Cell", "there are 2 boxes in the cell, a blue one and a red one, which one would you open?", "leftCell.png")
    levelRightDoor = Level("Right Cell", "there there is a door inside, seems to need a key to open", "rightCell.png")
    blueBoxOpenedLevel = Level("Blue Box", "You opened the bluebox, a giant python came and ate you alive, you die!", "blueBoxOpened.png")
    redBoxOpendLevel = Level("Red Box", "Your Opend the Red Box, a key apears, you took the key", "redBoxOpened.png")
    tiggerLevel = Level("Tiger level", "You entered a hallway, and found a tiger guarding the pass, the tiger asked: What has a neck but no head?", "Tiger.png")
    killedByTiggerLevel = Level("Killed", "The tiger says: You shall not pass! and killed you!", "TigerKill.png")
    winLevel = Level("Found Treasure!", "The tigger says: Greate answer! you shall pass! you get inside and found a montain of Treasure!", "Treasure.png")

    dungenOptLeftDoor = Option("Go to the Left Door", levelLeftDoor)
    dungenOptRightDoor = Option("Go to the Right Door", levelRightDoor)
    levelDungen.AddOption(dungenOptLeftDoor)
    levelDungen.AddOption(dungenOptRightDoor)

    leftCellBlueOption = Option("Open the blue one", blueBoxOpenedLevel)
    leftCellRedOption = Option("Open the red one", redBoxOpendLevel)
    levelLeftDoor.AddOption(leftCellBlueOption)
    levelLeftDoor.AddOption(leftCellRedOption)

    playAgainOption = Option("Player Again", levelDungen)
    playAgainOption.applyOptionLambda = lambda player : player.GameOver()
    blueBoxOpenedLevel.AddOption(playAgainOption)

    restartOption = Option("Back to the Entrance", levelDungen)
    restartOption.applyOptionLambda = lambda player : player.AddItem("Key")
    redBoxOpendLevel.AddOption(restartOption)

    backToEntranceOption = Option("Back to Entrance", levelDungen)
    openRightDoorOption = Option("Open with Key", tiggerLevel)
    openRightDoorOption.shouldDisplayLambda = lambda player : player.HasItem("Key")
    levelRightDoor.AddOption(backToEntranceOption)
    levelRightDoor.AddOption(openRightDoorOption)

    tigerAnswerOptionOne = Option("Me being killed?", killedByTiggerLevel)
    tigerAnswerOptionThree = Option("A bottle I guess...", winLevel)
    tigerAnswerOptionTwo = Option("You Killed by Me!", killedByTiggerLevel)
    tiggerLevel.AddOption(tigerAnswerOptionOne)
    tiggerLevel.AddOption(tigerAnswerOptionTwo)
    tiggerLevel.AddOption(tigerAnswerOptionThree)

    killedByTiggerLevel.AddOption(playAgainOption)
    winLevel.AddOption(playAgainOption)

    app = QApplication()
    novelApp = VisualNoveApp()
    novelApp.StartGame(levelDungen)
    novelApp.show()

    app.exec()