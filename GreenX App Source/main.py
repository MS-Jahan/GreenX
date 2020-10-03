from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.expansionpanel import MDExpansionPanelOneLine
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.label import MDLabel
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.list import MDList
from kivymd.toast import toast
from kivy.utils import platform
from kivymd.uix.filemanager import MDFileManager
import random
import time
import requests, urllib.request, shutil, threading
import json
import os
import matplotlib.pyplot as plt
from kivy.clock import Clock
from screen_nav import screen_manager
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.base import EventLoop
from kivy.config import Config
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()

Config.set('kivy', 'exit_on_escape', '0')
#Window.size = (720, 1440)


screensArr = []
file_manager = ''
isOpenFM = False
isLoggedIn = 0
location = "Dhaka"
previous_screen = "splash"
weatherData_main = ""
weatherData_other = {}
termtext = "\n\n"
lat = 11
lon = 11
#graphName = 'graph_1601096669.png'
name = ""
localID = '3234' # LocalID is used as userID, for each user
ts = '' # Post Timestamp
loading = ""
userdata = {
                'fullname': "Mr Newbie",
                'pic': 'URL',
                'bdate': "1992-2-2",
                'gender': "Male",
                'email': "ss@mail.com",
                'points': 0,
                'rank': 'Newbie',
                'pic' : 'not_uploaded'
            }

ele_data = "Temperature"
per_data = "Interannual"
img_gal = 'apod'
img_link = 'cache/apod'

imggalData = ''

class SplashScreen(Screen):    

    def on_enter(self, *args):
        global screensArr
        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)

# class SignupScreen(Screen):
from screens.signup import SignupScreen


class LoginScreen(Screen):

    def on_enter(self, *args):
        global isLoggedIn

        if isLoggedIn == 1:
            self.manager.current = 'input'

        global screensArr
        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)
        
        if os.path.isfile('helper.tn') == True:
            Snackbar(text="Logging in with saved credentials...").open()
            def go(self, *args):
                with open("helper.tn", 'r') as f:
                    message = f.read()

                import base64
                message = message.encode('ascii')
                message = base64.b64decode(message)
                message = message.decode('ascii')
                message = message.split('+')
                self.ids.email.text = message[0]
                self.ids.password.text = message[1]
                self.login()
            threading.Thread(target=go, args = (self, *args)).start()
    
    def login(self, *args):
        
        if self.ids.email.text != '' and self.ids.password.text != '':

            global localID, isLoggedIn, userdata

            import pyrebase
            import requests, json
            from screens import fbconfig
        
            firebaseConfig = fbconfig.users_firebaseConfig
            firebase = pyrebase.initialize_app(firebaseConfig)
            auth = firebase.auth()

            try:
                user = auth.sign_in_with_email_and_password(self.ids.email.text, self.ids.password.text)
                #print(user)
                print(user['localId'])
                localID = user['localId']
                Snackbar(text="Logged in successfully!").open()
                isLoggedIn = 1
                import base64

                message = self.ids.email.text + "+" + str(self.ids.password.text)
                message = message.encode('ascii')
                message = base64.b64encode(message)
                message = message.decode('ascii')
                print(message)

                with open('helper.tn', 'w') as f:
                    f.write(message)
                
                #global userdata, localID

                config = fbconfig.users_firebaseConfig
                firebase = pyrebase.initialize_app(config)
                db = firebase.database()
                userdata = db.child('users/' + localID).get()
                userdata = userdata.val()
                print(userdata)

                self.manager.current = 'input'
            except requests.HTTPError as e:
                #print('args start')
                error_json = e.args[1]
                #print(error_json)
                error = json.loads(error_json)['error']['message']
                #print(error)
                msg = ''
                if error == "INVALID_EMAIL":
                    msg = "Invalid email!"
                elif error == "EMAIL_NOT_FOUND":
                    msg = "Email not found!"
                elif error == 'INVALID_PASSWORD':
                    msg = "Wrong Password!"
                else:
                    msg = "Something's wrong. Check your internet connection."
                
                Snackbar(text=msg).open()
                if os.path.isfile('helper.tn') == True:
                    os.remove('helper.tn')
        else:
            Snackbar(text="Please enter email and password first!").open()
    
    def forgot(self, *args):
        if self.ids.email.text != '':
            import pyrebase
            import requests, json
            from screens import fbconfig
        
            firebaseConfig = fbconfig.users_firebaseConfig
            firebase = pyrebase.initialize_app(firebaseConfig)
            auth = firebase.auth()

            try:
                user = auth.send_password_reset_email(self.ids.email.text)
                Snackbar(text="Password reset code has been sent to email!").open()
            except requests.HTTPError as e:
                #print('args start')
                error_json = e.args[1]
                #print(error_json)
                error = json.loads(error_json)['error']['message']
                #print(error)
                msg = ''
                if error == "INVALID_EMAIL":
                    msg = "Invalid email!"
                elif error == "EMAIL_NOT_FOUND":
                    msg = "Email not found!"
                else:
                    msg = "Something's wrong. Check your internet connection."
                
                Snackbar(text=msg).open()
                if os.path.isfile('helper.tn') == True:
                    os.remove('helper.tn')

        else:
            Snackbar(text="Please enter only email to reset password!").open()

    def on_pre_leave(self, *args):
        global name, loading
        name = self.ids.email.text
        loading = "input"
        screensArr.pop()

