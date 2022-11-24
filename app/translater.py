from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="test-app")


class City:
    def __init__(self, city: str):
        self.city = city

    def get_longitude(self) -> float:
        location = geolocator.geocode(self.city)
        lng = location.longitude
        return float(lng)

    def get_latitude(self) -> float:
        location = geolocator.geocode(self.city)
        lat = location.latitude
        return float(lat)
        