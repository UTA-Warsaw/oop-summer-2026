import time
import sys

# 1. Kontrol: Requests yüklü mü?
try:
    import requests
except ImportError:
    print("\n[ERROR] 'requests' library is missing!")
    print("Please go to PyCharm Terminal and type: pip install requests")
    print("\nPress Ctrl+C to exit or close the window.")
    while True: time.sleep(1)


# 2. CLASS: API Client
class PokemonClient:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon/"

    def fetch_pokemon_data(self, pokemon_name):
        try:
            response = requests.get(self.base_url + pokemon_name.lower())
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None


# 3. CLASS: Pokemon Object
class Pokemon:
    def __init__(self, data):
        self.name = data["name"].capitalize()
        self.id = data["id"]
        self.height = data["height"]
        self.weight = data["weight"]
        self.type = data["types"][0]["type"]["name"].upper()

    def display_info(self):
        print("\n" + "=" * 30)
        print("      POKEMON DATA SHEET")
        print("=" * 30)
        print(f"Name   : {self.name}")
        print(f"ID     : {self.id}")
        print(f"Type   : {self.type}")
        print(f"Height : {self.height}")
        print(f"Weight : {self.weight}")
        print("=" * 30)


# --- ÇALIŞTIRMA ---
if __name__ == "__main__":
    client = PokemonClient()

    # Buraya istediğin Pokemon ismini yazabilirsin
    target = "charizard"
    print(f"Searching for {target}...")

    data = client.fetch_pokemon_data(target)

    if data:
        my_pokemon = Pokemon(data)
        my_pokemon.display_info()
    else:
        print("\n[ERROR] Pokemon not found!")

    # PENCEREYİ AÇIK TUTAN KISIM
    print("\nPROCESS FINISHED.")
    print("Close the window (X) to exit.")

    while True:
        time.sleep(1)