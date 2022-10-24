from distutils.log import debug
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout

Builder.load_file('design.kv')

# create classe that have same name as rules in kivy

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

class SignUpScreen(Screen):
    pass


if __name__ == "__main__":
    MainApp().run()