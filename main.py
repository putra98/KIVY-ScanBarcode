
from kivy.utils import platform

if platform != 'android':
    from kivy.config import Config
    Config.set("graphics","width",360)
    Config.set("graphics","height",740)
    
import os
os.environ['DISPLAY'] = ':0'
import sys
from pathlib import Path
from kivy.uix.anchorlayout import AnchorLayout

from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.lang import Builder



if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["RALLY_ROOT"] = sys._MEIPASS
else:
    os.environ["RALLY_ROOT"] = str(Path(__file__).parent)


KV_DIR = f"{os.environ['RALLY_ROOT']}/libs/kv/"

for kv_file in os.listdir(KV_DIR):
    with open(os.path.join(KV_DIR, kv_file), encoding="utf-8") as kv:
        Builder.load_string(kv.read())


# from android.permissions import request_permissions, Permission

# request_permissions([Permission.INTERNET,
#                      Permission.READ_EXTERNAL_STORAGE,
#                      Permission.WRITE_EXTERNAL_STORAGE,
#                      Permission.CAMERA])

KV = """
#:import SwapTransition kivy.uix.screenmanager.SwapTransition
#:import LoginScreen libs.baseclass.login_screen.LoginScreen
#:import RootScreen libs.baseclass.root_screen.RootScreen
#:import HomeScreen libs.baseclass.home_screen.HomeScreen
#:import InputBarangScreen libs.baseclass.input_barang_screen.InputBarangScreen
#:import InputMesinScreen libs.baseclass.input_mesin_screen.InputMesinScreen
#:import ScanScreen libs.baseclass.scan_screen.ScanScreen
#:import DaftarScreen libs.baseclass.daftar_screen.DaftarScreen
#:import DataScreen libs.baseclass.data_screen.DataScreen

ScreenManager:

    transition: SwapTransition()
    ScanScreen: 
        name: "scan_name"
    DataScreen: 
        name: "data_name"
    LoginScreen:
        name: "login_name"
    DaftarScreen: 
        name: "daftar_name"
    RootScreen:
        name: "root_name"
    HomeScreen: 
        name: "home_name"
    InputBarangScreen:
        name: "input_barang_name"
    InputMesinScreen:
        name: "input_mesin_name"

"""


class MDRally(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Rally"
        self.icon = f"{os.environ['RALLY_ROOT']}/assets/images/logo.png"

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = "Light"
        FONT_PATH = f"{os.environ['RALLY_ROOT']}/assets/fonts/"

        self.theme_cls.font_styles.update(
            {
                "H1": [FONT_PATH + "RobotoCondensed-Light", 96, False, -1.5],
                "H2": [FONT_PATH + "RobotoCondensed-Light", 60, False, -0.5],
                "H3": [FONT_PATH + "Eczar-Regular", 48, False, 0],
                "H4": [FONT_PATH + "RobotoCondensed-Regular", 34, False, 0.25],
                "H5": [FONT_PATH + "RobotoCondensed-Regular", 24, False, 0],
                "H6": [FONT_PATH + "RobotoCondensed-Bold", 20, False, 0.15],
                "Subtitle1": [
                    FONT_PATH + "RobotoCondensed-Regular",
                    16,
                    False,
                    0.15,
                ],
                "Subtitle2": [
                    FONT_PATH + "RobotoCondensed-Medium",
                    14,
                    False,
                    0.1,
                ],
                "Body1": [FONT_PATH + "Eczar-Regular", 16, False, 0.5],
                "Body2": [FONT_PATH + "RobotoCondensed-Light", 14, False, 0.25],
                "Button": [FONT_PATH + "RobotoCondensed-Bold", 14, True, 1.25],
                "Caption": [
                    FONT_PATH + "RobotoCondensed-Regular",
                    12,
                    False,
                    0.4,    
                ],
                "Overline": [
                    FONT_PATH + "RobotoCondensed-Regular",
                    10,
                    True,
                    1.5,
                ],
                "Money": [FONT_PATH + "Eczar-SemiBold", 48, False, 0],
            }
        )
        return Builder.load_string(KV)


MDRally().run()
