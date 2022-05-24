class Bus: 
    def __init__(self, route_number, destination):
        self.route_number = route_number 
        self.destination = destination 
        self.passenger = 0     
    
    def drive(self): 
        return "Brum brum"

    def passenger_count(self): 
        return self.passenger
    
    def pick_up(self, person):
        self.passenger += 1

    def drop_off(self, person):
        self.passenger -= 1  
    
    def empty(self):
        self.passenger = 0 
        return self.passenger
    
    def pick_up_from_stop(self, bus_stop):
        self.passenger_count = bus_stop.queue_length
        return self.passenger_count
