import os

import googlemaps

class PlacesApiHandler:
    API_KEY = os.environ["PLACES_API_KEY"]

    def __init__(self):
        self.gplaces = googlemaps.Client(self.API_KEY)
        self.search=None

    def search_place(self, query, location=None, pagetoken=None):
        self.search = self.gplaces.places(query=query, location=location, page_token=pagetoken)

        return self.search

