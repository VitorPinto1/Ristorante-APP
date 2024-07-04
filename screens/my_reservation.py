from kivy.uix.screenmanager import Screen
from kivymd.uix.list import ThreeLineListItem
from kivy.clock import Clock
from tools.database import DatabaseService

class MyReservation(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reservation_data = None

    def set_reservation_data(self, reservation_info):
        self.reservation_data = reservation_info
        
        details = [
            f"Reservation number: {reservation_info[0]}",
            f"Name: {reservation_info[1]}",
            f"Date: {reservation_info[3]}",
            f"Time: {reservation_info[4]}",
            f"Total guests: {reservation_info[2]}"
        ]

        detail_text = "\n".join(filter(None, details))

        self.ids.detail_label.markup = True
        self.ids.detail_label.text = detail_text

    def modify_reservation(self):
        modification_screen = self.manager.get_screen('ReservationModification')
        modification_screen.set_reservation_info(self.reservation_data)
        self.manager.current = 'ReservationModification'