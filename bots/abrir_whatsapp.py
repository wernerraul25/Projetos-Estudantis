#Abre o Whatsapp e manda mensagem pra quem desejar
import pyautogui

nome = str(input("Digite o nome de quem gostaria de mandar mensagem: "))

pyautogui.PAUSE = 2

pyautogui.press('win')
pyautogui.write('whatsapp')
pyautogui.press('backspace')
pyautogui.press('enter')
pyautogui.click(x=213, y=151)
pyautogui.write(nome)
pyautogui.click(x=214, y=221)
pyautogui.click(x=747, y=994)
pyautogui.write('Boa tarde, sou um bot desenvolvido por Raul Werner')
#pyautogui.press('enter')