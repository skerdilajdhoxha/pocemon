from django.shortcuts import render

from .crawler import Scraper
from .models import Pokemon


def pokemon_list(request):
    """
    If there's pokemon in database get and display them,
    else get them from pokeapi.co API and register them in database
    """
    pok_list = Pokemon.objects.all()
    if pok_list:
        return render(request, "pokemon_list.html", {"pokemon_list": pok_list})
    else:
        scraper = Scraper()
        response = scraper.get_response()
        pokemon_list = scraper.get_data(response)

        pokemon_to_create = [
            Pokemon(
                name=obj["name"],
                ability=obj["ability"],
                moves=obj["moves"],
                experience=obj["experience"],
                height=obj["height"],
                weight=obj["weight"],
            )
            for obj in pokemon_list
        ]
        created_pokemon = Pokemon.objects.bulk_create(
            pokemon_to_create, ignore_conflicts=True
        )
        return render(request, "pokemon_list.html", {"pokemon_list": created_pokemon})
