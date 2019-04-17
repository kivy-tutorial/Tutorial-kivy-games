"""
Create Kivy game from scratch

Criação de jogos com Kivy e Python

Homepage and documentation:
https://github.com/kivy-tutorial/Tutorial-kivy-games

License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import NumericProperty


class Manager(ScreenManager):
    """Class Manager Menu."""
    pass


class Menu(Screen):
    """Class Menu."""
    pass


class Game(Screen):
    """Class Game."""

    def on_enter(self, *args):
        """method enter."""
        Clock.schedule_interval(self.update, 1/30)


    def update(self, *args):
        """method update."""
        self. ids.player.speed += -self.height * 1/30
        self. ids.player.y += self.ids.player.speed * 1/30


    def on_touch_down(self, *args):
        """method on touch down."""
        self.ids.player.speed = self.height * 0.7


class Player(Image):
    """Class Player."""
    speed = NumericProperty(0)


class HashBird(App):
    """Main Class Hasbird."""

    pass


HashBird().run()
