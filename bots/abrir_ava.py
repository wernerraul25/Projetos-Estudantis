#chrome -> chromedriver
#firefox -> geckodriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui

username = str(input("Digite seu username: "))
senha = str(input("Digite a senha: "))

navegador = webdriver.Chrome()

navegador.maximize_window()
navegador.get("https://www.atitus.edu.br/")

#fecha o aviso de ser um software de teste automatizado
pyautogui.click(x=1892, y=115)

#clica em minha conta e abre o ava
pyautogui.click(x=1651, y=251)
pyautogui.click(x=1670, y=328)
pyautogui.moveTo(x=1913, y=295)
pyautogui.drag(0,120,1,button='left')
pyautogui.click(x=1424, y=487)

#clica em username e escreve
pyautogui.click(x=1651, y=251)
pyautogui.click(x=1403, y=682)
pyautogui.click(x=867, y=406)
pyautogui.write(username)

#clica em senha e escreve
pyautogui.click(x=903, y=462)
pyautogui.write(senha)

#clica em entrar
pyautogui.click(x=1095, y=535)

#deixa o mouse em cima do 'meus cursos'
pyautogui.moveTo(x=1730, y=130)