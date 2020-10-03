from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.picker import MDDatePicker
import random
from kivy.clock import Clock
from kivymd.uix.snackbar import Snackbar
from kivymd.toast import toast
import requests
import json, threading

userdata = "a"

class SignupScreen(Screen):
    def get_date(self, date, *args):
        print(date)
        print(type(date))
        self.ids.date.text = str(date)

    def show_date_picker(self, *args):
        date_dialog = MDDatePicker(
            callback=self.get_date,
            year=random.randint(1997, 2005),
            month=random.randint(1, 12),
            day=random.randint(1, 28),
        )
        date_dialog.open()

    def on_enter(self, *args):

        menu_items = [{"icon": "gender-male", "text": "Male"},
                      {"icon": "gender-female", "text": "Female"},
                      {"icon": "gender-non-binary", "text": "Other"},
                      {"icon": "face", "text": "Prefer not to say"}]

        self.menu = MDDropdownMenu(
            caller=self.ids.gender,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item)

    def set_item(self, instance_menu, instance_menu_item):
        def set_item(interval):
            self.ids.gender.text = instance_menu_item.text
            instance_menu.dismiss()
        Clock.schedule_once(set_item, 0.5)
    
    
    def signup(self, *args):
        errors = 0

        import string

        def isEnglish(s):
            try:
                s.encode(encoding='utf-8').decode('ascii')
            except UnicodeDecodeError:
                return False
            else:
                return True

        # Check full name

        self.ids.flname.error = False
        self.ids.flname.helper_text = ""

        if isEnglish(self.ids.flname.text) == True:
            for char in self.ids.flname.text:
                if char in string.punctuation and char not in ['_', '.', ' ']:
                    self.ids.flname.error = True
                    self.ids.flname.helper_text = "Punctuations other than '.' and '_' aren't allowed!"
                    errors = 3
                else:
                    self.ids.flname.error = False

        else:
            self.ids.flname.error = True
            self.ids.flname.helper_text = "Non-English characters aren't allowed!"
            errors = 4

        # Check date

        from datetime import datetime
        date_obj = ''
        self.ids.date.error = False
        self.ids.date.helper_text = ""
        try:
            date_obj = datetime.strptime(self.ids.date.text, '%Y-%m-%d')
        except:
            self.ids.date.error = True
            self.ids.date.helper_text = "Incorrect date!"
            errors = 5

        # Check gender

        self.ids.gender.error = False
        self.ids.gender.helper_text = ""
        self.ids.gender.helper_text_mode = "on_focus"

        if self.ids.gender.text == 'Prefer not to say':
            self.ids.gender.text = 'Undefined'

        if self.ids.gender.text not in ['Male', 'Female', 'Other', 'Undefined']:
            self.ids.gender.error = True
            self.ids.gender.helper_text = "Incorrect gender!"
            errors = 6

        # Check Email
        import re

        self.ids.email.error = False
        self.ids.email.helper_text = ""

        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        print(self.ids.email.text)
        if not (re.search(regex, self.ids.email.text)):
            self.ids.email.error = True
            self.ids.email.helper_text = "Incorrect email format!"
            errors = 7

        # Check Password

        # self.ids.passw.error = False
        # self.ids.passw.helper_text = ""

        # if isEnglish(self.ids.passw.text) == False:
        #     self.ids.passw.error = True
        #     self.ids.passw.helper_text = "Non-English letters aren't allowed!"
        #     errors = 8

        # # Check Confirm Password

        # self.ids.conf_pass.error = False
        # self.ids.conf_pass.helper_text = ""

        # if isEnglish(self.ids.conf_pass.text) == False:
        #     self.ids.conf_pass.error = True
        #     self.ids.conf_pass.helper_text = "Non-English letters aren't allowed!"
        #     errors = 9

        # Check if password does't match

        self.ids.passw.error = False
        self.ids.conf_pass.error = False
        self.ids.passw.helper_text = ""
        self.ids.conf_pass.helper_text = ""

        if(self.ids.passw.text != self.ids.conf_pass.text):
            self.ids.passw.error = True
            self.ids.conf_pass.error = True
            self.ids.passw.helper_text = "Passwords do not match!"
            self.ids.conf_pass.helper_text = "Passwords do not match!"
            errors = 10

        # Upload to firebase
        print("Signing up...")
        print(str(errors))
        if errors == 0:
            print("No errors")
            
            toast('Creating account...')
            def go(self, *args):
                data = {
                    'fullname': self.ids.flname.text,
                    'bdate': self.ids.date.text,
                    'gender': self.ids.gender.text,
                    'email': self.ids.email.text,
                    'points': 0,
                    'rank': 'Newbie',
                    'pic': 'not_uploaded'
                }

                import pyrebase
                from .fbconfig import users_firebaseConfig

                firebase = pyrebase.initialize_app(users_firebaseConfig)
                auth = firebase.auth()

                email = self.ids.email.text
                password = self.ids.passw.text

                try:
                    signup = auth.create_user_with_email_and_password(email, password)
                    print(signup)
                    print(signup['localId'])
                    db = firebase.database()
                    db.child("users").child(signup['localId']).set(data)
                    Snackbar(text = "Account created successfully!").open()
                    global userdata
                    userdata = data

                    self.manager.current = 'login'
                except requests.exceptions.HTTPError as e:
                    error_json = e.args[1]
                    error = json.loads(error_json)['error']['message']
                    print(error)
                    if error == "EMAIL_EXISTS":
                        print("Email already exists!")
                        Snackbar(text = "Email already exists!").open()
                    elif error == "WEAK_PASSWORD":
                        print("Enter a stronger password!")
                        Snackbar(text = "Enter a stronger password!").open()
                    else:
                        print(error)
                        Snackbar(text = error).open()
            threading.Thread(target=go, args=(self, *args)).start()

