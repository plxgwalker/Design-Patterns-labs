from fastapi import FastAPI
from enum import Enum

from Route import Route
from Depo import Depo, DepoInfo
from Schedule import Schedule
from Passenger import Passenger, PassengerInfo


class TransportType(str, Enum):
    bus = "Bus"
    train = "Train"
    truck = "Truck"


depos = []
passengers = []
schedule_v = Schedule([])

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/create_depo/{depo_name}")
async def create_depo(depo_name: str) -> str:
    for depo in depos:
        if depo_name == depo.depo_info.city:
            return "This city already in use! Try another one."

    new_depo = Depo()
    new_depo.depo_info = DepoInfo(0, depo_name, [], [], [], [])

    temp_id = len(depos)
    new_depo.depo_info.id = temp_id

    depos.append(new_depo)
    return new_depo.depo_info


@app.post("/{depo_name}/create_tickets")
async def create_tickets(depo_name: str, b_point: str, amount: int, transport_type: TransportType):
    for depo in depos:
        if depo_name == depo.depo_info.city:

            if transport_type is TransportType.bus:
                depo.create_tickets(b_point, amount, "Bus")
                return depo.print_all_tickets()

            elif transport_type is TransportType.train:
                depo.create_tickets(b_point, amount, "Train")
                return depo.print_all_tickets()

            elif transport_type is TransportType.truck:
                depo.create_tickets(b_point, amount, "Truck")
                return depo.print_all_tickets()

        else:
            return "No cities with this name! Try another one."


@app.get("/depo_list")
async def get_list_of_depos():
    return depos


@app.get("/schedule/{depo_name}")
async def get_schedule(depo_name: str):
    for depo in depos:
        if depo_name == depo.depo_info.city:
            schedule_v.create_schedule(depo.depo_info.tickets)
            return schedule_v.schedule


@app.get("/calculate_route/{point_a}_{point_b}")
async def calculate_route(point_a: str, point_b: str) -> list:
    new_route = Route(point_a, point_b)
    return new_route.route_info()


@app.post("/create_passenger")
async def create_passenger(first_name: str, last_name: str, age: int):
    new_passenger = Passenger()
    new_passenger.passenger_info = PassengerInfo(len(passengers), first_name, last_name, age, [])

    passengers.append(new_passenger)
    return new_passenger


@app.get("/passenger_list")
async def get_list_of_passengers():
    return passengers


@app.get("/passenger_buy_ticket")
async def passenger_buy_ticket(depo_name: str, passenger_id: int):
    for depo in depos:
        if depo_name == depo.depo_info.city:
            for passenger in passengers:
                if passenger_id == passenger.passenger_info.id:
                    depo.buy_ticket(passenger)
                    return passenger.passenger_info.tickets, depo.depo_info.tickets
                else:
                    return "No user with this ID!"
        else:
            return "No depo with this name!"
