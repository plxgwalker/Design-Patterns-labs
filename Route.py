from geopy.geocoders import Nominatim
import openrouteservice
from Ticket import Ticket


client = openrouteservice.Client(key="5b3ce3597851110001cf6248ce91032d4996451daa881cebcd9f7464")
geolocator = Nominatim(user_agent="test-app")


class Route:
    """Class Route represents calculation of ticket parameters.

    Arguments:
        start_point (str): Start point of 'Route'.
        finish_point (str): Finish point of 'Route'.

    Methods:
        get_longitude_of_start_point () -> float:
            Transforming from string location to longitude in float.

        get_latitude_of_start_point () -> float:
            Transforming from string location to latitude in float.

        get_longitude_of_finish_point () -> float:
            Same as get_longitude_of_start_point () but returns finish point.

        get_latitude_of_finish_point () -> float:
            Same as get_latitude_of_start_point () but returns finish point.

        route_info (ticket: Ticket) -> list:
            Returns list of information about the 'Route': distance, time in hours, start and finish point.

        """
    def __init__(self, start_point: str, finish_point: str):
        self.start_point = start_point
        self.finish_point = finish_point

    def get_longitude_of_start_point(self) -> float:
        location = geolocator.geocode(self.start_point)
        lng = location.longitude
        return float(lng)

    def get_latitude_of_start_point(self) -> float:
        location = geolocator.geocode(self.start_point)
        lat = location.latitude
        return float(lat)

    def get_longitude_of_finish_point(self) -> float:
        location = geolocator.geocode(self.finish_point)
        lng = location.longitude
        return float(lng)

    def get_latitude_of_finish_point(self) -> float:
        location = geolocator.geocode(self.finish_point)
        lat = location.latitude
        return float(lat)

    def route_info(self, ticket: Ticket) -> list:
        match ticket.ticket_info.transport_type:
            case "Train":
                coordinates = ((self.get_longitude_of_start_point(), self.get_latitude_of_start_point()),
                               (self.get_longitude_of_finish_point(), self.get_latitude_of_finish_point()))
                routes = client.directions(coordinates, profile="driving-hgv")

            case "Bus":
                coordinates = ((self.get_longitude_of_start_point(), self.get_latitude_of_start_point()),
                               (self.get_longitude_of_finish_point(), self.get_latitude_of_finish_point()))
                routes = client.directions(coordinates, profile="driving-hgv")

            case "Truck":
                coordinates = ((self.get_longitude_of_start_point(), self.get_latitude_of_start_point()),
                                (self.get_longitude_of_finish_point(), self.get_latitude_of_finish_point()))
                routes = client.directions(coordinates, profile="driving-hgv")

        distance = round(routes['routes'][0]['summary']['distance'] / 1000, 1)
        time_in_hours = round(routes['routes'][0]['summary']['duration'] / 3600, 1)

        route_info = [distance, time_in_hours, self.start_point, self.finish_point]
        return route_info
