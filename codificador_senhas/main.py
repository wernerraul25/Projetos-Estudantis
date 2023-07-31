import os
from cryptography.fernet import Fernet

senha_master = "Master852."

input_senha_master = str(input("Digite a senha master: "))
if input_senha_master == senha_master:
    def clear_terminal():
        os.system("cls")

    '''def write_key():
        key = Fernet.generate_key()
        with open("key.key","wb") as key_file:
            key_file.write(key)'''

    def load_key():
        file = open("key.key","rb")
        key = file.read()
        file.close()
        return key

    clear_terminal()
    #master_pwd = input("Qual a senha master? ")
    key = load_key() #+ master_pwd.encode()
    fer = Fernet(key)

    def view():
        with open("passwords.txt","r") as f:
            for line in f.readlines():
                data = line.rstrip()
                plat, user, passw = data.split("|")
                print("Username:", user, "| Senha:", fer.decrypt(passw.encode()).decode(), "| Plataforma:", plat)

    def add():
        username = input("Username: ")
        pwd = input("Senha: ")
        platform = input("Plataforma: ")

        with open("passwords.txt","a") as f:
            f.write(platform + "|" + username + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

    while True:
        clear_terminal()
        choose = str(input("Para adicionar senhas:(add)\nPara ver senhas:(view)\nSair:(q)\n")).lower()
        if choose == "q":
            break
        if choose == "add":
            add()
        elif choose == "view":
            view()
            input("Pressione qualquer tecla para continuar!")
else:
    print("A senha está incorreta!\nReinicie o programa e tente novamente.")