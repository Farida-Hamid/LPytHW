from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

  def enter(self):
    print("This scene is not yet configured.")
    print("sSubclass it and implement enter().")
    exit(1)


class Engine(object):

  def __init__(self, scene_map):
    self.scene_map = scene_map

  def play(self):
    current_scene = self.scene_map.opening_scene()
    last_scenen = self.scene_map.next_scense('finished')

    while current_scene != last_scenen:
      next_scene_name = current_scene.enter()
      current_scene = self.scene_map.next_scene(next_scene_name)

    # be sure to print out the last scenen
    current_scene.enter()

class Death(Scene):

  def enter(self):
    pass

class CentralCorridor(Scene):

  def enter(self):
    pass

class LaserWeaponArmory(Scene):

  def enter(self):
    pass

class TheBridge(Scene):

  def enter(self):
    pass

class EscapePod(Scene):

  def enter(self):
    pass

class Map(object):

  def __init__(self, start_scene):
    pass

  def next_scense(self, scene_name):
    pass

  def openning_scene(self):
    pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()