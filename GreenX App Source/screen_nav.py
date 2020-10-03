screen_manager = """
#:import MapView kivy_garden.mapview.MapView
#:import MapMarker kivy_garden.mapview.MapMarker


ScreenManager:
    SplashScreen:
	LoginScreen:
	SignupScreen:
	InputScreen:
	LoadingScreen:
	DataScreen:
	MapScreen:
	ContribScreen:
	#VideoShowcase:
	VideoScreen:
	RoboScreen:
	NasaScreen:
	NDataScreen:
	GraphScreen:
	SuggestionScreen:
	PostScreen:
	NasaCornerScreen:
	NDVScreen:
	ImgScreen:
	SocialShare:

<SplashScreen>:
    name: 'splash'
    MDFloatLayout:
		#md_bg_color: 0, 6/255, 26/255, 1

		Image:
            source: 'space.jpg'
			pos_hint: {'center_x': 0.5, 'center_y':0.5}
			allow_stretch: True
			size_hint_y: 3
			size_hint_x: 4


        Image:
            source: 'logo.png'
			pos_hint: {'center_x': 0.5, 'center_y':0.6}

		MDLabel:
			text: "Plant Green, Sustain Future"
			halign: "center"
			pos_hint: {'center_x': 0.5, 'center_y':0.3}
			theme_text_color: "Custom"
    		text_color: 1, 1, 1, 1
			font_style: "H5"

        # MDFlatButton:
        #     text: 'Continue'
        #     #font_name: 'font/SutonnyMJ'
        #     text_color: 77/255, 166/255, 255/255, 1
        #     pos_hint: {'center_x': 0.5, 'center_y':0.1}
        #     on_press: root.manager.current = 'login'
		
		MDRaisedButton:
			text: "Continue"
			pos_hint: {'center_x': 0.5, 'center_y':0.1}
			#md_bg_color: 0, 179/255, 0, 1
			on_press: root.manager.current = 'login'

<SignupScreen>:
	name: 'signup'
	MDLabel:
		text: "Fill in to sign up"
		halign: "center"
		pos_hint: {'center_x': 0.5, 'center_y': 0.9}
	
	MDTextField:
		id: flname
		hint_text: "Full Name"
		pos_hint: {"center_x": .5, "center_y": 0.8}
		size_hint: 0.7, None
		helper_text_mode: "on_focus"
		icon_right: "account"
	
	MDTextField:
		id: date
		hint_text: "Date of Birth"
		pos_hint: {"center_x": .5, "center_y": 0.7}
		size_hint: 0.7, None
		helper_text: "Tap the calender icon on the right"
		helper_text_mode: "on_focus"
		#icon_right: "calendar"
		#on_icon_right: app.show_date_picker()
	
    MDIconButton:
        icon: "calendar"
        pos_hint: {"center_x": 0.8, "center_y": .7}
		on_press: root.show_date_picker()
	
	MDTextField:
		id: gender
		hint_text: "Gender"
		pos_hint: {"center_x": .5, "center_y": 0.6}
		size_hint: 0.7, None
		helper_text_mode: "on_focus"
		icon_right: "email"
		on_focus: if self.focus: root.menu.open()

	MDTextField:
		id: email
		hint_text: "Email"
		pos_hint: {"center_x": .5, "center_y": 0.5}
		size_hint: 0.7, None
		helper_text_mode: "on_focus"
		icon_right: "email"
	
	MDTextField:
		id: passw
		hint_text: "Password"
		pos_hint: {"center_x": .5, "center_y": 0.4}
		password: True
		size_hint: 0.7, None
		helper_text_mode: "on_focus"
		icon_right: "lock"
	
	MDTextField:
		id: conf_pass
		hint_text: "Confirm Password"
		pos_hint: {"center_x": .5, "center_y": 0.3}
		password: True
		size_hint: 0.7, None
		helper_text_mode: "on_focus"
		icon_right: "lock-alert"
	
	MDRaisedButton:
		text: "Sign Up"
		pos_hint: {"center_x": .5, "center_y": 0.2}
		md_bg_color: 0, 179/255, 0, 1
		on_press: root.signup()

<LoginScreen>:
	name: 'login'
	padding: 20
	MDTextField:
		id: email
		hint_text: "Email"
		pos_hint: {"center_x": .5, "center_y": 0.6}
		size_hint: 0.7, None
		helper_text_mode: "on_focus"
	MDTextField:
		id: password
		hint_text: "Password"
		pos_hint: {"center_x": .5, "center_y": 0.5}
		password: True
		size_hint: 0.7, None
		helper_text_mode: "on_focus"
	MDRaisedButton:
		text: "Login"
		pos_hint: {"center_x": .5, "center_y": 0.4}
		md_bg_color: 0, 179/255, 0, 1
		on_release: root.login()
	MDTextButton:
		pos_hint: {"center_y": 0.3}
		text: "  Don't have an account? Sign up."
		custom_color: 128/255, 128/255, 128/255, 1
		on_press: root.manager.current = 'signup'
	MDTextButton:
		pos_hint: {"center_y": 0.25}
		text: "  Forgot Password"
		custom_color: 128/255, 128/255, 128/255, 1
		on_press: root.forgot()

<InputScreen>:
	name: 'input'
	NavigationLayout:
        ScreenManager:
            Screen:
				GridLayout:
					cols: 1
					#rows: 3
					#orientation: 'horizontal'
					#size_hint_y: None
					height: self.minimum_height
					#padding: 10
					#halign: 'center'
					#spacing: 40
					#BoxLayout
					MDToolbar:
						id: data_viewer_title
						title: "DataSet"
						left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
						mode: 'end'
						type: 'top'
						icon: "language-python"
						#on_action_button: app.navigation_draw()
				
				MDLabel:
					text: "Type location to get started:"
					halign: "center"
					#font_style: Secondary
				
				MDTextField:
					id: location_input 
					hint_text: "Location"
					pos_hint: {"center_x": .5, "center_y": 0.4}
					size_hint_x: 0.5
					size_hint_y: 0.1
					#width: 0.7
					#helper_text: ""
					helper_text_mode: "on_focus"
				
				MDIconButton:
					icon: "arrow-right-bold-circle-outline"
					pos_hint: {"center_x": .85, "center_y": .4}
					on_release:
						root.go()

				MDNavigationDrawer:
                    id: nav_drawer
                    BoxLayout:
                        #adaptive_size: True
                        #size_hint_y: 0.9
                        orientation: "vertical"
                        #spacing: '2dp'
                        #padding: '2dp'
						MDIconButton:
                            icon: "close"
                            pos_hint: {"center_x": 0.1, "center_y": 1.0}
                            user_font_size: "24sp"
                            on_release: nav_drawer.set_state("close")
                        Image:
                            source: "pro-icon.png"
                            #size: 10, 10
                            size_hint_y: 0.7
                        MDLabel:
							id: username_nav
                            text: "  User Name"
                            font_style: "Subtitle1"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
							id: rank_nav
                            text: "   Rank: Newbie"
                            font_style: "Caption"
							theme_text_color: "Hint"
                            size_hint_y: None
                            height: self.texture_size[1]
						MDLabel:
							id: point_nav
                            text: "   1200 Points"
							font_style: "Caption"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
    
                        ScrollView:
                            #spacing: '-10dp'
                            #padding: '-10dp'
                            #halign: 'left'
                            MDList:
                                #pos: self.x - 10, self.y - 10
                                OneLineIconListItem:
                                    text: 'Homepage'
                                    font_style: 'Body2'
                                    on_release: root.manager.current = 'input'
                                        
                                    IconLeftWidget:
                                        icon: 'home'
										
                                OneLineIconListItem:
                                    text: 'Profile'
                                    font_style: 'Body2'
                                    on_release:
                                        from kivymd.toast import toast
										toast("Not available right now.")
                                        nav_drawer.set_state("close")
                                        
                                    IconLeftWidget:
                                        icon: 'account-settings'
								
								OneLineIconListItem:
                                    text: 'Contributions'
                                    font_style: 'Body2'
                                    on_release:
										from kivymd.toast import toast
										toast("Not available right now.")
                                    IconLeftWidget:
                                        icon: 'earth-plus'
								
								OneLineIconListItem:
                                    text: 'Realtime bot data'
                                    font_style: 'Body2'
                                    on_release: 
										from kivymd.toast import toast
										toast("Real data available on robo app.")
										root.manager.current = 'robo'
                                    IconLeftWidget:
                                        icon: 'robot'

								OneLineIconListItem:
                                    text: 'Our Mission (Video)'
                                    font_style: 'Body2'
                                    on_release: root.manager.current = 'video'
                                    IconLeftWidget:
                                        icon: 'video'
										
                                OneLineIconListItem:
                                    text: 'Leaderboard'
                                    font_style: 'Body2'
                                    on_release:
                                        from kivymd.toast import toast
										toast("Not available right now.")
                                        
                                    IconLeftWidget:
                                        icon: 'playlist-star'
								
								OneLineIconListItem:
                                    text: 'Nasa Corner'
                                    font_style: 'Body2'
                                    on_release:
                                        root.manager.current = 'nasac'
                                    IconLeftWidget:
                                        icon: 'satellite-uplink'
								
								OneLineIconListItem:
                                    text: 'Image Gallery'
                                    font_style: 'Body2'
                                    on_release:
                                        app.imageGallery_show_list_bottom_sheet()
                                    IconLeftWidget:
                                        icon: 'tooltip-image-outline'
								
								OneLineIconListItem:
                                    text: 'Farmer Corner'
                                    font_style: 'Body2'
                                    on_release:
                                        from kivymd.toast import toast
										toast("Feature will be added in future!")
									IconLeftWidget:
                                        icon: 'tractor-variant'
								
								OneLineIconListItem:
                                    text: 'Specialist Corner'
                                    font_style: 'Body2'
                                    on_release:
                                        from kivymd.toast import toast
										toast("Feature will be added in future!")
									IconLeftWidget:
                                        icon: 'lightbulb'
										
                                OneLineIconListItem:
                                    text: 'Settings'
                                    font_style: 'Body2'
                                    on_release:
										from kivymd.toast import toast
										toast("Will be available soon.")                                      
                                    IconLeftWidget:
                                        icon: 'youtube-studio'
										
                                OneLineIconListItem:
                                    text: 'About'
                                    font_style: 'Body2'
                                    on_release:
                                        from kivymd.toast import toast
										toast("Made with love by Team OrionVI")
                                    IconLeftWidget:
                                        icon: 'human-handsdown'
									
								OneLineIconListItem:
                                    text: 'Logout'
                                    font_style: 'Body2'
                                    on_release:
                                        app.logout()
										from kivymd.toast import toast
										toast("Logged out")
                                    IconLeftWidget:
                                        icon: 'logout'
					
				MDFloatingActionButtonSpeedDial:
					id: float_button
					#data: root.data
					rotation_root_button: True
					callback: app.callback
					#hint_animation: True
					bg_hint_color: app.theme_cls.primary_light

					custom_color: 255/255, 153/255, 0, 0.8


				
<LoadingScreen>:
	name: 'load'
	MDSpinner:
		id: spinner
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .5, 'center_y': .5}
        active: True
	MDLabel:
		id: msg
		text: "Loading..."
		halign: 'center'
		pos_hint: {'center_x': .5, 'center_y': .4}

<DataScreen>:
	name: 'data'
	NavigationLayout:
        ScreenManager:
            Screen:
				GridLayout:
					cols: 1
					#rows: 3
					#orientation: 'horizontal'
					#size_hint_y: None
					#height: self.minimum_height
					#padding: 10
					#halign: 'center'
					spacing: 5
					#BoxLayout
					MDToolbar:
						id: data_viewer_title
						title: "DataSet"
						left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
						mode: 'end'
						type: 'top'
						icon: "language-python"
						#on_action_button: app.navigation_draw()
					BoxLayout:
						orientation: 'vertical'
						MDLabel:
							halign: 'center'
							text: "Environment Data For"
							pos_hint: {"center_x": .5, "center_y": 1}
							#size_hint: 1, None
							font_style: 'H6'
							#size_hint_y: None
							#height: 50
							
						MDLabel:
							id: data_scr_header
							halign: 'center'
							text: "Location"
							pos_hint: {"center_x": .5, "center_y": 0.9}
							#size_hint: 10, None
							font_style: 'H4'
							#size_hint_y: None
							#height: 10
					
						# ScrollView:
						# 	height: 1000
						# 	pos_hint: {"center_x": .5, "center_y": 1}
						# GridLayout:
						# 	rows: 2
						# 	cols: 1
						# 	orientation: 'vertical'
						# 	MDList:
						BoxLayout:
							size_hint_y: None
							height: 400
							spacing: 10
							padding: 10
							MDCard:
								#adaptive_height: True
								orientation: "vertical"
								padding: "8dp"
								size_hint: 0.5, 0.5
								#size: "230dp", "130dp"
								pos_hint: {"center_x": .4, "center_y": .8}
								

								MDLabel:
									text: "Temperature"
									theme_text_color: "Secondary"
									size_hint_y: None
									height: self.texture_size[1]
									
								MDSeparator:
									height: "1dp"
									
								MDLabel:
									id: temp
									text: "45°"
									font_style: "H5"
									halign: "center"
							MDCard:
								orientation: "vertical"
								padding: "8dp"
								size_hint: 0.5, 0.5
								#size: "230dp", "130dp"
								pos_hint: {"center_x": .4, "center_y": .8}
								

								MDLabel:
									text: "Humidity"
									theme_text_color: "Secondary"
									size_hint_y: None
									height: self.texture_size[1]
									
								MDSeparator:
									height: "1dp"
									
								MDLabel:
									id: humid
									font_style: "H5"
									halign: "center"
									text: "45°"
							MDCard:
								orientation: "vertical"
								padding: "8dp"
								size_hint: 0.5, 0.5
								#size: "230dp", "130dp"
								pos_hint: {"center_x": .4, "center_y": .8}
								

								MDLabel:
									text: "Wind Speed"
									theme_text_color: "Secondary"
									size_hint_y: None
									height: self.texture_size[1]
									
								MDSeparator:
									height: "1dp"
								
								# MDLabel:
								# 	text: "(metric tons per capita)"
								# 	theme_text_color: "Hint"
								# 	font_style: "H5"
								# 	size_hint_y: None
								# 	height: self.texture_size[1]
									
								MDLabel:
									id: wind
									font_style: "H5"
									halign: "center"
									text: "45°"
						BoxLayout:
							size_hint_y: None
							pos_hint: {"center_x": .5, "center_y": 1}
							spacing: 10
							padding: 10
							height: 400
							MDCard:
								adaptive_height: True
								orientation: "vertical"
								padding: "8dp"
								size_hint: 0.5, 0.5
								#size: "230dp", "130dp"
								pos_hint: {"center_x": .5, "center_y": 1}
								

								MDLabel:
									text: "Weather"
									theme_text_color: "Secondary"
									size_hint_y: None
									height: self.texture_size[1]
									
								MDSeparator:
									height: "1dp"
									
								MDLabel:
									id: weather
									text: "16%"
									font_style: "H5"
									halign: "center"
							MDCard:
								orientation: "vertical"
								padding: "8dp"
								size_hint: 0.5, 0.5
								#size: "230dp", "130dp"
								pos_hint: {"center_x": .5, "center_y": 1}
								

								MDLabel:
									text: "Pressure"
									theme_text_color: "Secondary"
									size_hint_y: None
									height: self.texture_size[1]
									
								MDSeparator:
									height: "1dp"
									
								MDLabel:
									id: pressure
									font_style: "H5"
									halign: "center"
									text: "45°"
							MDCard:
								orientation: "vertical"
								padding: "8dp"
								size_hint: 0.5, 0.5
								#size: "230dp", "130dp"
								pos_hint: {"center_x": .5, "center_y": 1}
								

								MDLabel:
									text: "Country Code"
									theme_text_color: "Secondary"
									size_hint_y: None
									height: self.texture_size[1]
									
								MDSeparator:
									height: "1dp"
									
								MDLabel:
									id: country
									font_style: "H5"
									halign: "center"
									text: "45°"
						BoxLayout:
							pos_hint: {"center_x": 0.5, "center_y": 0.2}
							MDRoundFlatIconButton:
								id: nasab
								icon: "satellite-uplink"
								text: "Get Recommendation Using Data from NASA"
								pos_hint: {"center_x": 0.9, "center_y": 0.4}
								on_release: root.manager.current = 'nasa'
			
				MDNavigationDrawer:
                    id: nav_drawer
                    BoxLayout:
                        #adaptive_size: True
                        #size_hint_y: 0.9
                        orientation: "vertical"
                        #spacing: '2dp'
                        #padding: '2dp'
						MDIconButton:
                            icon: "close"
                            pos_hint: {"center_x": 0.1, "center_y": 1.0}
                            user_font_size: "24sp"
                            on_release: nav_drawer.set_state("close")
                        Image:
                            source: "pro-icon.png"
                            #size: 10, 10
                            size_hint_y: 0.7

                        MDLabel:
							id: username_nav
                            text: "  User Name"
                            font_style: "Subtitle1"
                            size_hint_y: None
                            height: self.texture_size[1]

                        MDLabel:
							id: rank_nav
                            text: "   Rank: Newbie"
                            font_style: "Caption"
							theme_text_color: "Hint"
                            size_hint_y: None
                            height: self.texture_size[1]
							
						MDLabel:
							id: point_nav
                            text: "   1200 Points"
							font_style: "Caption"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
    
                        ScrollView:
                            #spacing: '-10dp'
                            #padding: '-10dp'
                            #halign: 'left'
                            MDList:
                                #pos: self.x - 10, self.y - 10
                                OneLineIconListItem:
                                    text: 'Homepage'
                                    font_style: 'Body2'
                                    on_release: root.manager.current = 'input'
                                        
                                    IconLeftWidget:
                                        icon: 'home'
										
                                OneLineIconListItem:
                                    text: 'Profile'
                                    font_style: 'Body2'
                                    on_release:
                                        from kivymd.toast import toast
										toast("Not available right now.")
                                        nav_drawer.set_state("close")
                                        
                                    IconLeftWidget:
                                        icon: 'account-settings'
								
								OneLineIconListItem:
                                    text: 'Contributions'
                                    font_style: 'Body2'
                                    on_release:
										from kivymd.toast import toast
										toast("Not available right now.")
                                    IconLeftWidget:
                                        icon: 'earth-plus'
								
								OneLineIconListItem:
                                    text: 'Realtime bot data'
                                    font_style: 'Body2'
                                    on_release: 
										from kivymd.toast import toast
										toast("Real data available on robo app.")
										root.manager.current = 'robo'
                                    IconLeftWidget:
                                        icon: 'robot'

								OneLineIconListItem:
                                    text: 'Our Mission (Video)'
                                    font_style: 'Body2'
                                    on_release: root.manager.current = 'video'
                                    IconLeftWidget:
                                        icon: 'video'
										
                                OneLineIconListItem:
                                    text: 'Leaderboard'
                                    font_style: 'Body2'
                                    on_release:
                                        from kivymd.toast import toast
										toast("Not available right now.")
                                        
                                    IconLeftWidget:
                                        icon: 'playlist-star'
								
								OneLineIconListItem:
                                    text: 'Nasa Corner'
                                    font_style: 'Body2'
                                    on_release:
                                        root.manager.current = 'nasac'
                                    IconLeftWidget:
                                        icon: 'satellite-uplink'
								
								OneLineIconListItem:
                                    text: 'Image Gallery'
                                    font_style: 'Body2'
                                    on_release:
                                        app.imageGallery_show_list_bottom_sheet()
                                    IconLeftWidget:
                                        icon: 'tooltip-image-outline'

								OneLineIconListItem:
                                    text: 'Farmer Corner'
                                    font_style: 'Body2'
                                    on_release:
                                        from kivymd.toast import toast
										toast("Feature will be added in future!")
									IconLeftWidget:
                                        icon: 'tractor-variant'
								
								OneLineIconListItem:
                                    text: 'Specialist Corner'
                                    font_style: 'Body2'
                                    on_release:
                                        from kivymd.toast import toast
										toast("Feature will be added in future!")
									IconLeftWidget:
                                        icon: 'lightbulb'

                                OneLineIconListItem:
                                    text: 'Settings'
                                    font_style: 'Body2'
                                    on_release:
										from kivymd.toast import toast
										toast("Will be available soon.")                                      
                                    IconLeftWidget:
                                        icon: 'youtube-studio'
										
                                OneLineIconListItem:
                                    text: 'About'
                                    font_style: 'Body2'
                                    on_release:
                                        from kivymd.toast import toast
										toast("Made with love by Team OrionVI")
                                    IconLeftWidget:
                                        icon: 'human-handsdown'
								
								OneLineIconListItem:
                                    text: 'Logout'
                                    font_style: 'Body2'
                                    on_release:
                                        app.logout()
										from kivymd.toast import toast
										toast("Logged out")
                                    IconLeftWidget:
                                        icon: 'logout'
					
				MDFloatingActionButtonSpeedDial:
					id: ddata
					#data: root.data
					rotation_root_button: True
					callback: app.callback
					#hint_animation: True
					bg_hint_color: app.theme_cls.primary_light

					custom_color: 255/255, 153/255, 0, 0.8


<MapScreen>:
	name: 'map'
	MapView:
		zoom: 2
		id: mapv
		
		double_tap_zoom: True
		
		MapMarkerPopup:
			id: mapv_pop
			source: 'marker.png'


<ContribScreen>:
    name: 'contrib'
	GridLayout:
		cols: 1
		#rows: 3
		#orientation: 'horizontal'
		#size_hint_y: None
		height: self.minimum_height
		MDToolbar:
			id: data_viewer_title
			title: "Your Contibutions"
			left_action_items: [["arrow-left", lambda x: app.changeScreen('data')]]
			mode: 'end'
			type: 'top'
			icon: "language-python"
			#on_action_button: app.navigation_draw()
		ScrollView:
			MDList:
				TwoLineIconListItem:
					text: "You planted a tree."
					secondary_text: "Wednesday, 2 Sep 2020 | 5:08 pm"
					font_style: 'Body2'
									
					IconLeftWidget:
						icon: 'tree'
						
				TwoLineIconListItem:
					text: "You took part in Environment Awareness Seminar."
					secondary_text: "Wednesday, 1 Aug 2020 | 3:00 pm"
					font_style: 'Body2'

					IconLeftWidget:
						icon: 'nature-people'


<VideoScreen>:
	name: 'video'
	VideoPlayer:
		id: vid
    	source: 'https://www.dropbox.com/s/yxpoudg7rcjtm0i/Environmental%20Protection%20Animation.mp4?dl=1'
		allow_stretch: True

<RoboScreen>:
	name: 'robo'
	MDBoxLayout:
		padding: 20
		md_bg_color: 0, 0, 0, 1
		MDLabel:
			pos_hint: {"center_y": 0.9}
			id: roboterm
			theme_text_color: "Custom"
    		text_color: 1, 1, 1, 1

<NasaScreen>:
	name: 'nasa'
	
	MDLabel:
		pos_hint: {"center_y": 0.9}
		halign: 'center'
		text: "Fetch Data"
		font_style: "H3"

	MDLabel:
		pos_hint: {'center_x': .6, "center_y": 0.8}
		text: "Search Topic"
	
	MDDropDownItem:
        id: ele_drop_item
        pos_hint: {'center_x': .7, 'center_y': .8}
        text: 'Select'
        on_release: root.ele_menu.open()
	
	MDLabel:
		pos_hint: {'center_x': .6, "center_y": .7}
		text: "Period"
	
	MDDropDownItem:
        id: per_drop_item
        pos_hint: {'center_x': .7, 'center_y': .7}
        text: 'Select'
        on_release: root.per_menu.open()
	
	MDLabel:
		pos_hint: {'center_x': .6, "center_y": .6}
		text: "Date Range"
	
	MDTextField:
		id: fromd
		hint_text: "From"
		pos_hint: {"center_x": .5, "center_y": .6}
		size_hint: 0.2, None
		helper_text_mode: "on_focus"

	MDIconButton:
        icon: "calendar"
        pos_hint: {"center_x": 0.7, "center_y": .6}
		on_press: root.from_show_date_picker()
	
	MDTextField:
		id: to
		hint_text: "To"
		pos_hint: {"center_x": .5, "center_y": .5}
		size_hint: 0.2, None
		helper_text_mode: "on_focus"

	MDIconButton:
        icon: "calendar"
        pos_hint: {"center_x": 0.7, "center_y": .5}
		on_press: root.to_show_date_picker()
	
	MDFloatingActionButton:
		icon: "send"
		md_bg_color: app.theme_cls.primary_color
		on_press: root.fetchData()
		pos_hint: {'center_x': .9, 'center_y': .1}


<NDataScreen>:
	name: 'ndata'
	FloatLayout:
		MDLabel:
			text: "Graph"
			halign: "center"
			pos_hint: {'center_x': 0.3, 'center_y': 0.9}
		Button:
			id: graph_img
			pos_hint: {'center_x': 0.3, 'center_y': 0.7}
			size_hint: 0.5, 0.3
			on_press: root.manager.current = 'graph'


<GraphScreen>:
	name: 'graph'
	BoxLayout:
        #size_hint_y: 0.8
        #orientation: 'vertical'
        adaptive_size: True
        id: box
        Scatter:
            id: scatter_box
            scale_min: .5
            scale_max: 8
            size: box.size
            pos: box.pos
            #scale: 5
            pos: img_viewer.pos
            do_rotation: False
            Image :
                id: img_viewer
                size: box.width, box.height
                #size: (500, 500/self.image_ratio)  
                #pos: 1, 1
                allow_stretch: True
                keep_ratio: True
    
    #BoxLayout:
        #size_hint_y: 0.2
    MDIconButton:
        icon: "backburger"
        user_font_size: "24sp"
        on_release: root.manager.current = 'nasa'
        pos_hint: {'center_x': 0.1, 'center_y': 0.95}

<SuggestionScreen>:
	name: 'sugg'
	GridLayout:
		cols: 1
		#rows: 3
		#orientation: 'horizontal'
		#size_hint_y: None
		height: self.minimum_height
		MDToolbar:
			
			title: "Suggestions and Caution"
			left_action_items: [["arrow-left", lambda x: app.changeScreen('data')]]
			mode: 'end'
			type: 'top'
			icon: "language-python"
			#on_action_button: app.navigation_draw()
		ScrollView:
			MDList:
				TwoLineIconListItem:
					text: "0.477 metric tons carbon per capita?"
					secondary_text: "Lower CO2 level! Acid rain will be inevitable soon."
					font_style: 'Body2'
									
					IconLeftWidget:
						icon: 'smog'
						
				TwoLineIconListItem:
					text: "Mass tree plantation is needed!"
					secondary_text: "Trees are below 25%."
					font_style: 'Body2'

					IconLeftWidget:
						icon: 'nature-people'
				TwoLineIconListItem:
					text: "Temperature may rise about 3°C in this week!"
					secondary_text: "There is a rise of temperature in the last week's data."
					font_style: 'Body2'

					IconLeftWidget:
						icon: 'thermometer-alert'

<PostScreen>:
	name: 'post'
	MDGridLayout:
		cols: 1
		MDToolbar:
			title: "Post"
			mode: 'end'
			type: 'top'
			left_action_items: [["arrow-left", lambda x: app.changeScreen('input')]]
			right_action_items: [["send", lambda x: root.post()]]
	
	MDTextField:
		id: post_txt
		hint_text: "Post Content"
		mode: "rectangle"
		pos_hint: {"center_x": .5, "center_y": 0.7}
		size_hint: 0.8, 0.3
	
	MDList:
		id: img_list
		pos_hint: {"center_x": 0.5, "center_y": 0.25}

	OneLineIconListItem:
		pos_hint: {"center_x": 0.5, "center_y": 0.5}
    	text: "Add Photo/Video"
		on_release: root.file_man()
    	IconLeftWidget:
        	icon: "camera-plus"
		
<NasaCornerScreen>:
	name: 'nasac'
	GridLayout:
		cols: 1
		#rows: 3
		#orientation: 'horizontal'
		#size_hint_y: None
		height: self.minimum_height
		MDToolbar:
			id: data_viewer_title
			title: "Nasa Corner"
			left_action_items: [["arrow-left", lambda x: app.changeScreen('data')]]
			mode: 'end'
			type: 'top'
			icon: "language-python"
			#on_action_button: app.navigation_draw()
		ScrollView:
			MDList:
				ThreeLineAvatarListItem:
					text: "Climate Kids"
					secondary_text: "A kid-friendly website to gain knowledge about environment."
					tertiary_text: "climatekids.nasa.gov"
					on_release: app.openLink('https://climatekids.nasa.gov')
					ImageLeftWidget:
						source: "icons/climate-kids.png"
						
				ThreeLineAvatarListItem:
					text: "Space Place"
					secondary_text: "A great place to start knowing about space. Contains kid friendly games."
					tertiary_text: "spaceplace.nasa.gov"
					on_release: app.openLink('https://spaceplace.nasa.gov')
					ImageLeftWidget:
						source: "icons/space-place.png"
				
				ThreeLineAvatarListItem:
					text: "EO Kids"
					secondary_text: "A blog from NASA for audiences aged 9 to 14."
					tertiary_text: "earthobservatory.nasa.gov/blogs/eokids"
					on_release: app.openLink('https://earthobservatory.nasa.gov/blogs/eokids')
					ImageLeftWidget:
						source: "icons/eokids-logo.png"
				
				ThreeLineAvatarListItem:
					text: "Nasa Image Gallery"
					secondary_text: "Images from Nasa about space and their work."
					tertiary_text: "www.nasa.gov/multimedia/imagegallery/iotd.html"
					on_release: app.openLink('www.nasa.gov/multimedia/imagegallery/iotd.html')
					ImageLeftWidget:
						source: "icons/nasa-logo.jpg"
				
				ThreeLineAvatarListItem:
					text: "Nasa: Climate Change and Global Warming"
					secondary_text: "Information about climate change and global warming!"
					tertiary_text: "climate.nasa.gov"
					on_release: app.openLink('https://climate.nasa.gov')
					ImageLeftWidget:
						source: "icons/nasa-logo.jpg"

<NDVScreen>:
	name: 'ndv'

	ScrollView:
		#size: self.size
		#size_hint: 1, None
		#height: self.minimum_height
		GridLayout:
			id: scroll_grid
			size_hint_y: None
			height: self.minimum_height  #<<<<<<<<<<<<<<<<<<<<
			#row_default_height: 500
			cols:1
			padding: 30
			spacing: 30
			#row_force_default: True

			MDLabel:
				id: title
				size_hint_y:None
				font_style: 'H6'
				padding_bottom: 400
				#text: 5*"d awoifhaisfia9 hdfiaw fioahdf9hawcoe rfiehs9f hasdfhaiwe8 wte87tawe8fPython | Scrollview widget in kivyLast Updated: 06-02-2020Kivy is a platform-independent GUI tool in Python. As it can be run on Android, IOS, Linux, and Windows, etc. It is basically used to develop the Android application, but it does not mean that it can not be used on Desktop applications.👉🏽 Kivy Tutorial – Learn Kivy with Examples.Scroll view:The ScrollView widget provides a scrollable/pannable viewport that is clipped at the scrollview’s bounding box.Scroll view accepts only one child and applies a window to it according to 2 properties:1) scroll_x2) scrool_yTo determine if interaction is a scrolling gesture, these properties are used:Python | Scrollview widget in kivyLast Updated: 06-02-2020Kivy is a platform-independent GUI tool in Python. As it can be run on Android, IOS, Linux, and Windows, etc. It is basically used to develop the Android application, but it does not mean that it can not be used on Desktop applications.👉🏽 Kivy Tutorial – Learn Kivy with Examples.Scroll view:The ScrollView widget provides a scrollable/pannable viewport that is clipped at the scrollview’s bounding box.Scroll view accepts only one child and applies a window to it according to 2 properties:1) scroll_x2) scrool_yTo determine if interaction is a scrolling gesture, these properties are used:Python | Scrollview widget in kivyLast Updated: 06-02-2020Kivy is a platform-independent GUI tool in Python. As it can be run on Android, IOS, Linux, and Windows, etc. It is basically used to develop the Android application, but it does not mean that it can not be used on Desktop applications.👉🏽 Kivy Tutorial – Learn Kivy with Examples.Scroll view:The ScrollView widget provides a scrollable/pannable viewport that is clipped at the scrollview’s bounding box.Scroll view accepts only one child and applies a window to it according to 2 properties:1) scroll_x2) scrool_yTo determine if interaction is a scrolling gesture, these properties are used:"
				#text_size: self.width, None
				height: self.texture_size[1]

			MDLabel:
				id: explanation
				size_hint_y:None
				text: 10*"d awoifhaisfia9 hdfiaw fioahdf9hawcoe rfiehs9f hasdfhaiwe8 wte87tawe8fPython | Scrollview widget in kivyLast Updated: 06-02-2020Kivy is a platform-independent GUI tool in Python. As it can be run on Android, IOS, Linux, and Windows, etc. It is basically used to develop the Android application, but it does not mean that it can not be used on Desktop applications.👉🏽 Kivy Tutorial – Learn Kivy with Examples.Scroll view:The ScrollView widget provides a scrollable/pannable viewport that is clipped at the scrollview’s bounding box.Scroll view accepts only one child and applies a window to it according to 2 properties:1) scroll_x2) scrool_yTo determine if interaction is a scrolling gesture, these properties are used:Python | Scrollview widget in kivyLast Updated: 06-02-2020Kivy is a platform-independent GUI tool in Python. As it can be run on Android, IOS, Linux, and Windows, etc. It is basically used to develop the Android application, but it does not mean that it can not be used on Desktop applications.👉🏽 Kivy Tutorial – Learn Kivy with Examples.Scroll view:The ScrollView widget provides a scrollable/pannable viewport that is clipped at the scrollview’s bounding box.Scroll view accepts only one child and applies a window to it according to 2 properties:1) scroll_x2) scrool_yTo determine if interaction is a scrolling gesture, these properties are used:Python | Scrollview widget in kivyLast Updated: 06-02-2020Kivy is a platform-independent GUI tool in Python. As it can be run on Android, IOS, Linux, and Windows, etc. It is basically used to develop the Android application, but it does not mean that it can not be used on Desktop applications.👉🏽 Kivy Tutorial – Learn Kivy with Examples.Scroll view:The ScrollView widget provides a scrollable/pannable viewport that is clipped at the scrollview’s bounding box.Scroll view accepts only one child and applies a window to it according to 2 properties:1) scroll_x2) scrool_yTo determine if interaction is a scrolling gesture, these properties are used:"
				#text_size: self.width, None
				height: self.texture_size[1]
			
			MDRaisedButton:
				id: button
				text: "Visit Link"
				pos_hint: {"center_x": .5}
				md_bg_color: 0, 179/255, 0, 1
				on_press: root.butt_ac()

<ImgScreen>:
	name: 'img'

	BoxLayout:
        #size_hint_y: 0.8
        #orientation: 'vertical'
        adaptive_size: True
        id: box
        Scatter:
            id: scatter_box
            scale_min: .5
            scale_max: 8
            size: box.size
            pos: box.pos
            #scale: 5
            pos: img.pos
            do_rotation: False
            Image :
                id: img
                size: box.width, box.height
                #size: (500, 500/self.image_ratio)  
                #pos: 1, 1
                allow_stretch: True
                keep_ratio: True

<SocialShare>:
	name: 'social'
	
	MDLabel:
		halign: 'center'
		size_hint_y:None
		font_style: 'H3'
		text: 'Social Share'
		pos_hint: {"center_x": .5, "center_y": .9}
	
	MDLabel:
		#halign: 'center'
		size_hint_y:None
		text: "Share this post once again on any social media as a public post and put the link here to get extra point. Go back if you're not interested."
		pos_hint: {"center_x": .54, "center_y": .8}
	
	MDTextField:
		id: link
		hint_text: "Link"
		pos_hint: {"center_x": .5, "center_y": 0.6}
		size_hint: 0.7, None
		helper_text_mode: "on_focus"
		#icon_right: "account"
	
	MDRaisedButton:
		text: "Submit"
		pos_hint: {'center_x': 0.5, 'center_y':0.5}
		#md_bg_color: 0, 179/255, 0, 1
		on_press: root.postLink()

"""