class InputScreen(Screen):    

    def go(self, *args):
        global loading
        loading = "data"
        self.manager.current = 'load'    

    def on_pre_enter(self, *args):
        global userdata

        self.ids.username_nav.text = "  " + userdata['fullname']
        self.ids.rank_nav.text = "   Rank: " + userdata['rank']
        self.ids.point_nav.text = "    " + str(userdata['points']) + " Points"


    def on_pre_leave(self, *args):
        global location, previous_screen

        #print(Nasa2020().userdata)

        previous_screen = 'splash'
        location = self.ids.location_input.text
        location = location.capitalize()
        print(location)

    def on_enter(self, *args):
        global userdata, screensArr
        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)
        
        
        data = {
            'image-plus': 'Upload Image',
            'pencil-box-multiple-outline': 'Write Status',
            'message-reply-text': 'Message'
        }

        self.ids.float_button.data = data

        #self.ids.nav_drawer.set_state("open")

    

class LoadingScreen(Screen):

    def on_pre_enter(self, *args):
        if loading == 'ndv':
            self.ids.msg.text = "This might take a while..."

    def on_enter(self):
        global previous_screen, location, weatherData_main, weatherData_other, lat, lon, loading
        previous_screen = 'input'

        print(loading)

        if loading == "data":

            def stopSpinner(*args):
                self.ids.spinner.active = False
                self.manager.current = 'data'

            
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
            CITY = location
            API_KEY = "OpenWeatherMap API KEY"
            URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

            response = ''

            try:
                response = requests.get(URL)
                print(response.json())
                
                if response.status_code == 200:
                    data = response.json()
                    weatherData_main = data['main']
                    lat = data['coord']['lat']
                    lon = data['coord']['lon']
                    weatherData_other['wind'] = data['wind']['speed']
                    weatherData_other['weather'] = data['weather'][0]['main']
                    weatherData_other['country'] = data['sys']['country']
                    print(str(lat) + " | " + str(lon))
                    #stop = stopSpinner(self)
                    Clock.schedule_once(stopSpinner, 0.5)
                else:
                    Snackbar(text="Wrong Location or server unavailable!").open()
                    #Clock.schedule_once(stopSpinner, 5)
                    self.manager.current = 'input'

            except(requests.ConnectionError, requests.Timeout):
                Snackbar(text="No internet connection!").open()
                #Clock.schedule_once(stopSpinner, 3)
                self.manager.current = 'input'

        elif loading == "input":
            self.manager.current = 'input'
        elif loading == 'ndv':
            self.ids.msg.text = "This might take a while..."
            def get(*args):
                global img_gal, img_link, imggalData
                if img_gal == 'apod':
                    url = "https://api.nasa.gov/planetary/apod?api_key=APIKEY"
                    response = requests.get(url)
                    print(response)
                    imggalData = response.json()
                    if imggalData['media_type'] == 'image':
                        #self.ids.img.source = self.link
                        #import requests

                        urllib.request.urlretrieve(imggalData['url'], 'img.jpg')
                        

                        img_link = 'img.jpg'
                        print(img_link)

                        #shutil.move('img.jpg', img_link)
                        
                self.manager.current = 'ndv'
            #Snackbar(text = "This may take a while... Be patient!").open()
            #threading.Thread(target=Snackbar(text = "Getting Data...").open()).start()
            get()
            #Clock.schedule_once(get, 2.5)
         
    def on_pre_leave(self, *args):
        global loading, screensArr
        loading = ''
        print(self.manager.current, screensArr)


