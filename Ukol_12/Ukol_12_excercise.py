flights =       {'Prague-Wien':271,
                'Prague-Denmark':626,
                'Prague-Tokyo':9110,
                'Prague-Warsaw':513}



class Plane:
    def __init__(self, color, capacity, speed, passangers):
        self.color = color
        self.capacity = capacity
        self.speed = speed
        self.passangers = passangers
    def change_colour(self, new_color):
        self.color = new_color

    def change_capacity(self, upgraded_capacity):
        self.capacity += upgraded_capacity
    
    def add_passangers(self, new_passangers):
        result = self.passangers + new_passangers
        if result <= self.capacity:
           self.passangers += new_passangers
        else:
            print('this plane cannot carry more passangers')
    
    def count_passangers(self):
        print(self.passangers)

    def get_flight_time(self, flight_path):
        if flight_path in flights:
            distance = flights[flight_path]
            time = distance / self.speed
            round_time = round(time, 1)
            print (f'this flight will be {round_time} hours long')
        else:
            print('this flight does not exist')





Aircraft_01 = Plane('silver', 215, 460, 180)





Aircraft_01.get_flight_time('Prague-Wien')

