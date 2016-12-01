class UserPlace:
    placeid = ""
    name = ""
    geo = {"latitude": 0, "longitude": 0}
    address = Address()
    phone_number = 0
    website = ""
    openingHours = []
    pictures = []
    averageStar = 0
    favorite = True
    review_list = [Review()]

    def __init__(self):
        pass

class openingHour:
    day = 0
    opens = 0000
    closes = 0000

class Address:
    street =""
    house_number = ""
    town = ""
    zip_code = 0

    def __init__(self):
        pass


class Review:
    starts = 0
    showName = True
    text = ""