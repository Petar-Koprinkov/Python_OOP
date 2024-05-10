from typing import List
from hotel.project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.room: List[Room] = []

    @property
    def guests(self):
        return sum([room.guests for room in self.room])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.room.append(room)

    def take_room(self, room_number: int, people: int):
        room = [r for r in self.room if r.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number: int):
        room = [r for r in self.room if r.number == room_number][0]
        return room.free_room()

    def status(self):
        free_room = [str(room.number) for room in self.room if not room.is_taken]
        taken_room = [str(room.number) for room in self.room if room.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_room)}\n" \
               f"Taken rooms: {', '.join(taken_room)}"
