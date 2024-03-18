import random
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk, ImageFilter



class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = Label(self.tooltip, text=self.text, justify='left', background="#ffffe0", relief='solid', borderwidth=1)
        label.pack(ipadx=1)

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

def alternar_desalternar():
    if vantagem_var.get() == 1:
        checkbox_desvantagem["state"] = "disabled"
    else:
        checkbox_desvantagem["state"] = "normal"

    if desvantagem_var.get() == 1:
        checkbox_vantagem["state"] = "disabled"
    else:
        checkbox_vantagem["state"] = "normal"

    if bonus_var.get()== 1:
        textobonus["state"] ="normal"
    else: textobonus["state"] = "disabled"

def on_validate(P):
    return P.isdigit() and len(P) <= 2 or P == ""

def armazenar_bonus():
    global bonus_valor
    bonus_valor = textobonus.get()

def mostrar_soma():
    resultado = texto_resposta_d20["text"]
    bonus_soma = int(bonus_valor) if bonus_valor else 0
    total_soma = int(resultado.split('/')[0]) + bonus_soma
    tooltip = Tooltip(texto_resposta_d20, f"Soma: {total_soma}")

def remover_bonus():
    textobonus.delete(0, END)
    global bonus_valor
    bonus_valor = 0
def rolar_d20():
    
    #ROLL NORMAL, COM BONUS OU SEM
    numero_aleatorio20 = random.randint(1, 20)
    if bonus_valor and bonus_var.get() == 1:
            resposta=numero_aleatorio20 + int(bonus_valor)

            texto_resposta_d20["text"] = f"{resposta}"
            Tooltip(texto_resposta_d20,f"{numero_aleatorio20} + {bonus_valor} = {resposta}")

    else: texto_resposta_d20["text"] =f"{numero_aleatorio20}"
    
 

    #ROLL COM DESVANTAGEM, COM BONUS OU SEM
    if desvantagem_var.get() == 1:
        des_numeros_aleatorios20 = random.choices(range(1, 21))
        des_numeros_aleatorios201 = random.choices(range(1, 21))
        roll1 = des_numeros_aleatorios20[0]
        roll2 = des_numeros_aleatorios201[0]

        if bonus_valor and bonus_var.get() == 1: 
            resposta=roll1+ int(bonus_valor)
            resposta2= roll2 +int(bonus_valor)
            if resposta != resposta2:
                if resposta< resposta2:
                    resposta= f"[{resposta}]"
                else: resposta2= f"[{resposta2}]"
            texto_resposta_d20["text"] = f"{resposta} / {resposta2}"

            Tooltip(texto_resposta_d20,f"{roll1} + {bonus_valor} = {resposta}\n{roll2} + {bonus_valor} = {resposta2}" )
            
        

        elif roll1 != roll2:
            if roll1< roll2:
                roll1= f"[{roll1}]"
            else: roll2=f"[{roll2}]"
            texto_resposta_d20["text"] = f"{roll1} / {roll2}"


    #ROLL COM VANTAGEM, COM BONUS OU SEM
    if vantagem_var.get() == 1:
        
        van_numeros_aleatorios20 = random.choices(range(1, 21))
        van_numeros_aleatorios201 = random.choices(range(1, 21))
        roll1 = van_numeros_aleatorios20[0]
        roll2 = van_numeros_aleatorios201[0]

        if bonus_valor and bonus_var.get() == 1:
            resposta = roll1 + int(bonus_valor)
            resposta2 = roll2 + int(bonus_valor)
        else:
            resposta = roll1
            resposta2 = roll2
        if resposta != resposta2:
            if resposta> resposta2:
                resposta= f"[{resposta}]"
            else: resposta2= f"[{resposta2}]"
        texto_resposta_d20["text"] = f"{resposta} / {resposta2}"

        Tooltip(texto_resposta_d20,f"{roll1} + {bonus_valor} = {resposta}\n{roll2} + {bonus_valor} = {resposta2}" )
            
        


        
       

def rolar_d8():
    numero_aleatorio8 = random.randint(1, 8)
    texto_resposta_d8["text"] = f"{numero_aleatorio8}"

def rolar_d6():
    numero_aleatorio6 = random.randint(1, 6)
    texto_resposta_d6["text"] = f"{numero_aleatorio6}"

def rolar_d12():
    numero_aleatorio12 = random.randint(1, 12)
    texto_resposta_d12["text"] = f"{numero_aleatorio12}"

