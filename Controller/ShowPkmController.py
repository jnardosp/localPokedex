from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
import requests

from View.PkmDisplay import Ui_PkmDisplay
from Model.pkmDB import pkmDB


import sys

class ShowPkm(QtWidgets.QMainWindow):
	def __init__(self, main):
		super(ShowPkm, self).__init__()
		self.ui = Ui_PkmDisplay()
		self.ui.setupUi(self)
		# Trae un objeto pokemon
		self.ui.img.setPixmap(QtGui.QPixmap("../View/images/unknown.png"))

		# Triggers the DisplayPkm function.
		self.ui.getPokemon.clicked.connect(self.displayPkm)
		self.ui.pushButton.clicked.connect(self.goBack)
		self.stack = main.getStack()

	def displayPkm(self):
		# Bring or download .pkl pkmn database
		allPokemon = pkmDB()
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

		self.mountType(pokemon.getTypes()[0], self.ui.Type1)
		self.mountType(pokemon.getTypes()[1], self.ui.Type2)

	def mountType(self, tipo, qTLabel):
		typeURL = "https://www.pokexperto.net/3ds/sprites/tipos/" + tipo + ".png"
		typeImg = QtGui.QImage()
		typeImg.loadFromData(requests.get(typeURL).content)
		typeImg = typeImg.scaled(50, 50, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.FastTransformation)
		qTLabel.setPixmap(QtGui.QPixmap(typeImg))

	def goBack(self):
		self.stack.setCurrentIndex(self.stack.currentIndex() -1)





