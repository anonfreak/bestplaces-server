import re


def create_geo_dict(latitude, longitude):
    return {"latitude":latitude, "longitude":longitude}


class MinimalPlace:
    def __init__(self, dict):
            self.placeId = dict["place_id"]
            self.name = dict["name"]
            self.geo = create_geo_dict(dict["geometry"]["location"]["lat"], dict["geometry"]["location"]["lng"])
            self.rating = dict["rating"]
            self.formatted_address = dict["formatted_address"]
            self.openNow = dict["opening_hours"]["open_now"]
            if "photos" in dict:
                self.photos = self.__parsephotos(dict["photos"])
            self.categories = dict["types"]

    def __parsephotos(self, dictPic):
        photos = []
        for photo in dictPic:
            photos.append("https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=" + str(photo["photo_reference"]) + "&key=AIzaSyCk-JFceB-S7QIakQTajh1O7fMGkob7pO0")
        return photos


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
    house_number = ""
    town = ""
    zip_code = 0

    def __init__(self, street, house_number, town, zip_code):
        self.street = street
        self.house_number = house_number
        self.town = town
        self.zip_code = zip_code


class Review:
    starts = 0
    showName = True
    text = ""