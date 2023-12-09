from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class pythonform(MDScreen):
    pass

    def __init__(self, **kwargs):
        Builder.load_file("kv/pythonform.kv")
        super().__init__(**kwargs)





