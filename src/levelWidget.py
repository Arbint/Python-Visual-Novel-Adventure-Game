from PySide6.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal
import os
from level import Level, Option
from player import Player
from dir import ASSET_DIR

class LevelOptionWidget(QWidget):
    def __init__(self, option: Option):
        super().__init__()
        self.masterLayout = QVBoxLayout()
        self.setLayout(self.masterLayout)
        self.option =option
        self.masterLayout.addWidget(QLabel(option.description))
    

class LevelWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.masterLayout = QVBoxLayout()
        self.setLayout(self.masterLayout)

        self.levelName = QLabel("TestLevel")
        self.masterLayout.addWidget(self.levelName)        
        
        self.levelImage = QLabel()
        levelPixelMap = QPixmap(os.path.join(ASSET_DIR, "dungen.png"))
        self.levelImage.setPixmap(levelPixelMap)
        self.levelImage.setFixedSize(levelPixelMap.size())
        self.masterLayout.addWidget(self.levelImage)

        self.levelDescriptionLabel = QLabel("Level Description")
        self.masterLayout.addWidget(self.levelDescriptionLabel)

        self.optionListWidget = QListWidget()
        testOptionOneItem = QListWidgetItem(self.optionListWidget)
        testOptionWidget = LevelOptionWidget(Option("left", None))
        testOptionOneItem.setSizeHint(testOptionWidget.sizeHint())
        self.optionListWidget.setItemWidget(testOptionOneItem, testOptionWidget)
        self.masterLayout.addWidget(self.optionListWidget)
        self.optionListWidget.itemClicked.connect(self.OptionSelected)

    def SetPlayer(self, player: Player):
        self.player = player

    def ConfigureWithLevel(self, level: Level):
        self.levelName.setText(level.name)

        levelPixelMap = QPixmap(level.imagePath)
        self.levelImage.setPixmap(levelPixelMap)
        self.levelImage.setFixedSize(levelPixelMap.size())

        self.levelDescriptionLabel.setText(level.description)

        self.optionListWidget.clear()
        for option in level.GetOptions(self.player):
            optionItem = QListWidgetItem(self.optionListWidget)
            optionWidget = LevelOptionWidget(option)
            optionItem.setSizeHint(optionWidget.sizeHint())
            self.optionListWidget.setItemWidget(optionItem, optionWidget)

    def OptionSelected(self, optionItem: QListWidgetItem):
        optionWidget = self.optionListWidget.itemWidget(optionItem)
        option: Option = optionWidget.option
        option.applyOptionLambda(self.player)
        if option.nextLevel is not None:
            self.ConfigureWithLevel(option.nextLevel)
        
        
