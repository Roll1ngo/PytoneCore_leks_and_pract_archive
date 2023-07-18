class Bus:
    def __init__(self, route):
        self.route = route
        self.passengers = []
        self.stopping = True
        
    def run(self):
        self.stopping = False
    
    def add_passenger(self, passenger):
        if self.stopping:
            self.passengers.append(passenger)
        else:
            return "Bus need to stop"
    
    def __enter__(self):
        self.stopping = True
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.run()


bus_567 = Bus("567")

bus_567.run()

with bus_567 as b:
    b.add_passenger("User")
    
print(bus_567.passengers)

print(bus_567.add_passenger("User_2"))