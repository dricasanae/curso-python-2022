from tkinter import*

class Tela:
   
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.titulo = Label(self.container1, text = "Login do Sistema")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        
        self.container2 = Frame(master)
        self.container2["pady"] = 10
        self.container2.pack()
        
        self.lbl_nome =Label(self.container2, text = "Usuário: ")
        self.lbl_nome["font"] = ("Arial", "10", "bold")
        self.lbl_nome.pack(side=LEFT)

        self.txt_nome = Entry(self.container2)
        self.txt_nome["width"] = 30
        self.txt_nome["font"] = ("Arial", "10", "bold")
        self.txt_nome.pack(side=LEFT)

        self.container3 = Frame(master)
        self.container3["pady"] = 10
        self.container3.pack()

        self.lbl_senha =Label(self.container3, text = "Senha: ")
        self.lbl_senha["font"] = ("Arial", "10", "bold")
        self.lbl_senha.pack(side=LEFT)

        self.txt_senha = Entry(self.container3)
        self.txt_senha["width"] = 30
        self.txt_senha["show"] = "*"
        self.txt_senha["font"] = ("Arial", "10", "bold")
        self.txt_senha.pack(side=LEFT)

        self.container4 = Frame(master)
        self.container4["pady"] = 10
        self.container4.pack()

        self.btn_login = Button(self.container4)
        self.btn_login["text"] = "LOGIN"
        self.btn_login["font"] = ("Calibri", "10")
        self.btn_login["width"] = 10
        self.btn_login["command"] = self.login
        self.btn_login.pack (side = LEFT)

        self.btn_sair = Button(self.container4)
        self.btn_sair["text"] = "SAIR"
        self.btn_sair["font"] = ("Calibri", "10")
        self.btn_sair["width"] = 10
        self.btn_sair["command"] = self.container4.quit
        self.btn_sair.pack (side = LEFT)

        self.container5 = Frame(master)
        self.container5["pady"] = 10
        self.container5.pack()

        self.lbl_resultado = Label(self.container5, text = "")
        self.lbl_resultado["font"] = ("Arial", "10", "bold")
        self.lbl_resultado.pack()

    def login(self):
        nome = (self.txt_nome.get())
        senha = (self.txt_senha.get())
        if nome != senha:
            self.lbl_resultado["text"] = f"Bem-vind@ ao sistema!"
        else:
            self.lbl_resultado["text"] = f"Usuário Inválido!"

root = Tk()
Tela(root)
root.mainloop()