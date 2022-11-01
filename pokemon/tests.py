import requests
from django.test import TestCase


class TaskTest(TestCase):
    def test_get_api_response(self):
        test_response = requests.get(f"https://pokeapi.co/api/v2/pokemon")
        self.assertEqual(test_response.status_code, 200)
        data = test_response.json()
        self.assertTrue(len(data["results"]) >= 1)

    def test_pokemon_list_view(self):
        test_response = self.client.get("/")
        self.assertEqual(test_response.status_code, 200)
        self.assertTemplateUsed(test_response, "pokemon_list.html")
