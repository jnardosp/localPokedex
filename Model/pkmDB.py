import pickle
import time
from Model.Pokemon import Pokemon

# Esta funcion mete en un array todos los pkmn y los serializa.
def pkmDB():
    try:
        # Buscamos el .pkl de pokemones
        with open("Model/pokeDB.pkl", "rb") as pokeDB:
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

        end1 = time.time()
        with open("Model/pokeDB.pkl", "wb") as pokeDB:
            pickle.dump(allPokemon, pokeDB)
        print("getting the pokemon taked :",(end1-start1) * 10**3, "ms")

    return allPokemon