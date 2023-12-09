from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Hallog(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv//hallog.kv")
        super().__init__(**kw)