class DataScreen(Screen):

    def on_pre_enter(self, *args):
        global userdata
        self.ids.username_nav.text = "  " + userdata['fullname']
        self.ids.rank_nav.text = "   Rank: " + userdata['rank']
        self.ids.point_nav.text = "    " + str(userdata['points']) + " Points"

    def on_enter(self, *args):
        global location, previous_screen, weatherData_main, weatherData_other, name, screensArr
        previous_screen = 'input'

        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)

        self.ids.data_scr_header.text = location
        self.ids.temp.text = str(round(float(weatherData_main['temp']) - 273, 2)) + "°C"

        self.ids.temp.theme_text_color = "Custom"
        self.ids.temp.text_color = 45/255, 179/255, 0, 1

        if round(float(weatherData_main['temp']) - 273, 2) > 32:
            self.ids.temp.theme_text_color = 'Error'

        self.ids.humid.text = str(weatherData_main['humidity']) + "%"

        self.ids.humid.theme_text_color = "Custom"
        self.ids.humid.text_color = 45/255, 179/255, 0, 1

        if round(float(weatherData_main['humidity'])) > 80:
            self.ids.humid.theme_text_color = 'Error'

        
        self.ids.country.text = weatherData_other['country']


        

        self.ids.weather.text = weatherData_other['weather']

        # self.ids.trees.theme_text_color = "Custom"
        # self.ids.trees.text_color = 45/255, 179/255, 0, 1

        # if trees < 20:
        #     self.ids.trees.theme_text_color = 'Error'

        self.ids.pressure.text = str(weatherData_main['pressure']) + " hPa"

        # if weatherData_main['pressure'] > 1200 or weatherData_main['pressure'] < 1100:
        #	self.ids.pressure.theme_text_color = 'Error'

        self.ids.wind.text = str(weatherData_other['wind']) + " m/s"
        #self.ids.co2.theme_text_color = 'Error'

        data = {
            'image-plus': 'Upload Image',
            'pencil-box-multiple-outline': 'Write Status',
            'message-reply-text': 'Message',
            'map-marker': 'Check Map',
        }

        self.ids.ddata.data = data

        global userdata
        
        self.ids.username_nav.text = "  " + userdata['fullname']
        self.ids.rank_nav.text = "   Rank: " + userdata['rank']
        self.ids.point_nav.text = "    " + str(userdata['points']) + " Points"

class MapScreen(Screen):

    def on_enter(self):
        global lat, lon, previous_screen, screensArr

        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)

        previous_screen = 'data'
        print(str(lat) + " | " + str(lon))
        self.ids.mapv.lat = lat
        self.ids.mapv.lon = lon
        #self.ids.mapv.zoom = int(5)

        self.ids.mapv_pop.lat = lat
        self.ids.mapv_pop.lon = lon


class ContribScreen(Screen):
    def on_enter(self, *args):
        global screensArr
        screensArr.append(self.manager.current)


class VideoScreen(Screen):

    def on_enter(self, *args):
        global screensArr
        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)

    def on_pre_leave(self):
        self.ids.vid.state = 'stop'


class RoboScreen(Screen):

    def addLines(self, *args):
        global termtext
        self.ids.roboterm.text = termtext
        #self.manager.current = 'robo'

    def on_enter(self):
        global location, termtext, lat, lon, screensArr
        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)

        self.ids.roboterm.text = ""

        termtext += "\n\n\n\n\n\n\n\n\n\n\n\n\n\n========= BOT TERMINAL ========="

        termtext += "\n\n\n\n\nConnecting to Local RoboEarth (" + location.lower(
        ) + ".roboeserver.org:443)"
        Clock.schedule_once(self.addLines, 1)
        # addLines(termtext)

        termtext += "\nConnected (STATUS 200 OK)"
        # addLines(termtext)
        Clock.schedule_once(self.addLines, 4)

        termtext += "\nSent data request..."
        Clock.schedule_once(self.addLines, 7)
        # addLines(termtext)

        termtext += "\n\n\n--------- DATA ---------\n\nTemperature: " + \
            str(random.randint(28, 34)) + "°C"
        termtext += "\nHumidity: " + str(random.randint(69, 79)) + "%"
        termtext += "\nWind: " + str(random.randint(3, 9)) + " kmph"
        termtext += "\nAir Pressure: " + \
            str(random.randint(1000, 1010)) + " hPa"
        termtext += "\n\nLatitude: " + str(lat) + " | Longitude: " + str(lon)

        termtext += "\n\n\n\n\nPress Back to exit."

        Clock.schedule_once(self.addLines, 7)


