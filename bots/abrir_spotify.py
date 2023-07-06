#abre o Spotify e da play na música
import pyautogui

pyautogui.PAUSE = 2

pyautogui.press('win')
pyautogui.write('Spotify')
pyautogui.press('enter')
pyautogui.click(x=969, y=949)