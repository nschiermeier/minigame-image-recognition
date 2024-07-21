import os
print (os.getcwd())
import pyautogui
from pyautogui import locateOnScreen, locateAllOnScreen, center, moveTo, mouseDown, mouseUp, ImageNotFoundException
from time import sleep
from PIL import Image
import numpy as np

photos_folder = r'/images'
# region is (left_most_pixel, top_most_pixel, width, height)
#region = (1150, 740, 250, 250)
region = (1170, 800, 205, 150)

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
    bomb_pos = center(locateOnScreen(bomb, confidence=0.80, region = region))
     
    moveTo(bomb_pos)
    mouseDown()
  except:
    print("no bomb")

def release_bomb():
  mouseUp() # Does this really need to be a function?

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def move_bomb(points, region, step=1):
  
  max_dist = 0
  furthest_point = None
  # issue: I had region measuring the entire touchscreen, which doesn't work
  #        because the playable area is slightly smaller. Either shrink playable
  #        area here, or remeasure touchscreen region.
  x_range = np.arange(region[0], region[0] + region[2], step)
  y_range = np.arange(region[1], region[1] + region[3], step)

  for curr_x in x_range:
    for curr_y in y_range:
      for x, y in points:
        new_dist = euclidean_distance((x,y), (curr_x, curr_y))

        if new_dist > max_dist:
          max_dist = new_dist
          furthest_point = (curr_x, curr_y)
  
  return furthest_point

def play_game(images):
  print("game")
  bomb, fireball, bowser_fire = images
  rotation = 0
  fireball_count = len(list(locateAllOnScreen(fireball, confidence=.8, region=region)))
  dodge_poss = [] # List of positions to be avoided, will be passed into the scipy max distance
  for fire in bowser_fire:
    rotation += 90
    try:
      print(center(locateOnScreen(fire, confidence=0.70, region=(region))))
      # locateOnScreen returns Point(x=X, y=Y), so maybe just say go away from that?

      #moveTo(center(locateOnScreen(fire, confidence=0.70, region=(800, 520, 310, 220))))
      dodge_poss.append(center(locateOnScreen(fire, confidence=0.70, region=region)))
    except ImageNotFoundException:
      print(rotation)

  # How do I move the bomb away? Need some type of distance function/heuristic
  print(f"There are {fireball_count} fireballs located on screen")
  # for pos in locateAllOnScreen(fireball, confidence=.8, region=region):
  #  print(pos)
  #  moveTo(pos)
  #  sleep(2)
  #  dodge_poss.append(center(pos))
  dodge_poss.extend(center(pos) for pos in locateAllOnScreen(fireball, confidence=.8, region=region))
  print(dodge_poss)

  new_bomb_pos = move_bomb(dodge_poss, region)
  moveTo(new_bomb_pos)
  sleep(0.1)
  
  

#b = setup()
#hold_bomb(b)
#release_bomb()
#a = play_game(b)

#Initialize, give time to set up game after running program
for i in range(4,-1,-1):

  print(str(i)+"...")
  sleep(1)

b = setup()
hold_bomb(b)
a = 0
while a < 500:
  play_game(b)
  a+=1
releease_bomb()
