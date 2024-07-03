from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from tools.database import DatabaseService
import bcrypt  


class LoginScreen(Screen):
    def login(self):
        username = self.ids.username_field.text
        password = self.ids.password_field.text

        if not username or not password:
            self.show_error_dialog("Please enter your username and password")
            return
        
        db_service = DatabaseService()
        user = db_service.userName(username)
      
        if user:
            stored_password_hash = user[2]  
            if stored_password_hash:
                try:
                    if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                        reservation_screen = self.manager.get_screen('Reservation')
                        reservation_screen.set_user_id(user[0])
                        self.manager.current = 'Reservation'
                    else:
                        self.show_error_dialog("The password is incorrect")
                except ValueError as e:
                    print(f"Error verifying password hash: {e}")
                    self.show_error_dialog("An error occurred during login")
            else:
                self.show_error_dialog("Stored password hash is invalid")
        else:
            self.show_error_dialog("The user was not found")

    def show_error_dialog(self, message):
        ok_button = MDFlatButton(
            text="OK",
            on_release=lambda x: self.dialog.dismiss()
        )
        if hasattr(self, 'dialog'):
            self.dialog.text = message
            self.dialog.buttons = [ok_button]
        else:
            self.dialog = MDDialog(
                text=message,
                buttons=[ok_button]
            )
        self.dialog.open()
