from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens import LoginScreen, MyReservation, Reservation, ReservationModification

import os
from dotenv import load_dotenv




Window.size = (360, 640)

class MyApp(MDApp):
    def build(self):
        Builder.load_file('screens.kv')
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(LoginScreen(name='login'))
        self.screen_manager.add_widget(MyReservation(name='MyReservation'))
        self.screen_manager.add_widget(Reservation(name='Reservation'))
        self.screen_manager.add_widget(ReservationModification(name='ReservationModification'))
        return self.screen_manager

    def on_start(self):
        Window.orientation = 'portrait'
    
    def show_error_dialog(self, message):
        self.screen_manager.current_screen.show_error_dialog(message)

    def show_date_picker(self):
        current_screen = self.screen_manager.current_screen
        if isinstance(current_screen, ReservationModification):
            current_screen.show_date_picker()

    def show_time_picker(self):
        current_screen = self.screen_manager.current_screen
        if isinstance(current_screen, ReservationModification):
            current_screen.show_time_picker()


    def go_to_login(self):
        self.screen_manager.current = 'login'
    def go_to_reservation(self):
        reservation_screen = self.root.get_screen('Reservation')
        reservation_screen.load_reservations()
        self.root.current = 'Reservation'
    def go_to_modification(self):
        self.screen_manager.current = 'ReservationModification'
    
    def save_modification(self):
        current_screen = self.screen_manager.current_screen
        if isinstance(current_screen, ReservationModification):
            current_screen.save_modification()

if __name__ == '__main__':
    MyApp().run()
