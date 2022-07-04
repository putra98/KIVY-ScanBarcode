from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivy.clock import Clock, mainthread
import threading
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ListProperty, StringProperty, ObjectProperty, BooleanProperty
from kivymd.uix.snackbar import Snackbar
import concurrent.futures
from kivymd.uix.datatables import MDDataTable
import json
import urllib.request
import urllib.parse

class Loading(MDBoxLayout):
    pass

class InputMesinScreen(MDScreen):
    dialog = None

    def save(self):
        self.kode       = self.ids.kode_mesin_id
        self.kodee      = self.kode.text
        self.kodeee     = str(self.kodee)

        self.nama       = self.ids.nama_mesin_id
        self.namaa      = self.nama.text
        self.namaaa     = str(self.namaa)

        self.jumlah     = self.ids.jumlah_id
        self.jumlahh    = self.jumlah.text
        self.jumlahhh   = str(self.jumlahh)        


        try:
            with open('json/url.json', 'r') as f:
                data = json.load(f)
            for item in data:
                urll = item['url']
            url             = 'http://{}/add_mesin.php'.format(urll)
            print(url)
            data           = {'kode_mesin':self.kodeee, 'nama_mesin':self.namaaa,'jumlah':self.jumlahhh}
            headers         = {'application/json; charset=utf-8'}
            post_data       = urllib.parse.urlencode(data).encode()
            post_response   = urllib.request.urlopen(url=url, data=post_data)
            text_res        = post_response.read()
            text_str        = text_res.decode("utf-8")
            # Dict = eval(text_str)
            # print(Dict['result'])
            if  text_str == 'sukses':

                self.manager.current = "root_name"
                self.dismiss()
                Clock.schedule_once( self.pop_up2('Berhasil Upload.'))  # pop_up2() must be done on the main thread

            else:
                self.dismiss()
                Clock.schedule_once( self.pop_up2('Gagal Upload.'))  # pop_up2() must be done on the main thread

        except Exception as e:
            print(e)
            print('-------------------------------------')
            self.dismiss()
            Clock.schedule_once( self.pop_up2('Koneksi Gagal.!')) 

    def back(self):
        self.manager.current = "root_name"

    def start(self,fuction):
        if fuction=='save':
            self.progress = self.save
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