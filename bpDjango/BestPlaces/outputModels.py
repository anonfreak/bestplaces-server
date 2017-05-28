def create_geo_dict(latitude, longitude):
    return {"latitude": latitude, "longitude": longitude}


def parsephotos(dictPic):
    photos = []
    for photo in dictPic:
        photos.append("https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=" + str(photo["photo_reference"]) + "&key=AIzaSyCk-JFceB-S7QIakQTajh1O7fMGkob7pO0")
    return photos


class MinimalPlace(object):
    photos = None
    openNow = None
    rating = None

    def __init__(self, jsonPlace):
            self.placeId = jsonPlace["place_id"]
            self.name = jsonPlace["name"]
            self.geo = create_geo_dict(jsonPlace["geometry"]["location"]["lat"], jsonPlace["geometry"]["location"]["lng"])
            if "rating" in jsonPlace:
                self.rating = jsonPlace["rating"]
            self.formatted_address = jsonPlace["formatted_address"]
            if "opening_hours" in jsonPlace:
                self.openNow = jsonPlace["opening_hours"]["open_now"]
            if "photos" in jsonPlace:
                self.photos = parsephotos(jsonPlace["photos"])
            self.categories = jsonPlace["types"]


class FullPlace(MinimalPlace):
    address = None
    phone_number = None
    website = None
    openingHours = None
    favorite = None

    def __init__(self, jsonPlace):
        super(FullPlace, self).__init__(jsonPlace)
        if "address_components" in jsonPlace:
            self.address = Address(array=jsonPlace)
        if "international_phone_number" in jsonPlace:
            self.phone_number = jsonPlace["international_phone_number"]
        if "website" in jsonPlace:
            self.website = jsonPlace["website"]
        if "opening_hours" in jsonPlace:
            self.openingHours = jsonPlace["opening_hours"]["weekday_text"]



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

    def __init__(self, json_array):
        self.placeId = json_array["place_id"]
        self.averageStar = json_array["rating"]
        self.name = json_array["name"]
        self.geo["latitude"] = json_array["location"]["lat"]
        self.geo["longitude"] = json_array["location"]["lng"]


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
            for component in array["address_components"]:
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