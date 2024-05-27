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
  
  bombs.append(black_bomb)
  bombs.append(red_bomb)

  black_bound = Image.open(r'./images/BlackBombBounds.png')
  red_bound = Image.open(r'./images/RedBombBounds.png')

  #black_bound = Image.open(r'./images/BlackBombBoundsFullQuality.png')
  #red_bound = Image.open(r'./images/RedBombBoundsFullQuality.png')
  
  bounds.append(black_bound)
  bounds.append(red_bound)

def play_game():

  touch_screen = pyautogui.screenshot(region=(590, 532, 744, 548))
  for bound in bounds:
    #TODO: Need a way to separate the red / black bounds
    # Can do this by just knowing first is black and second is red?
    #found_bound = pyautogui.locate(bound, touch_screen, confidence=0.3)
    found_bound = pyautogui.locateOnScreen(bound, confidence=0.4)
    center_of_bound = pyautogui.center(found_bound)
    #print("Box")
    #print(center_of_bound)
    bound_centers.append(center_of_bound)
  bound_tuple = (bound_centers[0], bound_centers[1])
#  print(bound_tuple)

  for bomb in bombs:
    # Should alternate black / red / black / red / ...
    #found_bomb = pyautogui.locate(bomb, touch_screen, confidence=0.5)
    found_bomb = pyautogui.locateOnScreen(bomb, confidence=0.6)
    center_of_bomb = pyautogui.center(found_bomb)
    #print(center_of_bomb[0], center_of_bomb[1])
    pyautogui.moveTo(center_of_bomb[0], center_of_bomb[1])

    print(pyautogui.position())
    #print(bound_tuple[0][0], bound_tuple[0][1])
    #pyautogui.drag(bound_tuple[0][0]-center_of_bomb[0], bound_tuple[0][1]-center_of_bomb[1], duration=0.5)
    pyautogui.dragTo(bound_tuple[0][0], bound_tuple[0][1], button='left', duration=0.2)
    print(pyautogui.position())
    #print("Bomb")
    #print(found_bomb)
    


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

