from requests_html import HTMLSession

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
        imgPokemon = POKEDEX_SUMMARY_SESSION.html.find("tr.bazul")[self.getNumber()].find("td.bordetodos")[1].find("img", first=True).attrs["src"]
        print(imgPokemon)

        return imgPokemon