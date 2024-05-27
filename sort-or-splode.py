import os
print (os.getcwd())
import pyautogui
from time import sleep
from PIL import Image

photos_folder = r'/images'
bombs = []
bounds = []
bound_centers = []
bound_tuple = (0, 0)


def setup():
  """
  sets up the game by opening the images then
  appending them (and their color, as a tuple) 
  to an array: one for bombs, one for bounds.

  Returns: a tuple that is the x,y coords of the black bound as a tuple with the word "black",
           a tuple that is the x,y cords of the red bound as a tuple with the word "red"
  """
  black_bomb = Image.open(r'./images/BlackBomb.png')
  red_bomb = Image.open(r'./images/RedBomb.png')

  bombs.append((black_bomb, "black"))
  bombs.append((red_bomb, "red"))

  black_bound = Image.open(r'./images/BlackBombBounds.png')
  red_bound = Image.open(r'./images/RedBombBounds.png')

  bounds.append((black_bound, "black"))
  bounds.append((red_bound, "red"))
  
  for bound in bounds:
    # Find the center of the bounds the bombs belong in, then append them to an
    # array with their color, then add those to the tuple for the bounds
    # This needed to be created in set-up, because the bombs would get too crowded
    # and then it was no longer detectable
    found_bound = pyautogui.locateOnScreen(bound[0], confidence=0.47)
    print(f"Found the {bound[1]} bound")

    center_of_bound = pyautogui.center(found_bound)
    bound_centers.append((center_of_bound, bound[1]))
  bound_tuple = (bound_centers[0], bound_centers[1])
  return bound_tuple

def play_game(bound_tuple):
  """
    called every iteration of loop, will look for a bomb,
    and if it finds one, will drag it to the corresponding
    bound that matches it's color

    input: the bound tuple with the center x,y pos that was 
           created during setup
  """

  #touch_screen = pyautogui.screenshot(region=(590, 532, 744, 548))
  
  for bomb in bombs:
    bomb_color = bomb[1]
    try:
      # Find a bomb of the specified color in the tuple, then move
      # the mouse to the center of it
      found_bomb = pyautogui.locateOnScreen(bomb[0], confidence=0.95)
      print("Color is " + bomb_color)
      center_of_bomb = pyautogui.center(found_bomb)
      pyautogui.moveTo(center_of_bomb[0], center_of_bomb[1])
    except:
      # Since ImageNotFoundError is raised if no image is on screen and halts program,
      # just catch and handle the error to prevent program crashing
      # (i.e. sometimes there might be no red bombs but that's okay)
      print("Could not find " + bomb_color)
      continue
    
    # These two get black, red respecitvely: bound_tuple[0][1], bound_tuple[1][1]
    
    for bound in bound_tuple:
      # get all the info for both bounds, then look at our current
      # bomb's color, and move the bomb to its respective bound
      bound_pos, bound_color = bound
      bound_x, bound_y = bound_pos
      if bomb_color == bound_color:
        print("Match with " + bomb_color, bound_color, bound_pos)  
        # below is a way to use the "drag" feature but that took too long,
        # and i got better results by just snapping the bomb to the goal
        #pyautogui.dragTo(bound_x, bound_y, button='left', duration=0.45)
        pyautogui.mouseDown(_pause=False)
        sleep(0.05)
        pyautogui.moveTo(bound_x, bound_y)
        sleep(0.05)
        pyautogui.mouseUp(_pause=False)

# Initialize, give time to set up game after running program
for i in range(4,-1,-1):

  print(str(i)+"...")
  sleep(1)

b = setup()
a = 0
while a < 500:
  play_game(b)
  a+=1
