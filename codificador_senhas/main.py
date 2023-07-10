master_pwd = input("Qual a senha master? ")



def view():
    pass
def add():
    username = input("Username: ")
    pwd = input("Senha: ")
    platform = input("Plataforma: ")
    try:
        with open("passwords.txt","a") as f:
            f.write(platform + "|" + username + "|" + pwd + "\n")
    except:
        with open("passwords.txt","w") as f:
            f.write(platform + "|" + username + "|" + pwd + "\n")

choose = str(input("Para adicionar senhas:(1)\nPara ver senhas:(2)"))
if choose == "1":
    add()
elif choose == "2":
    view()