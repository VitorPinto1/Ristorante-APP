from kivy.uix.screenmanager import Screen
from kivymd.uix.list import ThreeLineListItem
from kivy.clock import Clock
from tools.database import DatabaseService

class Reservation(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_id = None  

    def set_user_id(self, user_id):
        self.user_id = user_id
        self.load_reservations()

    def load_reservations(self):
        Clock.schedule_once(self.fetch_reservations)

    def fetch_reservations(self, *args):
        if self.user_id is not None:
            reservations = DatabaseService().userReservation(self.user_id)
            self.ids.reservation_list.clear_widgets()
            for reservation in reservations:
                self.ids.reservation_list.add_widget(
                    ThreeLineListItem(
                        text=f"Reservation at {reservation[1]}",  
                        secondary_text=f"Date: {reservation[2]}",
                        tertiary_text=f"Time: {reservation[3]}"
                    )
                )
        else:
            print("Error: user_id is not set")
