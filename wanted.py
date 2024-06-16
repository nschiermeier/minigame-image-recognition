import os
import pyautogui
from time import sleep
from PIL import Image

photos_folder = r'/images'
face_posters = []
wanted_face = ''

def setup():
  """
  Sets up the game by creating all pairs of faces and their posters,
  then returns them all in an array
  
  Returns: an array of the images of each face.
  """

  mario_face = Image.open(r'./images/MarioFace.png')
  mario_poster = Image.open(r'./images/MarioPoster.png')
  mario = (mario_face, mario_poster, "mario")

  luigi_face = Image.open(r'./images/LuigiFace.png')
  luigi_poster = Image.open(r'./images/LuigiPoster.png')
  luigi = (luigi_face, luigi_poster, "luigi")
  
  wario_face = Image.open(r'./images/WarioFace.png')
  wario_poster = Image.open(r'./images/WarioPoster.png')
  wario = (wario_face, wario_poster, "wario")

  yoshi_face = Image.open(r'./images/YoshiFace.png')
  yoshi_poster = Image.open(r'./images/YoshiPoster.png')
  yoshi = (yoshi_face, yoshi_poster, "yoshi")

  face_posters.extend([mario, luigi, wario, yoshi])
  return face_posters

def play_game(face_poster_array):
  """
  Plays the game by selecting whichever face matches most closely to
  the one on the top of the screen.

  Parameters: an array with the images of all the faces
  """
  finding = 0
  for character in face_poster_array:
    #Instead of highest confidence, loop through them all but just have confidence
    #set high enough to not get false positives?
    try:
      curr_character = pyautogui.locateOnScreen(character[1], confidence=0.8)
    except:
      print(f"Could not find {character[2]}")
      continue
    print(character[2])
    while(finding<15):
      finding+=1
      try:
        small_character = pyautogui.locateOnScreen(character[0], confidence=0.75, region=(800, 520, 312, 220))
        center = pyautogui.center(small_character)
        pyautogui.moveTo(center)
        sleep(0.04)
        pyautogui.mouseDown()
        sleep(0.04)
        pyautogui.mouseUp()
      except:
        print('')


face_poster_pairs = setup()
a = 0
while (a < 100):

  play_game(face_poster_pairs)
  a+=1
