from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

  def enter(self):
    print("This scene is not yet configured.")
    print("Subclass it and implement enter().")
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

  quips = [
    "You died. You kinda suck at this.",
    "Your Mom would be proud...if she were smarter.",
    "Such a luser.",
    "I have a small puppy the's better at this.",
    "You're worse than your Dad's jokes."
  ]

  def enter(self):
    print(Death.quips[randint(0, len(self.quips) -1)])
    exit(1)

class CentralCorridor(Scene):

  def enter(self):
    print(dedent("""
          The Gothons of planet percal #25 have invaded your ship and 
          destroyed your entire crew. You are the last surviving
          member and your last mission is to get the neutron destruct
          bomb from Weapons Armory, put it in the bridge, and
          blow the ship up after getting into an esca[e pod.
            
          You're running down the central corridor to the weapons
          Armory when Gothon jumps out, red scaly skin, dark grimmy
          teeth, and evil clown costume flowing around his hate
          filled body. He's blocking the door to the Armory and
          about to pull a weapon to blast you.
          """))
    
    action = input("> ")

    if action == "shoot!":
      print(dedent("""
            The Quick on the draw you yank out your blaster and fire
            iit at the Gothon. His clown costume is flowing and
            moving his nody, which thoughs off your aim.
            Your laser hits his costume but misses him entirely.
            this complerely ruins his brand new costume  his mother 
            bought him, which makes him fly into an insane rage
            and blast you repeatedly in the head until you are
            dead. The  eats you.
            """))
      return 'death'
    
    elif action == "dodge!":
      print(dedent("""
            Like a world calss master, you dodge, weave, slip and
            slide right as the Gothon's blaster crancks a laser
            past your head. In the middle of your artful dodge
            your foor slips and bangs your head in the metal
            wall and the Gothon stops on your head and eats you.
            """))
      return 'death'
    
    elif action =="tell a joke":
      print(dedent("""
            Luckly for you, they made you learn Gothon insults in
            the academy. You tell tha one Gothon joke you know:
            lbhe zbgure vf sng, jura fur fvgf nebhaq gur unhfr,
            furfvgf nebhaq gur ubhfr. The Gothon stops, tries
            to lagh, then busts out laughing and can't move.
            While he's laughing you run up and shoot him square in
            the head putting him down, then jump through the
            Weapon Armory door.
            """))
      return 'laser_weapon_armory'
    
    else:
      print("DOES NOT COMPUTE!")
      return 'central_corridor'
    

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