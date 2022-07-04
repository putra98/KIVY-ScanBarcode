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
import urllib.request
import urllib.parse
from kivymd.uix.datatables import MDDataTable
import json
import codecs
import utils

class ScanScreen(MDScreen):


	def kode(self, ins):
		print(ins)
		# instance = 
		try:
			with open('json/url.json', 'r') as f:
				data = json.load(f)
			for item in data:
				urll = item['url']
			url 			= 'http://{}/check_data.php'.format(urll)
			data 			= {'kode':"{}".format(eval(ins))}
			headers 		= {'application/json; charset=utf-8'}
			post_data 		= urllib.parse.urlencode(data).encode()
			post_response 	= urllib.request.urlopen(url=url, data=post_data)
			text_res 		= post_response.read()
			text_str 		= text_res.decode("utf-8")
			with open('json/file.json', 'w') as f:
				json.dump(text_str, f)
				print(text_str)
			self.manager.current = "data_name"
			Snackbar(text="[color=#37E125]Sukses.[/color]",bg_color=(0,0,.45,1)).open()
		except:
			print('failed')
			Snackbar(text="[color=#E12525]Gagal Upload[/color]",bg_color=(0,0,.45,1)).open()

	def back(self):
		self.manager.current = "root_name"
		
