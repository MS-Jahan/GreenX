# this file was merged with main.py file

from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.picker import MDDatePicker
import random
from kivy.clock import Clock
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.label import MDLabel
import requests
import json

class NasaScreen(Screen):

    self.ids.fromd.text = "2016-01-01"
    self.ids.to.text = "2016-12-31"

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
        self.ele_menu.dismiss()

    def per_set_item(self, instance_menu, instance_menu_item):
        self.ids.per_drop_item.set_item(instance_menu_item.text)
        global per_data
        per_data = instance_menu_item.text
        self.per_menu.dismiss()

    def fetchData(self, *args):
        global lat, lon

        spinner = MDSpinner(
            size_hint=(None, None),
            size=(46, 46),
            pos_hint={'center_x': .5, 'center_y': .2},
            active=True,
            id=spin
        )

        self.add_widget(spinner)

        label = MDLabel(
            pos_hint={'center_y': 0.1},
            text="This may take a while",
            halign="center",
            id=splabel
        )
        self.add_widget(label)

        def graphPlot(category, parameter):
            cat = ''
            para = ''
            if category == 'Interannual':
                cat = "INTERANNUAL"
            else:
                cat = "DAILY"
            
            if parameter == 'T2M_RANGE':
                para = 'Temperature (C)'
            elif parameter == 'RH2M':
                para = 'Moisture(%)'
            else:
                para = 'Wind Speed (m/s)'

            url = "https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?&request=execute&identifier=SinglePoint&parameters=" + parameter + "&startDate=" + self.ids.fromd.text[:4] + "&endDate=" + self.ids.to.text[:4] +"&userCommunity=AG&tempAverage=" + cat + "&outputList=JSON&lat=" + lat + "&" + "lon=" + lon
            try:
                response = requests.get(url)
                print(response)
                data = response.json()

                data = data['features'][0]['properties']['parameter']['T2M_RANGE']

                dates = []
                values = []

                for key, value in data.items():
                        if key[-2:] != '13' and value >= 0:
                                dates.append(key)
                                values.append(value)
                                print(key + " " + str(value))

                import matplotlib.pyplot as plt

                plt.figure(figsize=(40,20))        
                plt.plot(dates, values)
                plt.title(para + ' Vs Year')
                plt.xlabel('Year')
                plt.ylabel(para)

                plt.savefig('graph.png', bbox_inches='tight')
                self.remove_widget(self.ids.spinner)
                self.remove_widget(self.ids.splabel)

                self.manager.current = 'ndata'
                
            except:
                print("Error")
                self.manager.current = "nasa"
                Snackbar(text="Can't get data from Nasa!").show()

        
            if self.ids.ele_drop_item.text == 'Temperature':
                graphPlot(self.ids.per_drop_item.text, 'T2M_RANGE')
            elif self.ids.ele_drop_item.text == 'Moisture':
                graphPlot(self.ids.per_drop_item.text, 'RH2M')
            elif self.ids.ele_drop_item.text == 'Wind':
                graphPlot(self.ids.per_drop_item.text, 'WS2M')
            else:
                Snackbar(text="Select Search Topic and Period first!").show()
            
            


        
