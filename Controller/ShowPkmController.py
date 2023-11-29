from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
import requests

from LocalPokedex.View.PkmDisplay import Ui_PkmDisplay
from LocalPokedex.Model.pkmDB import pkmDB

import sys

class ShowPkm(QtWidgets.QMainWindow):
	def __init__(self, stack):
		super(ShowPkm, self).__init__()
		self.ui = Ui_PkmDisplay()
		self.ui.setupUi(self)
		# Trae un objeto pokemon
		self.ui.img.setPixmap(QtGui.QPixmap("../View/images/unknown.png"))

		# Triggers the DisplayPkm function.
		self.ui.getPokemon.clicked.connect(self.displayPkm)
		self.ui.pushButton.clicked.connect(self.goBack)
		self.stack = stack

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

		type1URL = "https://www.pokexperto.net/3ds/sprites/tipos/" + pokemon.getTypes()[0] + ".png"
		type1Img = QImage()
		type1Img.loadFromData(requests.get(type1URL).content)
		type1Img = type1Img.scaled(50, 50, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.FastTransformation)
		self.ui.Type1.setPixmap(QtGui.QPixmap(type1Img))

	def goBack(self, stack):
		self.stack.setCurrentIndex(self.stack.currentIndex() -1)