class NasaScreen(Screen):

    def from_get_date(self, date, *args):
        print(date)
        print(type(date))
        self.ids.fromd.text = str(date)

    def from_show_date_picker(self, *args):
        date_dialog = MDDatePicker(
            callback=self.from_get_date,
            year=2016,
            month=random.randint(1, 12),
            day=random.randint(1, 28),
        )
        date_dialog.open()

    def to_get_date(self, date, *args):
        print(date)
        print(type(date))
        self.ids.to.text = str(date)

    def to_show_date_picker(self, *args):
        date_dialog = MDDatePicker(
            callback=self.to_get_date,
            year=2017,
            month=random.randint(1, 12),
            day=random.randint(1, 28),
        )
        date_dialog.open()


    def on_enter(self):
        global screensArr
        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)

        self.ids.fromd.text = "2016-01-01"
        self.ids.to.text = "2016-12-31"
        
        try:
            self.remove_widget(spinner)
            self.remove_widget(label)
        except:
            pass

        ele_menu_items = [{"icon": "thermometer", "text": "Temperature"},
                          {"icon": "water", "text": "Moisture"},
                          {"icon": "weather-windy", "text": "Wind"}
                         ]

        self.ele_menu = MDDropdownMenu(
            caller=self.ids.ele_drop_item,
            items=ele_menu_items,
            position="bottom",
            width_mult=4,
        )
        self.ele_menu.bind(on_release=self.ele_set_item)

        per_menu_items = [{"icon": "calendar-today", "text": "Daily"},
                          {"icon": "calendar-clock", "text": "Interannual"}
                         ]

        self.per_menu = MDDropdownMenu(
            caller=self.ids.per_drop_item,
            items=per_menu_items,
            position="bottom",
            width_mult=4,
        )
        self.per_menu.bind(on_release=self.per_set_item)

    def ele_set_item(self, instance_menu, instance_menu_item):
        self.ids.ele_drop_item.set_item(instance_menu_item.text)
        global ele_data
        ele_data = instance_menu_item.text
        self.ids.ele_drop_item.text = instance_menu_item.text
        print(self.ids.ele_drop_item.text)
        self.ele_menu.dismiss()

    def per_set_item(self, instance_menu, instance_menu_item):
        self.ids.per_drop_item.set_item(instance_menu_item.text)
        global per_data
        per_data = instance_menu_item.text
        self.ids.per_drop_item.text = instance_menu_item.text
        print(self.ids.per_drop_item.text)
        self.per_menu.dismiss()

    def fetchData(self, *args):
        global lat, lon

        spinner = MDSpinner(
            size_hint=(None, None),
            size=(46, 46),
            pos_hint={'center_x': .5, 'center_y': .2},
            active=True,
        )

        self.add_widget(spinner)

        label = MDLabel(
            pos_hint={'center_y': 0.1},
            text="This may take a while",
            halign="center",
        )
        self.add_widget(label)

        def graphPlot(category, parameter, *args):
            def snk(*args):
                Snackbar(text = "Getting Data...").open()
            Clock.schedule_once(snk, 0.1)
            cat = ''
            para = ''
            if category == 'Interannual':
                cat = "INTERANNUAL"
                url = "https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?&request=execute&identifier=SinglePoint&parameters=" + parameter + "&startDate=" + self.ids.fromd.text[:4].replace('-','') + "&endDate=" + self.ids.to.text[:4].replace('-','') +"&userCommunity=AG&tempAverage=" + cat + "&outputList=JSON&lat=" + str(lat) + "&" + "lon=" + str(lon)
            else:
                cat = "DAILY"
                url = "https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?&request=execute&identifier=SinglePoint&parameters=" + parameter + "&startDate=" + self.ids.fromd.text.replace('-','') + "&endDate=" + self.ids.to.text.replace('-','') +"&userCommunity=AG&tempAverage=" + cat + "&outputList=JSON&lat=" + str(lat) + "&" + "lon=" + str(lon)

            if parameter == 'T2M_RANGE':
                para = 'Temperature (C)'
            elif parameter == 'RH2M':
                para = 'Moisture (%)'
            else:
                para = 'Wind Speed (m/s)'

            
            print(url)
            try:
                response = requests.get(url)
                print(response)
                data = response.json()

                data = data['features'][0]['properties']['parameter'][parameter]

                dates = []
                values = []

                for key, value in data.items():
                    if category == 'Interannual': 
                        if key[-2:] != '13' and value >= 0:
                            dates.append(key)
                            values.append(value)
                            print(key + " " + str(value))
                    else:
                        dates.append(key)
                        values.append(value)
                        print(key + " " + str(value))

                import matplotlib.pyplot as plt

                plt.figure(figsize=(17,10))        
                plt.plot(dates, values)
                plt.title(para + ' Vs Year')
                plt.xlabel('Year')
                plt.ylabel(para)
                plt.xticks(rotation=90)
                #my_path = os.path.dirname(os.path.realpath(__file__))

                global graphName
                graphName = 'graphs/graph_' + str(int(time.time())) + '.png'
                print(graphName)

                plt.savefig(graphName, bbox_inches='tight')

                #self.manager.current = 'graph'
                def changeScreen(*args):
                    self.manager.current = 'ndata'

                Clock.schedule_once(changeScreen, 1)
                
            except Exception as e:
                try:
                    self.remove_widget(spinner)
                    self.remove_widget(label)
                except:
                    pass
                print("Error")
                print(e)
                self.manager.current = "nasa"
                Snackbar(text="Can't get data from Nasa!").open()
        
        print(self.ids.ele_drop_item.text)
        print(self.ids.per_drop_item.text)
        
        if self.ids.ele_drop_item.text == 'Temperature':
            graphPlot(self.ids.per_drop_item.text, 'T2M_RANGE')
        elif self.ids.ele_drop_item.text == 'Moisture':
            graphPlot(self.ids.per_drop_item.text, 'RH2M')
        elif self.ids.ele_drop_item.text == 'Wind':
            graphPlot(self.ids.per_drop_item.text, 'WS2M')
        else:
            Snackbar(text="Select Search Topic and Period first!").open()
            

