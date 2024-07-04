from kivy.uix.screenmanager import Screen
from kivymd.uix.list import ThreeLineListItem
from kivy.clock import Clock
from tools.database import DatabaseService

class Reservation(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_id = None  

    def on_enter(self, *args):
        self.load_reservations()

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
                        text=f"Reservation name:  {reservation[1]}",  
                        secondary_text=f"Date: {reservation[3]}",
                        tertiary_text=f"Time: {reservation[4]}",
                        on_release=lambda x, reservation_info=reservation: self.reservation_details(reservation_info)
                    )
                )
        else:
            print("Error: user_id is not set")

    def reservation_details(self, reservation_info):
        reservation_detail_screen = self.manager.get_screen('MyReservation')
        reservation_detail_screen.reservation_data = reservation_info
        
        details = [
            f"Reservation number: {reservation_info[0]}",
            f"Name: {reservation_info[1]}",
            f"Date: {reservation_info[3]}",
            f"Time: {reservation_info[4]}",
            f"Total guests: {reservation_info[2]}"
           
        ]

        detail_text = "\n".join(filter(None, details))

        reservation_detail_screen.ids.detail_label.markup = True
        reservation_detail_screen.ids.detail_label.text = detail_text

        self.manager.current = 'MyReservation'
