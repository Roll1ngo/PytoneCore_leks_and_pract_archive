from collections import UserDict


class Seat:
    def __init__(self, sector, number):
        self.sector = sector
        self.status = False
        self.number = number

    def __str__(self):
        return f"seat {self.number} in sector {self.sector}"

    def __repr__(self):
        return str(self)


class Stadium(UserDict):
    def add_seats(self, seats: list[Seat]):
        for seat in seats:
            self.data[(seat.sector, seat.number)] = seat
        return f"{len(seats)} add success"

    # def get_seat_by_sector(self, sector):
    #     seats  = filter(lambda x: x.sector == sector, self.seats)
    #     if seats:
    #         return list(seats)

    # def sold_seat(self,sector,seat_number):


seats = []


stadium = Stadium(seats)

for seat in stadium.seats:
    print(seat)
