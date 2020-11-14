from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyboardController
import time
import pygame
pygame.init()
Controller = Controller()
keyboard = KeyboardController()
Controller.position = (562, 852)
Controller.press(Button.left)


Controller.release(Button.left)
#Bear_Python_Bot : E



while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == ord('q'):
                break
    Controller.position = (425, 779)
    time.sleep(1.5)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == ord('q'):
                break
    Controller.press(Button.left)
    Controller.release(Button.left)
    Controller.press(Button.right)
    Controller.release(Button.right)
    Controller.position = (440, 760)
    Controller.press(Button.left)
    Controller.release(Button.left)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)



