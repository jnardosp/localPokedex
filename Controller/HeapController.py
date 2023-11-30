from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QTableWidgetItem

from View.Heap import Ui_Heap
from Model.pkmDB import pkmDB
from Model.PokeHeap import PokeHeap

class ShowHeap(QtWidgets.QMainWindow):
    def __init__(self, main):
        super(ShowHeap, self).__init__()
        self.ui = Ui_Heap()
        self.ui.setupUi(self)
        self.stack = main.getStack()
        self.pkArray = pkmDB()
        self.myPkmHeap = PokeHeap().getMaxArray()

        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(len(self.pkArray))
        self.ui.tableWidget.setHorizontalHeaderLabels(["Numero", "Nombre"])
        self.ui.sortMax.clicked.connect(self.displayMax)
        self.ui.sortMin.clicked.connect(self.displayMin)
        self.ui.pushButton.clicked.connect(self.goBack)
        self.ui.sortAZ.hide()
        self.ui.sortZA.hide()

    def displayMin(self):
        print("organizando tabla")
        for pokemon in self.pkArray:
            # print("Añadiendo pokemon a la tabla")
            num = pokemon.getNumber()
            name = QTableWidgetItem(pokemon.getName())
            self.ui.tableWidget.setItem(num, 0, QTableWidgetItem(str(pokemon.getNumber() + 1)))
            self.ui.tableWidget.setItem(num, 1, name)
        print("Pokemones añadidos")
        self.ui.tableWidget.show()

    def displayMax(self):
        print("organizando tabla")
        for pokemon in self.myPkmHeap:
            inx = self.myPkmHeap.index(pokemon)
            self.ui.tableWidget.insertRow(inx)
            self.ui.tableWidget.setItem(inx, 0, QTableWidgetItem(str(pokemon.getNumber()+1)))
            self.ui.tableWidget.setItem(inx, 1, QTableWidgetItem(pokemon.getName()))
        print("Pokemones añadidos")
        self.ui.tableWidget.show()

    def goBack(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() - 2)