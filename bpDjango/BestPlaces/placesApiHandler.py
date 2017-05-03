# coding=utf-8
import os

import googlemaps
from googleplaces import GooglePlaces, types, GooglePlacesSearchResult
import json


class PlacesApiHandler:
    API_KEY = os.environ["PLACES_API_KEY"]

    def __init__(self):
        self.gmaps = GooglePlaces(self.API_KEY)

    def get_place_information(self, query):
        result = self.gmaps.text_search(query=query)
        return result.places

    def search_place(self):
        return None