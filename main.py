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
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, ListProperty
from kivy.animation import Animation


class Manager(ScreenManager):
    """Class Manager Menu."""
    pass


class Menu(Screen):
    """Class Menu."""
    pass


class Game(Screen):
    """Class Game."""

    obstacles = []

    def on_enter(self, *args):
        """method enter."""
        # Gravidade
        Clock.schedule_interval(self.update, 1/30)
        Clock.schedule_interval(self.putObstacle, 1)

    def on_pre_enter(self, *args):
        """method on pre enter."""
        self.ids.player.y = self.height/2
        self.ids.player.speed = 0


    def update(self, *args):
        """method update."""

        # Física do Jogo
        self. ids.player.speed += -self.height * 1/30
        self. ids.player.y += self.ids.player.speed * 1/30
        
        # Condição para perde o jogo
        if self.ids.player.y > self.height or self.ids.player.y < 0:
            self.gameOver()
    

    def putObstacle(self, *args):
        """method put obstacle."""

        # Instace Obstacle class
        obstacle = Obstacle(x=self.width, height=400)
        self.add_widget(obstacle)
        self.obstacles.append(obstacle)


    def gameOver(self, *args):
        """method Game Over."""
        Clock.unschedule(self.update, 1/30)
        Clock.unschedule(self.putObstacle, 1)

        # remove os obstacle da lista obstacles
        for ob in self.obstacles: 
            # cancelar a animação no gameover
            ob.anim.cancel(ob)
            self.remove_widget(ob)

        self.obstacles = []
        App.get_running_app().root.current = 'gameOver'


    def on_touch_down(self, *args):
        """method on touch down."""
        self.ids.player.speed = self.height * 0.7


class Obstacle(Widget):
    """Class Obstacle."""
    color = ListProperty([0.3, 0.2, 0.2, 1])

    def __init__(self, **kwargs):
        """Method init from Obstacle."""
        super().__init__(**kwargs)
        
        self.anim = Animation(x=-self.height, duration=3)
        self.anim.bind(on_complete=self.vanish)
        self.anim.start(self)

    def vanish(self, *args):
        """Method vanish from Obstacle."""

        # if self.parent:
        #     # parent == Game(Screen)
        #     self.parent.remove_widget(self)

        # outra forma de fazer
        gameScreen = App.get_running_app().root.get_screen('game')
        gameScreen.remove_widget(self)

        # Atualizar lista de obstacle
        gameScreen.obstacles.remove(self)

class GameOver(Screen):
    """Class Game Over."""
    pass


class Player(Image):
    """Class Player."""
    speed = NumericProperty(0)


class HashBird(App):
    """Main Class Hasbird."""
    pass


HashBird().run()
