from PyQt5 import QtWidgets
from View.MainMenuView import Ui_MainWindow


class ShowMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(ShowMain, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.findByNumber.clicked.connect(self.goToShowPkm)
        # self.ui.listPokemon.clicked.connect(self.goToListPkm)
        self.ui.comparePokemon.clicked.connect(self.goToCompare)
        self.stack = QtWidgets.QStackedWidget()
        self.stack.setFixedWidth(800)
        self.stack.setFixedHeight(600)

    def getStack(self):
        return self.stack

    def setStackIdex(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() -1)

    def goToShowPkm(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() + 1)

    def goToListPkm(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() + 2)

    def goToCompare(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() + 2)




