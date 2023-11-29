from requests_html import HTMLSession


class Tipo:
    def __init__(self, propio):
        self._PKM_TYPE_CHART_URL = "https://bulbapedia.bulbagarden.net/wiki/Type#Type_chart"
        self._propio = None
        self._fuerteContra = []
        self.setPropio(propio)

    def setPropio(self, nombre):
        # print("creando Tipo")
        # De manera provisional, estoy obteniendo la información de un tipo de pokemon particular.
        consulta = HTMLSession()
        tablaDeTipos = consulta.get(self._PKM_TYPE_CHART_URL)
        tipo = tablaDeTipos.html.find("table")[1].find("a", containing=nombre)[1].text
        self._propio = tipo
        consulta.close()
        """
         A futuro, esta función la debe implementar el controlador de vista del comparador de la siguiente manera:
          - Despues de que el usuario ingresa los pokemones que desea buscar, el sistema crea un objeto Tipo y setea su
          valor propio al valor de pkm.getTipo.
         """
    def getPropio(self):
        return self._propio # Devuelve el valor del tipo de pokemon que se está consultando.
    def setFuerteContra(self):
        adyacencias = []
        print("consultando lista de adyacencia...")
        consulta = HTMLSession()
        tablaDeTipos = consulta.get(self._PKM_TYPE_CHART_URL)
        fila = tablaDeTipos.html.find("table")[1].find("tr", containing=self.getPropio(), first=True).find("td")

        for element in fila:
            if element.text == '2×':
                adyacencias.append(fila.index(element))
        self._fuerteContra = adyacencias
        print("lista de adyacencia generada.")
        consulta.close()
        """
        Esta función consulta en la página https://bulbapedia.bulbagarden.net/wiki/Type#Type_chart por un tipo y extrae
        todos los tipos contra los que este es fuerte, es decir que el ataque resulta con un valor x2 y devuelve una 
        lista con los indices de estas casillas. 
        """

    def getFuerteContra(self):
        print("consultando tipos.")
        consulta = HTMLSession()
        tablaDeTipos = consulta.get(self._PKM_TYPE_CHART_URL)
        tipos = tablaDeTipos.html.find("table")[1].find("th")

        # Limpiando dos datos que trae la tabla que no necesito.
        tipos.pop(0)
        tipos.pop(0)

        fuerteContra = []

        for index in self._fuerteContra:
            fuerteContra.append(tipos[index].text)
        print("lista de tipos creada.")
        return fuerteContra
    """
    def printfuerteContra(self):
        cad = ""
        for tipo in self._fuerteContra:
            cad = cad + " " + tipo

        print(str)
    """

tipo = Tipo("Psychic")
tipo.setFuerteContra()
print("Los pokemones de tipo " + tipo.getPropio() + " son fuertes contra los pokemones del tipo " + str(tipo.getFuerteContra()))
# tipo.printfuerteContra()





