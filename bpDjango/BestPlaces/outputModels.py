import re


def create_geo_dict(latitude, longitude):
    return {"latitude": latitude, "longitude": longitude}


class MinimalPlace(object):
    photos = None
    openNow = None
    rating = None

    def __init__(self, dict):
            self.placeId = dict["place_id"]
            self.name = dict["name"]
            self.geo = create_geo_dict(dict["geometry"]["location"]["lat"], dict["geometry"]["location"]["lng"])
            if "rating" in dict:
                self.rating = dict["rating"]
            self.formatted_address = dict["formatted_address"]
            if "opening_hours" in dict:
                self.openNow = dict["opening_hours"]["open_now"]
            if "photos" in dict:
                self.photos = self.__parsephotos(dict["photos"])
            self.categories = dict["types"]

    def __parsephotos(self, dictPic):
        photos = []
        for photo in dictPic:
            photos.append("https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=" + str(photo["photo_reference"]) + "&key=AIzaSyCk-JFceB-S7QIakQTajh1O7fMGkob7pO0")
        return photos

class FullPlace(MinimalPlace):
    address = None
    phone_number = None
    website = None
    openingHours = None
    favorite = None

    def __init__(self, dict):
        super(FullPlace, self).__init__(dict)
        if "address" in dict:
            self.address = Address(array=dict)


class UserPlace:
    placeId = ""
    name = ""
    geo = {"latitude": 0, "longitude": 0}
    phone_number = 0
    website = ""
    openingHours = []
    pictures = []
    averageStar = 0
    favorite = True
    review_list = []

    def __init__(self, dict):
        self.placeId = dict["place_id"]
        self.averageStar = dict["rating"]
        self.name = dict["name"]
        self.geo["latitude"] = dict["location"]["lat"]
        self.geo["longitude"] = dict["location"]["lng"]


class openingHour:
    day = 0
    opens = 0000
    closes = 0000


class Address:
    street =""
    streetNumber = ""
    town = ""
    zipCode = 0

    def __init__(self, street=None, house_number=None, town=None, zip_code=None, array=None):
        if array is None:
            self.street = street
            self.streetNumber = int(house_number)
            self.town = town
            self.zipCode = int(zip_code)
        else:
            for component in array:
                if "route" in component["types"]:
                    self.street = component["long_name"]
                if "locality" in component["types"]:
                    self.town = component["long_name"]
                if "street_number" in component["types"]:
                    self.streetNumber = int(component["long_name"])
                if "postal_code" in component["types"]:
                    self.zipCode = int(component["long_name"])

class Review:
    starts = 0
    showName = True
    text = ""