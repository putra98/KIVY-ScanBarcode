from kivy.app import App
from kivy.properties import StringProperty
from kivy.clock import Clock, mainthread
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.spinner import MDSpinner
import urllib.request
import urllib.parse
import json
import concurrent.futures
import utils
from kivymd.uix.snackbar import Snackbar
from kivy.lang.builder import Builder
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
import utils

class Loading(MDBoxLayout):
	pass

class LoginScreen(MDScreen):
	dialog = None

	# email_value = StringProperty("ss")
	# pass_value = StringProperty("passd")
		
	try:
		with open('json/user.json', 'r') as f:
			data = json.load(f)
		for item in data:
			email = item['nik']	
			passd = item['password']

		email_value = StringProperty(email)
		pass_value = StringProperty(passd)

	except Exception as e:
		email_value = StringProperty()
		pass_value = StringProperty()

	def login(self):
		self.email 		= self.ids.email_id
		self.userr    	= self.email.text
		self.user_l     = str(self.userr)

		self.password 	= self.ids.password_id
		self.passdd    	= self.password.text
		self.pasw_l    	= str(self.passdd)
		

		label = self.ids.success

		try:
			with open('json/url.json', 'r') as f:
				data = json.load(f)
			for item in data:
				urll = item['url']
			url 			= 'http://{}/autentication.php'.format(urll)
			print(url)
			data2 			= {'nik':self.user_l, 'password':self.pasw_l}
			headers 		= {'application/json; charset=utf-8'}
			post_data 		= urllib.parse.urlencode(data2).encode()
			post_response 	= urllib.request.urlopen(url=url, data=post_data)
			text_res 		= post_response.read()
			text_str 		= text_res.decode("utf-8")
			# data = json.loads(text_str)
			# print(data)
			if  text_str == 'failed':

				label.text ="[color=#FC2828]NIK atau Pasword salah.[/color]"
				self.dismiss()
					
			else:
				self.dismiss()
				self.manager.current = "root_name"
				Clock.schedule_once( self.pop_up2('berhasil User'))  # pop_up2() must be done on the main thread

		except Exception as e:
			print(e)
			print('-------------------------------------')
			self.dismiss()
			Clock.schedule_once( self.pop_up2('Koneksi Gagal.!'))		

	def start(self,fuction):
		if fuction=='login':
			self.progress = self.login
			self.pop_up1()
		executor = concurrent.futures.ThreadPoolExecutor()
		f2 = executor.submit(self.progress)

	def pop_up1(self):
		'''Displays a pop_up with a spinning wheel'''
		self.dialog = MDDialog(
                title="Loading...",
                type="custom",
                content_cls=Loading(),
                )
		self.dialog.open()



	def pop_up2(self,title):
		Snackbar(text="[color=#ffffff]{}[/color]".format(title),
			bg_color=(0,.45,0,1)).open()

	@mainthread
	def dismiss(self, *args):
		self.dialog.dismiss()
