from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from PyQt5.QtGui import QImage

from View.PkmDisplay import Ui_PkmDisplay
import pokemonDataBase
import sys


class ShowPkm(QtWidgets.QMainWindow):
	def __init__(self):
		super(ShowPkm, self).__init__()
		self.ui = Ui_PkmDisplay()
		self.ui.setupUi(self)
		# Trae un objeto pokemon
		self.ui.img.setPixmap(QtGui.QPixmap("View/images/unknown.png"))


		# Triggers the DisplayPkm function.
		self.ui.getPokemon.clicked.connect(self.displayPkm)

	def displayPkm(self):
		# Bring or download .pkl pkmn database
		allPokemon = pokemonDataBase.getAllPokemon()
		# Calls the getName function of the pokemon object using as value the text from lineEdit.
		pokemon = allPokemon[int(self.ui.lineEdit.text())-1]

		# Brings the Pokemon name and adds it to the respective label. 
		self.ui.nombre.setText(pokemon.getName())
		print(pokemon.getName())

		# Creates the URL of the pokemon image.
		pkmImgURL = "https://www.pokexperto.net/" + pokemon.getImg()
		# Creates a QImage and loads it from another request to the HTML page.
		pkmImg = QImage()
		pkmImg.loadFromData(requests.get(pkmImgURL).content)
		pkmImg = pkmImg.scaled(200, 200, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.FastTransformation)
		print(pkmImgURL)

		# sets the respective label on the GUI.
		self.ui.img.setPixmap(QtGui.QPixmap(pkmImg))



app = QtWidgets.QApplication([])
stack = QtWidgets.QStackedWidget()

showPkm = ShowPkm()

stack.addWidget(showPkm)

stack.setFixedWidth(1000)
stack.setFixedHeight(1000)
stack.show()
sys.exit(app.exec())