def rolar_d4():
    numero_aleatorio4 = random.randint(1, 4)
    texto_resposta_d4["text"] = f"{numero_aleatorio4}"


#INTERFACE
app = Tk()

app.title("Dices")
app.geometry("700x500")

imagem_icone = Image.open("d20.png")
icone_app = ImageTk.PhotoImage(imagem_icone)

app.iconphoto(False, icone_app)

frame = Frame(app, bg="white", bd=5, relief="ridge")
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.75, anchor="n")

# Adiciona um título
title_label = Label(frame, text="Dados", bg="white", font=("Arial", 16))
title_label.pack(fill="x", pady=10)

# Adiciona um frame para os botões e textos de resposta
buttons_frame = Frame(frame, bg="white")
buttons_frame.pack(pady=20)

# Botões e textos de resposta para D20
botao_d20 = Button(buttons_frame, text="D20", bg="lightblue", font=("Arial", 12), relief="raised", padx=20, pady=10, command=rolar_d20)
botao_d20.grid(row=0, column=0, padx=10)
texto_resposta_d20 = Label(buttons_frame, text="", font=("Arial", 14, "bold"), bg="lightblue", relief="solid")
texto_resposta_d20.grid(row=1, column=0, padx=10, pady=10)

# Botões e textos de resposta para D12
botao_d12 = Button(buttons_frame, text="D12", bg="lightgreen", font=("Arial", 12), relief="raised", padx=20, pady=10, command=rolar_d12)
botao_d12.grid(row=0, column=1, padx=10)
texto_resposta_d12 = Label(buttons_frame, text="", font=("Arial", 14, "bold"), bg="lightgreen", relief="solid")
texto_resposta_d12.grid(row=1, column=1, padx=10, pady=10)

# Botões e textos de resposta para D8
botao_d8 = Button(buttons_frame, text="D8", bg="lightpink", font=("Arial", 12), relief="raised", padx=20, pady=10, command=rolar_d8)
botao_d8.grid(row=0, column=2, padx=10)
texto_resposta_d8 = Label(buttons_frame, text="", font=("Arial", 14, "bold"), bg="lightpink", relief="solid")
texto_resposta_d8.grid(row=1, column=2, padx=10, pady=10)

# Botões e textos de resposta para D6
botao_d6 = Button(buttons_frame, text="D6", bg="lightyellow", font=("Arial", 12), relief="raised", padx=20, pady=10, command=rolar_d6)
botao_d6.grid(row=0, column=3, padx=10)
texto_resposta_d6 = Label(buttons_frame, text="", font=("Arial", 14, "bold"), bg="lightyellow", relief="solid")
texto_resposta_d6.grid(row=1, column=3, padx=10, pady=10)

# Botões e textos de resposta para D4
botao_d4 = Button(buttons_frame, text="D4", bg="lightcoral", font=("Arial", 12), relief="raised", padx=20, pady=10, command=rolar_d4)
botao_d4.grid(row=0, column=4, padx=10)
texto_resposta_d4 = Label(buttons_frame, text="", font=("Arial", 14, "bold"), bg="lightcoral", relief="solid")
texto_resposta_d4.grid(row=1, column=4, padx=10, pady=10)

vantagem_var = IntVar()
desvantagem_var = IntVar()
bonus_var = IntVar()
bonus_valor = 0




vantagem_var = IntVar()
checkbox_vantagem = Checkbutton(frame, text="Vantagem", variable=vantagem_var, bg="white", font=("Arial", 12), command=alternar_desalternar)
checkbox_vantagem.pack()

# Checkbox desvantagem
desvantagem_var = IntVar()
checkbox_desvantagem = Checkbutton(frame, text="Desvantagem", variable=desvantagem_var, bg="white", font=("Arial", 12), command=alternar_desalternar)
checkbox_desvantagem.pack()

# Checkbox bônus
bonus_var = IntVar()
checkbox_bonus = Checkbutton(frame, text="Bônus", variable=bonus_var, bg="white", font=("Arial", 12), command=alternar_desalternar)
checkbox_bonus.pack()

# Entry do bônus
textobonus = Entry(frame, state="disabled", validate="key", validatecommand=(app.register(on_validate), '%P'))
textobonus.pack()

# Botões de armazenar e remover bônus
botao_armazenar = Button(frame, text="Adicionar Bônus", command=armazenar_bonus)
botao_armazenar.pack(pady=5)

botao_remover = Button(frame, text="Remover Bônus", command=remover_bonus)
botao_remover.pack(pady=5)

vcmd = app.register(on_validate)



app.mainloop()
