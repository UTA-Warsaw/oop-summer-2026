import requests

class PokemonClient:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon"

    def get_pokemon(self, name):
        response = requests.get(f"{self.BASE_URL}/{name}")
        return response.json()

class Pokemon:
    def __init__(self, data):
        self.name = data["name"]

    def display(self):
        print(self.name)

client = PokemonClient()

data = client.get_pokemon("pikachu")

pokemon = Pokemon(data)

pokemon.display()
