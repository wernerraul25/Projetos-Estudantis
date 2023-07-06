import pyautogui

pyautogui.PAUSE = 1

#abrir a ferramenta/o sistema/ o programa
pyautogui.press("win")
pyautogui.write("login.xlsx")
pyautogui.press("backspace")
pyautogui.press("enter")

#preencher o login
pyautogui.click(x=501, y=340)
pyautogui.write("werner")
#preencher a senha
pyautogui.click(x=509, y=395)
pyautogui.write("senhawerner")
#clicar em fazer login
pyautogui.click(x=479, y=526)