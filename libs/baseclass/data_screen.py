from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivy_garden.zbarcam.zbarcam import ZBarCam

from kivy.clock import Clock
import threading
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ListProperty, StringProperty, ObjectProperty, BooleanProperty
from kivymd.uix.snackbar import Snackbar

from kivymd.uix.datatables import MDDataTable
import json
import codecs

class DataScreen(MDScreen):

	table_id = ObjectProperty()
	text_json = StringProperty()
	dialog = None
	def view(self):
		self.layout = AnchorLayout()

		try:
			file_json = open("json/file.json")
			data 	  = json.loads(file_json.read())
			data2	  = data.replace("\'","")
			data3 	  = eval(data2)
			print(type(data3))
			self.ids.table_id.clear_widgets()
			data_tables = MDDataTable(
	            size_hint=(1, .8),
	            # use_pagination=True,
	            column_data=[('{}'.format(value),dp(30)) for value, key in data3.items()],
	            row_data=[

	                 (
						[(key) for value, key in data3.items()]
					
					),
	                 (
						[('') for value, key in data3.items()]
					
					)
	            ],
	        )
			self.layout.add_widget(data_tables)
			self.ids.table_id.add_widget(self.layout)
			Snackbar(text="[color=#32E125]Type Json[/color]",bg_color=(0,0,.45,1)).open()
		except:
			print('failed')
			Snackbar(text="[color=#E12525]Bukan Type Json[/color]",bg_color=(0,0,.45,1)).open()


	def back(self):
		self.ids.table_id.clear_widgets()
		self.manager.current= 'scan_name'
