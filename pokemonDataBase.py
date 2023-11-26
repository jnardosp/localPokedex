import pickle
from requests_html import HTMLSession
import time

POKEDEX_SUMMARY_SESSION = HTMLSession().get("https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/buscar")

class Pokemon:
    """
    Un pokemon tiene una propiedad número, un nombre y una propiedad URL. Mas dos funciones para inicializarlas.
    """
    def __init__(self, number):
        self.__number = None
        self.__name = None
        self.__url = None
        self.setNumber(number)
        self.setURL(number)
        self.setName()

    def setNumber(self, number):
        self.__number = number
    def getNumber(self):
        return self.__number
    
    def setName(self):
        # Buscar en la lista de toda la pokedex, el nombre de pokemon que buscamos
        self.__name = POKEDEX_SUMMARY_SESSION.html.find("tr.bazul")[self.getNumber()].find("a.nav5c", first=True).text
    def getName(self):
        return self.__name
    
    def setURL(self, number):
        self.__url = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk=" + str(number)
    def getURL(self):
        return self.__url

        return name
    def getImg(self):
        """
        Esta función consulta la dirección de la ubicación de la imagen del pokemon.
        """
        session = HTMLSession()
        pokedexPage = session.get(self.getURL())
        imgPokemon = pokedexPage.html.find(".pkmain", first=True).find(".center.bordedcho", first=True).find("img", first=True).attrs["src"]

        return imgPokemon

# Esta funcion mete en un array todos los pkmn y los serializa.
def getAllPokemon():
    try:
        # Buscamos el .pkl de pokemones
        with open("pokeDB.pkl", "rb") as pokeDB:
            allPokemon = pickle.load(pokeDB)
    except FileNotFoundError:
        # De no existir el .pkl de pokemones lo creamos
        start1 = time.time()
        allPokemon = []
        print("Creando .pkl")
        for number in range(151):
            start = time.time()
            allPokemon.append(Pokemon(number))
            end = time.time()
            print("getting a pokemon taked :",(end-start) * 10**3, "ms")

        with open("pokeDB.pkl", "wb") as pokeDB:
            pickle.dump(allPokemon, pokeDB)
        end1 = time.time()
        print("getting the pokemon taked :",(end1-start1) * 10**3, "ms")

    return allPokemon

getAllPokemon()