from kivy.uix.screenmanager import Screen
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from datetime import datetime, timedelta, time
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.metrics import dp
from tools.database import DatabaseService

class ReservationModification(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reservation_info = None
        self.dialog = None

    def on_enter(self, *args):
     

        if self.reservation_info:
            self.ids.date_field.text = str(self.reservation_info[3])
            self.ids.time_field.text = str(self.reservation_info[4])
            self.ids.total_guests_field.text = str(self.reservation_info[2])
        
    def set_reservation_info(self, reservation_info):
     
        self.reservation_info = reservation_info

    def save_modification(self):
        date = self.ids.date_field.text
        time = self.ids.time_field.text
        total_guests = self.ids.total_guests_field.text
        
        if date and time and total_guests and self.reservation_info:
            try:
                total_guests = int(total_guests)
                if total_guests < 1 or total_guests > 10:
                    raise ValueError
            except ValueError:
                self.show_error_dialog("Total guests must be between 1 and 10")
                return


            reservation_id = self.reservation_info[0]
            DatabaseService().update_reservation(reservation_id, date, time, total_guests)
            MDApp.get_running_app().go_to_reservation()

        else:
            missing_fields = []
            if not date:
                missing_fields.append("Date")
            if not time:
                missing_fields.append("Time")
            if not total_guests:
                missing_fields.append("Total Guests")
            if not self.reservation_info:
                missing_fields.append("Reservation Data")
            self.show_error_dialog(f"Missing required fields or reservation data: {', '.join(missing_fields)}")

    def show_date_picker(self):
        date_picker = MDDatePicker(
            min_date=datetime.now().date(),
            max_date=(datetime.now() + timedelta(days=365)).date(),
        )
        date_picker.bind(on_save=self.on_save_date, on_cancel=self.on_cancel_date)
        date_picker.open()

    def on_save_date(self, instance, value, date_range):
        if value.weekday() != 0 and value >= datetime.now().date():  # 0 is Monday
            self.ids.date_field.text = value.strftime('%Y-%m-%d')
        else:
            self.show_error_dialog("Invalid date selected: Mondays or past dates are not allowed")

    def on_cancel_date(self, instance, value):
        self.show_error_dialog("Date picker cancelled")
    
    def show_time_picker(self):
        time_picker = MDTimePicker()
        time_picker.bind(on_save=self.on_save_time, on_cancel=self.on_cancel_time)
        time_picker.open()

    def on_save_time(self, instance, value):
        if time(12, 0) <= value <= time(23, 59):
            self.ids.time_field.text = value.strftime('%H:%M')
        else:
            self.show_error_dialog("Invalid time selected: Please select a time between 12:00 and 00:00")

    def on_cancel_time(self, instance, value):
        self.show_error_dialog("Time picker cancelled")

    def show_error_dialog(self, error_message):
        if not self.dialog:
            self.dialog = MDDialog(
                text=error_message,
                buttons=[
                    MDFlatButton(
                        text="Close",
                        on_release=self.close_dialog
                    )
                ]
            )
        self.dialog.text = error_message
        self.dialog.open()

    def close_dialog(self, instance):
        self.dialog.dismiss()