class NDataScreen(Screen):
    
    def on_enter(self, *args):
        global graphName, screensArr
        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)

        self.ids.graph_img.background_normal = graphName
        self.ids.graph_img.background_down = graphName
        self.ids.graph_img.text = 'Click to view'

class GraphScreen(Screen):        

    def on_pre_enter(self, *args):
        global graphName
        self.ids.img_viewer.source = graphName
    def on_enter(self, *args):
        global screensArr
        screensArr.append(self.manager.current)

class SuggestionScreen(Screen):
    def on_enter(self, *args):
        global screensArr
        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)

class PostScreen(Screen):

    def on_enter(self, *args):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
            #import os, shutil
            # if os.path.isdir("/storage/emulated/0") == True:
            #     try:
            #         os.remove('/storage/emulated/0/test_Folder_greenx')
            #     except:
            #         pass
                
            #     try:
            #         os.mkdir('/storage/emulated/0/test_Folder_greenx')
            #         #Snackbar(text="Syllabus saved to internal storage.").open()
            #     except:
            #         def func(*args):
            #             Snackbar(text="Please allow storage permission to upload images.").open()
            #         Clock.schedule_once(func, 0.1)
            # else:
            #     Snackbar(text="Please accept storage permission.").open()


        global screensArr
        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)
        self.link = ''
        self.files = []
        #self.fpath = '/'  # path to the directory that will be opened in the file manager
        global file_manager
        file_manager = MDFileManager(
            exit_manager=self.exit_manager,  # function called when the user reaches directory tree root
            select_path=self.select_path,  # function called when selecting a file/directory
            #preview=True
        )

        self.imgList = MDList()
    
    def storageLink(self, link, *args):
        self.link = link
        # if link == 'memcard':
        #     from jnius import autoclass
        #     try:
        #         Environment = autoclass('android.os.Environment')
        #         Environment.getExternalStorageDirectory().getAbsolutePath()
        #         #self.link = sdpath

        #     # Not on Android
        #     except:
        #         Snackbar(text = "Can't access SD Card!").open()
        #         sdpath = '/storage'
            
        #     if '/storage' not in sdpath:
        #         sdpath = '/storage'

            
        #     self.link = sdpath
        
        global isOpenFM
        isOpenFM = 'True'
        self.file_manager_open()

    def storage_bottom_sheet_android(self, *args):
        #toolbar = MDToolbar(title="This is a toolbar")
        bottom_sheet_menu = MDListBottomSheet()
        bottom_sheet_menu.add_item("Internal Storage", lambda x: self.storageLink('/storage/emulated/0'), icon='cellphone-android')        
        bottom_sheet_menu.add_item("SD Card", lambda x: self.storageLink('/storage'), icon='micro-sd')                
        bottom_sheet_menu.open()
    
    # def storage_bottom_sheet_linux(self, *args):
    #     #toolbar = MDToolbar(title="This is a toolbar")
    #     bottom_sheet_menu = MDListBottomSheet()
    #     bottom_sheet_menu.add_item("Internal Storage", lambda x: self.storageLink('/'), icon='numeric-1-circle')        
    #     bottom_sheet_menu.add_item("SD Card", lambda x: self.storageLink('memcard'), icon='numeric-2-circle')                
    #     bottom_sheet_menu.open()

    def file_man(self, *args):
        if platform == 'android':
            self.storage_bottom_sheet_android()
            #self.link = '/storage/emulated/0'
        elif platform == 'linux':
            self.link = '/home'
            #self.storage_bottom_sheet_linux()
        elif platform == 'win':
            self.link = 'c://'
        
        self.file_manager_open()

    def file_manager_open(self, *args):
        global isOpenFM, file_manager
        isOpenFM = True
        file_manager.show(self.link)  # output manager to the screen
    
    def select_path(self, path):
        self.exit_manager()
        #self.fpath = path
        self.files.append(path)
        global isOpenFM
        isOpenFM = False
        toast("Selected file " + self.files[len(self.files) - 1])


        img = '''
OneLineAvatarListItem:
    id: aaa
    text: "Single-line item with avatar"

    ImageLeftWidget:
        id: two
        source: "logo.png"
     
'''

        img = Builder.load_string(img)
        img.text = self.files[len(self.files) - 1]
        img.ids.two.source = self.files[len(self.files) - 1]
        self.ids.img_list.add_widget(img)

    def exit_manager(self, *args):
        global file_manager
        file_manager.close()
    
    def post(self, *args):
        global localID, userdata

        def snk(*args):
                Snackbar(text = "Posting...").open()

        #Clock.schedule_once(snk, 2.5)
        #threading.Thread(target = Snackbar(text="Posting...").open())
        #def go(self, *args):
        global localID, userdata, ts
        if len(self.ids.post_txt.text) < 2048 or len(self.ids.post_txt.text) == 0:
            from screens import fbconfig
            import pyrebase
            ts = str(time.time()).replace('.', '-')
            firebaseConfig = fbconfig.posts_firebaseConfig
            firebase = pyrebase.initialize_app(firebaseConfig)
            storage = firebase.storage()
            db = firebase.database()
            
            
            data = {
                'fullname': userdata['fullname'],
                'pic': userdata['pic']
            }
            db.child(localID).update(data)
            
            
            data = {
                'text': self.ids.post_txt.text
            }
            db.child(localID).child(ts).update(data)
                    
            
            files_url_dict = {}
            
            for i, file in enumerate(self.files):
                fname = file.split('.')
                db_file_location = "posts/" + localID + "/" + ts + "/" + str(i) + '.' + fname[len(fname) - 1]
                storage.child(db_file_location).put(file)
                furl = storage.child(db_file_location).get_url(None)
                # files[i] = url
                files_url_dict[i] = furl
            
            #print(files_url_dict)
            db.child(localID).child(ts).update({'approval' : 'waiting'})
            db.child(localID).child(ts).update({'socialLink' : 'not available'})
            db.child(localID).child(ts).child('files').update(files_url_dict)

            # post = {
            #     'text' : self.ids.post_txt.text,
            #     'files' : files_url_dict
            #     }

            posts = db.child("posts").get()
            length = len(posts.val())
            print(posts, length)

            data = {str(length): localID + ", " + ts}
            db.child('posts').update(data)
            
            firebaseConfig = fbconfig.users_firebaseConfig
            firebase = pyrebase.initialize_app(firebaseConfig)
            db = firebase.database()
            

            self.files = []
            #toast("Post will be judged by moderators.")
            if userdata['points'] == 0:
                userdata['points'] += 30
                toast("You've got 30 points for first post!")
            else:
                userdata['points'] += 0
                toast("Points will be given after moderation!")
            
            db.child('users').child(localID).update({'points' : userdata['points']})
            
            userdata = db.child('users/' + localID).get()
            userdata = userdata.val()
            print(userdata)
            
            self.manager.current = 'social'

        else:
            Snackbar(text="No more than 2048 character!").open()
        #threading.Thread(target=go, args=self).start()
    
    def on_pre_leave(self, *args):
        self.files = []
        # for child in self.ids.img_list:
        # self.remove_widget(self.ids.img_list)


