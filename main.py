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


class Manager(ScreenManager):
    """Class Manager Menu."""
    pass


class Menu(Screen):
    """Class Menu."""
    pass


class Game(Screen):
    """Class Game."""
    pass


class Player(Image):
    """Class Player."""
    pass


class HashBird(App):
    """Main Class Hasbird."""

    pass


HashBird().run()
