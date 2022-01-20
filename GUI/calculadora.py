from doctest import master
from tkinter import*

class Tela:
   
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.titulo = Label(self.container1, text = "Calculadora")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        
        self.container2 = Frame(master)
        #PADY para dar espaço nos container
        self.container2["pady"] = 10
        self.container2.pack()
        
        self.lbl_num1 =Label(self.container2, text = "Número 1: ")
        self.lbl_num1["font"] = ("Arial", "10", "bold")
        self.lbl_num1.pack(side=LEFT)

        self.txt_num1 = Entry(self.container2)
        self.txt_num1["width"] = 30
        self.txt_num1["font"] = ("Arial", "10", "bold")
        self.txt_num1.pack(side=LEFT)

        self.lbl_num2 =Label(self.container2, text = "Número 2: ")
        self.lbl_num2["font"] = ("Arial", "10", "bold")
        self.lbl_num2.pack(side=LEFT)

        self.txt_num2 = Entry(self.container2)
        self.txt_num2["width"] = 30
        self.txt_num2["font"] = ("Arial", "10", "bold")
        self.txt_num2.pack(side=LEFT)

        self.container3 = Frame(master)
        self.container3["pady"] = 10
        self.container3.pack()

        self.btn_soma = Button(self.container3)
        self.btn_soma["text"] = "+"
        self.btn_soma["font"] = ("Calibri", "10")
        self.btn_soma["width"] = 5
        self.btn_soma["command"] = self.soma
        self.btn_soma.pack ()

        self.container4 = Frame(master)
        self.container4["pady"] = 10
        self.container4.pack()

        self.lbl_resultado = Label(self.container4, text = "")
        self.lbl_resultado["font"] = ("Arial", "10", "bold")
        self.lbl_resultado.pack()

        self.container5 = Frame(master)
        self.container5["pady"] = 10
        self.container5.pack()

        self.btn_sub = Button(self.container5)
        self.btn_sub["text"] = "-"
        self.btn_sub["font"] = ("Calibri", "10")
        self.btn_sub["width"] = 5
        self.btn_sub["command"] = self.sub
        self.btn_sub.pack()
        
        self.container6 = Frame(master)
        self.container6["pady"] = 10
        self.container6.pack()

        self.lbl_resultados = Label(self.container6, text = "")
        self.lbl_resultados["font"] = ("Arial", "10", "bold")
        self.lbl_resultados.pack()
       
        self.container7 = Frame(master)
        self.container7["pady"] = 10
        self.container7.pack()

        self.btn_mult = Button(self.container7)
        self.btn_mult["text"] = "x"
        self.btn_mult["font"] = ("Calibri", "10")
        self.btn_mult["width"] = 5
        self.btn_mult["command"] = self.mult
        self.btn_mult.pack()
        
        self.container8 = Frame(master)
        self.container8["pady"] = 10
        self.container8.pack()

        self.lbl_resultadom = Label(self.container8, text = "")
        self.lbl_resultadom["font"] = ("Arial", "10", "bold")
        self.lbl_resultadom.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 10
        self.container9.pack()

        self.btn_div = Button(self.container9)
        self.btn_div["text"] = "/"
        self.btn_div["font"] = ("Calibri", "10")
        self.btn_div["width"] = 5
        self.btn_div["command"] = self.div
        self.btn_div.pack()
        
        self.container9 = Frame(master)
        self.container9["pady"] = 10
        self.container9.pack()

        self.lbl_resultadod = Label(self.container9, text = "")
        self.lbl_resultadod["font"] = ("Arial", "10", "bold")
        self.lbl_resultadod.pack()

    def soma(self):
        num1 = float(self.txt_num1.get())
        num2 = float(self.txt_num2.get())
        soma = num1 +num2
        self.lbl_resultado["text"] = f"{num1} + {num2} = {soma}"

    def sub(self):
        num1 = float(self.txt_num1.get())
        num2 = float(self.txt_num2.get())
        sub = num1 - num2
        self.lbl_resultados["text"] = f"{num1} - {num2} = {sub}"
    
    def mult(self):
        num1 = float(self.txt_num1.get())
        num2 = float(self.txt_num2.get())
        mult = num1 * num2
        self.lbl_resultadom["text"] = f"{num1} x {num2} = {mult}"
    
    def div(self):
        num1 = float(self.txt_num1.get())
        num2 = float(self.txt_num2.get())
        if num2 != 0:
            div = num1 / num2
            self.lbl_resultadod["text"] = f"{num1} / {num2} = {div}"
        else:
            self.lbl_resultadod["text"] = f"Não é possível fazer divisão por zero"
    

root = Tk()
Tela(root)
root.mainloop()