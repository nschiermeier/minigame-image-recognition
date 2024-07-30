import os; print (os.getcwd())
from pyautogui import locateOnScreen, locateAllOnScreen, center, moveTo, press, keyDown, keyUp, ImageNotFoundException
from time import sleep
from PIL import Image

photos_folder = r'/images'
# region is (left_most_pixel, top_most_pixel, width, height)
#region = (1150, 740, 250, 250)
region = (1290, 800, 55, 55)
buttons = []
hotkeys = ['L', 'K', 'I', 'J'] # hotkeys for DS emu in order of A, B, X, Y

def setup():
  a_button = Image.open(r'./images/de_a2.png')
  b_button = Image.open(r'./images/de_b2.png')
  x_button = Image.open(r'./images/de_x2.png')
  y_button = Image.open(r'./images/de_y2.png')

  buttons.extend([a_button, b_button, x_button, y_button])
  # Create dictioanry that maps hotkeys to their button
  button_map = {hotkeys[i]: buttons[i] for i in range(len(hotkeys))}
  return button_map

def play_game(button_list):
  # Do stuff here idk
  #print(button_list)
  for button_img in button_list:
    try:
      loc = locateOnScreen(button_list[button_img], confidence=0.845, region=region, grayscale=True)
      keyDown(button_img)
      sleep(0.02)
      keyUp(button_img)
      print(f"Found {button_img}!")
      break
    except ImageNotFoundException:
      print(f"Could not find {button_img}.")

# Initialize, give time to set up game after running program
for i in range(4,-1,-1):

  print(str(i)+"...")
  sleep(1)

b = setup()
a = 0
while a < 100:
  play_game(b)
  a+=1
