import os
print (os.getcwd())
import pyautogui
from pyautogui import locateOnScreen, center, moveTo, mouseDown, mouseUp, ImageNotFoundException
from time import sleep
from PIL import Image

photos_folder = r'/images'

"""
Idea: Maybe have a second setup() function that just calls mouseDown on the bomb
      so that I can continuously loop the moving away from fire part? Then call
      and end_game() function that will release mouseDown
"""

def setup():
  print("setting up")
  bomb = Image.open(r'./images/DangerBomb.png')
  fireball = Image.open(r'./images/Fireball.png')
  # Since the fireballs are spinning from Bowser, I rotated the Image and 
  # will have it as a tuple that will check all rotations in case a fireball
  # isn't in the correct orientation.
  bowser_fireballs = (
                      Image.open(r'./images/BowserFireball_0.png'), 
                      Image.open(r'./images/BowserFireball_90.png'),
                      Image.open(r'./images/BowserFireball_180.png'),
                      Image.open(r'./images/BowserFireball_270.png'),
                )
  game_components = (bomb, fireball, bowser_fireballs)
  return game_components

def hold_bomb(images):
  bomb = images[0]
  try: 
    bomb_pos = center(locateOnScreen(bomb, confidence=0.85, region = (800, 520, 310, 220)))
     
    moveTo(bomb_pos)
    mouseDown()
    moveTo(600, 600)
  except:
    print("no bomb")

def release_bomb():
  mouseUp() # Does this really need to be a function?

def play_game(images):
  print("game")
  bomb, fireball, bowser_fire = images
  rotation = 0
  for fire in bowser_fire:
    rotation += 90
    try:
      print(center(locateOnScreen(fire, confidence=0.70, region=(800, 520, 310, 220))))
      # locateOnScreen returns Point(x=X, y=Y), so maybe just say go away from that?

      #moveTo(center(locateOnScreen(fire, confidence=0.70, region=(800, 520, 310, 220))))
    except ImageNotFoundException:
      print(rotation)

  # How do I move the bomb away? Need some type of distance function/heuristic
    
  


b = setup()
hold_bomb(b)
release_bomb()
a = play_game(b)

