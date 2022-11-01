import requests


class Scraper:
    def get_response(self):
        url = "https://pokeapi.co/api/v2/pokemon"
        response = requests.get(url)

        if response.status_code == 200:
            return response
        else:
            response.raise_for_status()

    def get_data(self, response):
        data = response.json()

        pokemon_list = []

        for item in data["results"]:
            res = requests.get(item["url"])
            pokemon_data = res.json()

            ability = pokemon_data["abilities"][0]["ability"]["name"]
            moves = pokemon_data["moves"][0]["move"]["name"]
            experience = pokemon_data["base_experience"]
            height = pokemon_data["height"]
            weight = pokemon_data["weight"]

            details = {
                "name": item["name"],
                "ability": ability,
                "moves": moves,
                "experience": experience,
                "height": height,
                "weight": weight,
            }

            pokemon_list.append(details)
        return pokemon_list
