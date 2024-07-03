from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens import LoginScreen, MyReservation, Reservation

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
        return self.screen_manager

    def on_start(self):
        Window.orientation = 'portrait'
    
    def show_error_dialog(self, message):
        self.screen_manager.current_screen.show_error_dialog(message)

    def go_to_login(self):
        self.screen_manager.current = 'login'
    def go_to_welcome(self):
        self.screen_manager.current = 'Reservation'

if __name__ == '__main__':
    MyApp().run()
