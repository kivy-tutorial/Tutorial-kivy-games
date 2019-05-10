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
from random import random


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
        self. ids.player.speed += -self.height*2 * 1/30
        self. ids.player.y += self.ids.player.speed * 1/30

        # Condição para perde o jogo
        if self.ids.player.y > self.height or self.ids.player.y < 0:
            self.gameOver()
        
        # verificar se colideil
        elif self.playerCollided():
            self.gameOver()


    def putObstacle(self, *args):
        """method put obstacle."""

        # gap = 200
        # gap = self.height*0.3
        gap = self.height*0.35
        # position = 400
        position = (self.height - gap)*random()
        widt = self.width*0.05

        # Instace Obstacle class        
        obstacleLow = Obstacle(x=self.width, height=position, width=widt)
        obstacleHigh = Obstacle(
                                x=self.width,
                                y=position + gap,
                                height=self.height - position - gap,
                                width=widt)
        self.add_widget(obstacleLow, 3)
        self.add_widget(obstacleHigh, 3)
        self.obstacles.append(obstacleLow)
        self.obstacles.append(obstacleHigh)


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

    
    def collided(self, wid1, wid2):
        """method Collided."""

        # wid1 = play, wid2 = obstacles 
        # \ para usar mais de uma linha
        if wid2.x <= wid1.x + wid1.width and wid2.x + wid2.width >= wid1.x and \
            wid2.y <= wid1.y + wid1.height and  wid2.y + wid2.height >= wid1.y:
            return True
        return False


    def playerCollided(self):
        """method Player Collided."""
        collided = False 

        for obstacle in self.obstacles:
            # wid1 = play, wid2 = obstacles 
            if self.collided(self.ids.player, obstacle):
                collided = True
                break
        return collided


    def on_touch_down(self, *args):
        """method on touch down."""
        self.ids.player.speed = self.height * 0.7


class Obstacle(Widget):
    """Class Obstacle."""
    color = ListProperty([0.3, 0.2, 0.2, 1])

    def __init__(self, **kwargs):
        """Method init from Obstacle."""
        super().__init__(**kwargs)
        
        self.anim = Animation(x=-self.width, duration=3)
        self.anim.bind(on_complete=self.vanish)
        self.anim.start(self)

    def vanish(self, *args):
        """Method vanish from Obstacle."""

        # outra forma de fazer remover widget
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