class NasaCornerScreen(Screen):
    def on_enter(self, *args):
        global screensArr
        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)

class NDVScreen(Screen):
    def changeScr(self, *args):
        self.manager.current = 'img'

    def butt_ac(self, *args):
        global imggalData
        if imggalData['media_type'] == 'image':
            self.manager.current = 'img'
            #import webbrowser
            #webbrowser.open(self.link, new=2)
        else:
            import webbrowser
            webbrowser.open(self.link, new=2)


    def on_pre_enter(self, *args):
        global img_gal, img_link, imggalData

        self.spinner = MDSpinner(
            size_hint=(None, None),
            size=(46, 46),
            pos_hint={'center_x': 1, 'center_y': .5},
            active=True,
        )

        self.ids.scroll_grid.add_widget(self.spinner)

        

        if img_gal == 'apod':
            #self.data = imggalData
            #data = {'media_type' : 'video'}
            print(imggalData)
            self.ids.title.text = imggalData['title']
            self.ids.explanation.text = imggalData['explanation']
            self.link = imggalData['url']

            if imggalData['media_type'] == 'image':
                #self.ids.img.source = self.link
                #import requests

                
                self.ids.button.text = 'View Image'
                self.ids.button.on_press = self.changeScr
                
            elif imggalData['media_type'] == 'video':
                self.ids.button.text = 'Watch Video'


    def on_enter(self, *args):
        self.ids.scroll_grid.remove_widget(self.spinner)

        global screensArr
        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)

                

			# 	
			# 	text: 10*"d awoifhaisfia9 hd
            # fiaw fioahdf9hawcoe rfiehs9f hasdfhaiwe8 wte87tawe8fPython | Scrollview widget in kivyLast Updated: 06-02-2020Kivy is a platform-independent GUI tool in Python. As it can be run on Android, IOS, Linux, and Windows, etc. It is basically used to develop the Android application, but it does not mean that it can not be used on Desktop applications.👉🏽 Kivy Tutorial – Learn Kivy with Examples.Scroll view:The ScrollView widget provides a scrollable/pannable viewport that is clipped at the scrollview’s bounding box.Scroll view accepts only one child and applies a window to it according to 2 properties:1) scroll_x2) scrool_yTo determine if interaction is a scrolling gesture, these properties are used:Python | Scrollview widget in kivyLast Updated: 06-02-2020Kivy is a platform-independent GUI tool in Python. As it can be run on Android, IOS, Linux, and Windows, etc. It is basically used to develop the Android application, but it does not mean that it can not be used on Desktop applications.👉🏽 Kivy Tutorial – Learn Kivy with Examples.Scroll view:The ScrollView widget provides a scrollable/pannable viewport that is clipped at the scrollview’s bounding box.Scroll view accepts only one child and applies a window to it according to 2 properties:1) scroll_x2) scrool_yTo determine if interaction is a scrolling gesture, these properties are used:Python | Scrollview widget in kivyLast Updated: 06-02-2020Kivy is a platform-independent GUI tool in Python. As it can be run on Android, IOS, Linux, and Windows, etc. It is basically used to develop the Android application, but it does not mean that it can not be used on Desktop applications.👉🏽 Kivy Tutorial – Learn Kivy with Examples.Scroll view:The ScrollView widget provides a scrollable/pannable viewport that is clipped at the scrollview’s bounding box.Scroll view accepts only one child and applies a window to it according to 2 properties:1) scroll_x2) scrool_yTo determine if interaction is a scrolling gesture, these properties are used:"
			# 	#text_size: self.width, None
			# 	height: self.texture_size[1]
        
