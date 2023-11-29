from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QTableWidgetItem

from LocalPokedex.View.Heap import Ui_Heap
from Model.pkmDB import pkmDB

class ShowHeap(QtWidgets.QMainWindow):
    def __init__(self, main):
        super(ShowHeap, self).__init__()
        self.ui = Ui_Heap()
        self.ui.setupUi(self)
        self.stack = main.getStack()
        self.pkArray = pkmDB()

        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setRowCount(len(self.pkArray))
        self.ui.tableWidget.setHorizontalHeaderLabels(["Nombre"])
        self.ui.sortMin.clicked.connect(self.displayMin)
        self.ui.pushButton.clicked.connect(self.goBack)

    def displayMin(self):
        print("organizando tabla")
        for pokemon in self.pkArray:
            # print("Añadiendo pokemon a la tabla")
            num = pokemon.getNumber()
            name = QTableWidgetItem(pokemon.getName())
            self.ui.tableWidget.setItem(num - 1, 1, name)
        print("Pokemones añadidos")
        self.ui.tableWidget.show()
    def goBack(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() - 2)