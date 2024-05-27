import os
print (os.getcwd())
import pyautogui
from time import sleep
#from image import *
from PIL import Image

photos_folder = r'/images'
bombs = []
bounds = []
bound_centers = []

""" Testing with pyautogui
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

pyautogui.moveTo(100, 150)

pyautogui.click()

"""

def setup():
  """
  sets up the game by opening the images then
  appending them to an array, one for bombs, one for bounds.
  """
  black_bomb = Image.open(r'./images/BlackBomb.png')
  red_bomb = Image.open(r'./images/RedBomb.png')

  #black_bomb = Image.open(r'./images/BlackBombFullQuality.png')
  #red_bomb = Image.open(r'./images/RedBombFullQuality.png')
  
  bombs.append((black_bomb, "black"))
  bombs.append((red_bomb, "red"))

  black_bound = Image.open(r'./images/BlackBombBounds.png')
  red_bound = Image.open(r'./images/RedBombBounds.png')

  #black_bound = Image.open(r'./images/BlackBombBoundsFullQuality.png')
  #red_bound = Image.open(r'./images/RedBombBoundsFullQuality.png')
  
  bounds.append((black_bound, "black"))
  bounds.append((red_bound, "red"))

def play_game():

  touch_screen = pyautogui.screenshot(region=(590, 532, 744, 548))
  for bound in bounds:
      # Can do this by just knowing first is black and second is red?
      #found_bound = pyautogui.locate(bound, touch_screen, confidence=0.3)
    found_bound = pyautogui.locateOnScreen(bound[0], confidence=0.47)
    print("Color of bound is " + bound[1])
    center_of_bound = pyautogui.center(found_bound)

      #pyautogui.moveTo(center_of_bound[0], center_of_bound[1])
      #print("Box")
      #print(center_of_bound)
    bound_centers.append((center_of_bound, bound[1]))
      #sleep(1)
  bound_tuple = (bound_centers[0], bound_centers[1])
#  print(bound_tuple)

  for bomb in bombs:
    #found_bomb = pyautogui.locate(bomb, touch_screen, confidence=0.5)
    try:
      found_bomb = pyautogui.locateOnScreen(bomb[0], confidence=0.94)
      bomb_color = bomb[1]
      print("Color is " + bomb[1])
      center_of_bomb = pyautogui.center(found_bomb)
      #print(center_of_bomb[0], center_of_bomb[1])
      pyautogui.moveTo(center_of_bomb[0], center_of_bomb[1])
      #sleep(1)
    except:
      # Since ImageNotFoundError is raised if no image is on screen and halts program,
      # just catch and handle the error (sometimes there might be no red bombs but that's okay)
      print("Could not find " + bomb[1])
      continue
    #print(pyautogui.position())
    #print(bound_tuple[0][0], bound_tuple[0][1])
    #pyautogui.drag(bound_tuple[0][0]-center_of_bomb[0], bound_tuple[0][1]-center_of_bomb[1], duration=0.5)
    
    #bound_x = bound_tuple[0][0]
    #pyautogui.dragTo(bound_tuple[0][0][0], bound_tuple[0][0][1], button='left', duration=0.25)
    # These two get black, red respecitvely: bound_tuple[0][1], bound_tuple[1][1]
    
    #print(pyautogui.position())
    #print("Bomb")
    #print(found_bomb)
    for bound in bound_tuple:
      bound_pos, bound_color = bound
      bound_x, bound_y = bound_pos
      if bomb_color == bound_color:
        print("Match with " + bomb_color, bound_color, bound_pos)  
        pyautogui.dragTo(bound_x, bound_y, button='left', duration=0.25)
    


"""
print("3...")
sleep(1)
print("2...")
sleep(1)
print("1...")
sleep(1)

"""

sleep(4)
setup()
a = 0
while a < 100:
  play_game()

