# Ukol 13, Kompozice, Dědičnost

# 3 příklady kompozice
    # 1. Hotel - pokoje
    # 2. Vysílačka - mikrofon (vysílačka má jeden mikrofon)
    # 3. Myš - tlačítka (myš má levé a pravé tlačítko)

# 3 příklady dědičnosti
    # Šelmy kočkovité(parent) - kočka(child)
    # Klávesnice(parent) - Mechanická Klávesnice(child)
    # myš - herní myš

class Room:
    def __init__(self, room_number: int, room_capacity: int):
        self.room_number = room_number
        self.room_capacity = room_capacity


class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = {} #číslo pokoje/ jeho kapacita


    def add_room(self, room: Room):
        if room.room_number not in self.rooms.keys():
            self.rooms[room.room_number] = room.room_capacity
        else:
            return('this room has been added')

    def remove_room(self, room_number):
        self.rooms.pop(room_number)
    
    def show_room_dict(self):
        print(f'List of rooms: {self.rooms}')

    def show_hotel_capacity(self):
        result = []
        for value in self.rooms.values():
            result.append(value)
        return sum(result)




room_1 = Room(1, 3)
room_2 = Room(2, 4)
room_3 = Room(3, 2)


hotel_1 = Hotel('Orion')

hotel_1.add_room(room_1)
hotel_1.add_room(room_3)
hotel_1.add_room(room_2)
hotel_1.show_room_dict()
print(hotel_1.show_hotel_capacity())




class Mouse:
    def __init__(self, name, dpi: int):
        self.name = name
        self.dpi = dpi

    def left_click():
        print('left click')

    def right_click():
        print('right click')

    def scroll_wheel():
        print('scroll wheel')



class GamingMouse(Mouse):

    def __init__(self, name, dpi):
        super().__init__(name, dpi)
        self.rgb_light_color = 'Red'

    def change_dpi_button(self):
        if self.dpi < 150:
            print('you cant set lower dpi')
        self.dpi += 150

    def change_rgb_color(self, new_color):
        self.rgb_light_color = new_color



