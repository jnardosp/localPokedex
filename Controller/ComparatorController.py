from PyQt5 import QtWidgets, QtGui

from LocalPokedex.View.Comparator import Ui_Comparator
from LocalPokedex.Model.pkmDB import pkmDB
from LocalPokedex.Model.PkmStrenghts import Tipo

traducciones = {
            "normal": "Normal",
            "fuego": "Fire",
            "lucha": "Fighting",
            "agua": "Water",
            "volador": "Flying",
            "planta": "Grass",
            "electrico": "Electric",
            "veneno": "Poison",
            "tierra": "Ground",
            "psiquico": "Psychic",
            "roca": "Rock",
            "hielo": "Ice",
            "bicho": "Bug",
            "dragon": "Dragon",
            "fantasma": "Ghost",
            "siniestro": "Dark",
            "acero": "Steel",
            "hada": "Fairy"

        }
class ShowComparator(QtWidgets.QMainWindow):
    """
    ShowComparator es el controlador del comparador de pokemones. Buscamos traer dos pokemones particulares de la base
    de datos y compararlos en función de sus tipos, invocando el grafo de tipos construido en PKMStrenghts.
    """
    def __init__(self, ):
        super(ShowComparator, self).__init__()
        self.ui = Ui_Comparator()
        self.ui.setupUi(self)

        self.ui.getPkms.clicked.connect(self.displayPkms)
        # This overwrites the function above, thus the program is not bringing a pokemon.
        self.ui.getPkms.clicked.connect(self.showComparator)
        self.allPkm = pkmDB()
        self.myPkm = None
        self.rivalPkm = None

    def displayPkms(self):

        # Initialize my pokemon and display it on screen:
        self.myPkm = self.allPkm[int(self.ui.getMyPkm.text()) -1]
        self.ui.myPkmName.setText(self.myPkm.getName())
        miTipo1 = self.myPkm.getTypes()[0]
        miTipo2 = ''
        if self.myPkm.getTypes()[1] == 'n':
            miTipo2 = ''
        else:
            miTipo2 = self.myPkm.getTypes()[1]
        self.ui.myType1.setText(miTipo1)
        self.ui.myType2.setText(miTipo2)

        # Initialize the rival's pokemon and dislay it on screen:
        self.rivalPkm = self.allPkm[int(self.ui.getRivalPkm.text()) -1]
        self.ui.rivalPkmName.setText(self.rivalPkm.getName())
        rivalTipo1 = self.rivalPkm.getTypes()[0]
        rivalTipo2 = ''
        if self.rivalPkm.getTypes()[1] == 'n':
            rivalTipo2 = ''
        else:
            rivalTipo2 = self.rivalPkm.getTypes()[1]

        self.ui.rivalType1.setText(rivalTipo1)
        self.ui.rivalType2.setText(rivalTipo2)

    def showComparator(self):
        tipo1 = traducciones[self.myPkm.getTypes()[0]]
        myPkmType = Tipo(tipo1)
        print(myPkmType.getFuerteContra())

        tipo2 = traducciones[self.rivalPkm.getTypes()[0]]
        rivalPkmType = Tipo(tipo2)
        print(rivalPkmType.getFuerteContra())

        if myPkmType.getPropio() in rivalPkmType.getFuerteContra():
            print("El pokemon oponente es mas fuerte que el tuyo.")
            self.ui.conclusion.setText("El pokemon oponente es mas fuerte que el tuyo.")
        elif rivalPkmType.getPropio() in myPkmType.getFuerteContra():
            print("Tu pokemon es mas fuerte que el oponente.")
            self.ui.conclusion.setText("Tu pokemon es mas fuerte que el oponente.")
        else:
            print("Es una pelea balanceada.")
            self.ui.conclusion.setText("Es una pelea balanceada.")







