import os; print (os.getcwd())
import pyautogui
from time import sleep
from PIL import Image

photos_folder = r'/images'

def setup():
  """
  Just open and return the image of the mole target.
  This was the easiest game to program, since it's 
  literally just looking for a single target until
  time runs out.

  Returns: the image of the mole target.
  """

  mole = Image.open(r'./images/MontyMole.png')
  return(mole)

def play_game(mole_pic):
  """
  Every time this is called, just find the mole on the screen,
  move the mouse to it, and then click on it.

  Parameters: The picture of the mole.
  """

  try:
    mole_pos = pyautogui.locateOnScreen(mole_pic, confidence=0.725)
    pyautogui.moveTo(pyautogui.center(mole_pos))
    pyautogui.mouseDown()
    sleep(0.02)
    pyautogui.mouseUp()
  except pyautogui.ImageNotFoundException as INFE:
    print('INFE')


# Initialize, give time to set up game after running program
for i in range(4,-1,-1):

  print(str(i)+"...")
  sleep(1)

b = setup()
a = 0
while a < 200:
  a += 1
  play_game(b)

