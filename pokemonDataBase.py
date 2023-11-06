import pickle
from requests_html import HTMLSession

POKEDEX_URL= "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="

class Pokemon:
    def __init__(self, name, type, img, url):
        self.name = name
        self.type = type
        self.img = img
        self.url = url

# Accedemos y guardamos los datos de un pokemon determinado por el número en pokedex.
def getPokemon(number):
        url = "{}{}" .format(POKEDEX_URL, number)
        session = HTMLSession()
        pokedexPage = session.get(url)
        newPokemon = Pokemon(pokedexPage.html.find("span", first=True).find(".mini", first=True).text, [],
                             pokedexPage.html.find(".pkmain", first=True).find(".center.bordedcho", first=True).find("img", first=True).attrs["src"], url)

        # En nuestra wiki los tipos de pokemon son imágenes jajaja
        for img in pokedexPage.html.find(".pkmain", first=True).find(".bordeambos", first=True).find("img"):
            newPokemon.type.append(img.attrs["alt"])
        
        return newPokemon

def getAllPokemon():
    try:
        # Buscamos el .pkl de pokemones
        with open("pokeDB.pkl", "rb") as pokeDB:
            allPokemon = pickle.load(pokeDB)
    except FileNotFoundError:
        # De no existir el .pkl de pokemones lo creamos
        allPokemon = []
        print("Creando .pkl")
        for number in range(151):
            allPokemon.append(getPokemon(number + 1))

        with open("pokeDB.pkl", "wb") as pokeDB:
            pickle.dump(allPokemon, pokeDB)

    return allPokemon

def main():
    getAllPokemon()
    print("x")

if __name__ == "__main__":
    main()