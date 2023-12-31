from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window

Window.size = (500, 650)

from screens.screens import *

class WindowManager(ScreenManager):
	pass

class IREPAIR(MDApp):
	def build(self):
		self.wm = WindowManager()
		screens =[
			Hallog(name="hallog"),
			Hallogadmin(name="hallogadmin"),
			pythonform(name="pythonform"),
			Daftar(name="daftar"),
		]
		for screen in screens:
			self.wm.add_widget(screen)
		return self.wm
if __name__ == '__main__':
	LabelBase.register(name="Atma", fn_regular="kv/assets/fonts/Atma-Bold.ttf")
	LabelBase.register(name="Tagline", fn_regular="kv/assets/fonts/Ubuntu-LI.ttf")
	LabelBase.register(name="Line", fn_regular="kv/assets/fonts/Ubuntu-M.ttf")
	IREPAIR().run()