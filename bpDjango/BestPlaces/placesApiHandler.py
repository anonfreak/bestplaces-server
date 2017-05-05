import os

import googlemaps

from BestPlaces.outputModels import MinimalPlace


class PlacesApiHandler:
    API_KEY = os.environ["PLACES_API_KEY"]

    def __init__(self):
        self.gplaces = googlemaps.Client(self.API_KEY)
        self.search=None

    def search_place(self, query=None, location=None, pagetoken=None, radius=None):
        if pagetoken is None:
            self.search = self.gplaces.places(query=query, location=location, radius=radius)
        else:
            self.search = self.gplaces.places(page_token=pagetoken)
        places = []
        for place in self.search["results"]:
            places.append(MinimalPlace(place))
        return places

    def get_pagetoken(self):
        return self.search["next_page_token"]
