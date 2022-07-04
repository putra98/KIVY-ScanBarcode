from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivy.clock import Clock
import threading
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ListProperty, StringProperty, ObjectProperty, BooleanProperty
from kivymd.uix.snackbar import Snackbar

from kivymd.uix.datatables import MDDataTable
import json

class RootScreen(MDScreen):
	data = {
        'Scan QR': 'qrcode-scan',
        'Data Material':  'plus-thick',
        'Data Setting Mesin': 'plus-outline',
    }
	def callback(self, instance):
		print(instance.icon)
		if instance.icon == "qrcode-scan":
			self.manager.current = "scan_name"
		elif instance.icon == "plus-thick":
			self.manager.current = "input_barang_name"
		elif instance.icon == "plus-outline":
			self.manager.current = "input_mesin_name"
	def qr(self):
		self.dialog_password = MDDialog(
				type="custom",
				content_cls=ScanScreen(),
				# buttons=[
    #                     MDFlatButton(
    #                         text="CANCEL",md_bg_color=(0,1,0,1)
    #                     ),

    #                     MDRaisedButton(
    #                         text='.',
    #                     ),
				# 		MDRaisedButton(
    #                         text='SEND', md_bg_color=(0,1,1,1)
    #                     ),
                    # ],
                )

		# self.dialog_password.set_normal_height()
		self.dialog_password.open()