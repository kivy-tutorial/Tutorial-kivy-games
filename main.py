"""
Create Kivy game from scratch

Criação de jogos com Kivy e Python

Homepage and documentation:
https://github.com/kivy-tutorial/Tutorial-kivy-games

License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class HashBird(App):
    """Main Class Hasbird."""

    def build(self):
        """Build Method."""
        player = Image(source='img/player.png')
        layout = FloatLayout()
        layout.add_widget(player)
        return layout        


HashBird().run()