class ImgScreen(Screen):

    def on_pre_enter(self, *args):
        global img_link
        self.ids.img.source = img_link

    def on_enter(self, *args):
        global screensArr
        screensArr.append(self.manager.current)
        print(self.manager.current, screensArr)
    
class SocialShare(Screen):
    
    def postLink(self, *args):
        import pyrebase
        from screens import fbconfig
        if self.ids.link.text != '':
            try:
                firebaseConfig = fbconfig.posts_firebaseConfig
                firebase = pyrebase.initialize_app(firebaseConfig)
                db = firebase.database()
                db.child(localID).child(ts).update({'socialLink' : self.ids.link.text})
                toast(text = "Got the link. Moderators will judge your social share.")
            except:
                Snackbar(text="No internet connection or something is wrong!").open()
        else:
            Snackbar(text="No link inputted!").open()



sm = ScreenManager()
sm.add_widget(SplashScreen(name='splash'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(SignupScreen(name='signup'))
sm.add_widget(InputScreen(name='input'))
sm.add_widget(LoadingScreen(name='load'))
sm.add_widget(DataScreen(name='data'))
sm.add_widget(MapScreen(name='map'))
sm.add_widget(ContribScreen(name='contrib'))
sm.add_widget(VideoScreen(name='video'))
sm.add_widget(RoboScreen(name='robo'))
sm.add_widget(NasaScreen(name='nasa'))
sm.add_widget(NDataScreen(name='ndata'))
sm.add_widget(GraphScreen(name='graph'))
sm.add_widget(SuggestionScreen(name='sugg'))
sm.add_widget(PostScreen(name='post'))
sm.add_widget(NasaCornerScreen(name='nasac'))
sm.add_widget(NDVScreen(name='ndv'))
sm.add_widget(ImgScreen(name='img'))
sm.add_widget(SocialShare(name='social'))

def delScr(*args):
    global screensArr
    #screensArr.pop()
    del screensArr[-1]
    print("delscr", screensArr)

# verify / check last array item if ''

class Nasa2020(MDApp):

    def on_start(self):
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        #global loading
        #loading = 'data'
        #self.screen.current = 'post'
        from shutil import rmtree
        
        
        folders = ['graphs', 'cache', 'files']

        for name in folders:
            try:
                rmtree(name)
            except:
                pass

        for name in folders:
            try:
                os.mkdir(name)
            except:
                pass


    def build(self):
        self.screen = Builder.load_string(screen_manager)

        return self.screen

    def changeScreen(self, scrname, *args):
        if scrname != 'load':
            global screensArr
            if screensArr[len(screensArr) - 2] == scrname:
                #screensArr.pop()
                del screensArr[-1]
                i = len(screensArr) - 1
                while screensArr[i] == '':
                    i -= 1
                self.screen.current = screensArr[i]
            else:
                screensArr.append(scrname)
                self.screen.current = screensArr[len(screensArr) - 1]
        elif scrname == 'load':
            self.screen.current = 'load'


    def hook_keyboard(self, window, key, *args):
        global screensArr, delScr, isOpenFM
        if key == 27:
            # for i in range(0, len(screensArr)):
            #     if screensArr[i] == 'load':
            #         screensArr.pop(i)

            print("before esc", screensArr)
            # print(self.screen.current)
            # if self.screen.current == 'splash':
            #     self.get_running_app().stop()
            # elif self.screen.current == 'input':
            #     self.screen.current = 'splash'
            # elif self.screen.current == 'load':
            #     self.screen.current = 'input'
            # elif self.screen.current == 'data':
            #     self.screen.current = 'input'
            # elif self.screen.current == 'map':
            #     self.screen.current = 'data'
            # elif self.screen.current == 'contrib':
            #     self.screen.current = 'data'
            # elif self.screen.current == 'video':
            #     self.current_video_state = 'stop'
            #     self.screen.current = 'data'
            # elif self.screen.current == 'robo':
            #     self.screen.current = 'data'
            # elif self.screen.current == 'contrib':
            #     self.screen.current = 'data'
            # elif self.screen.current == 'sugg':
            #     self.screen.current = 'data'
            # elif self.screen.current == 'ndata' or self.screen.current == 'nasa':
            #     self.screen.current = 'data'
            if isOpenFM == True:
                global file_manager
                file_manager.back()
            elif self.screen.current == 'signup':
                i = len(screensArr) - 1
                while screensArr[i] == '':
                    i -= 1
                self.screen.current = screensArr[i]
                
            else:
                if screensArr[len(screensArr) - 1] == screensArr[len(screensArr) - 2]:
                    delScr()
                    delScr()
                else:
                    delScr()

                if len(screensArr) > 1:
                    i = len(screensArr) - 1
                    if screensArr[i] == '':
                        screensArr.pop(i)
                        print(screensArr)
                    self.screen.current = screensArr[len(screensArr) - 1]
                else:
                    self.get_running_app().stop()
            print("after pressing esc", screensArr)


    def delScrapp(self, *args):
        global screensArr
        #screensArr.pop()
        del screensArr[-1]

    def callback(self, instance):
        if instance.icon == 'map-marker':
            self.screen.current = 'map'
        elif instance.icon == 'image-plus' or instance.icon == 'image-box-multiple-outline':
            self.screen.current = 'post'

    def get_date(self, date, *args):
        print(date)
        print(type(date))

    def show_date_picker(self, *args):
        date_dialog = MDDatePicker(
            callback=self.get_date,
            year=2010,
            month=2,
            day=12,
        )
        date_dialog.open()
    
    def openLink(self, str, *args):
        #time.sleep(3)
        import webbrowser
        webbrowser.open(str, new=2)
        #print("Browser")

    def imgGal(self, str, *args):
        global img_gal, loading
        img_gal = str
        loading = 'ndv'
        self.screen.current = 'load'

    def imageGallery_show_list_bottom_sheet(self, *args):
        #toolbar = MDToolbar(title="This is a toolbar")
        bottom_sheet_menu = MDListBottomSheet()
        bottom_sheet_menu.add_item("Astronomy Picture of the Day (APOD)", lambda x: self.imgGal('apod'), icon='numeric-1-circle')        
        bottom_sheet_menu.open()

    def logout(self, *args):
        try:
            os.remove('helper.tn')
        except:
            pass
        global screensArr, isLoggedIn
        screensArr = []
        isLoggedIn = 0
        self.screen.current = 'login'

Nasa2020().run()
