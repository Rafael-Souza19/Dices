import random
from tkinter import *
import tkinter.ttk as ttk


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
        checkboxdesvantagem["state"] = "disabled"
    else:
        checkboxdesvantagem["state"] = "normal"

    if desvantagem_var.get() == 1:
        checkboxvantagem["state"] = "disabled"
    else:
        checkboxvantagem["state"] = "normal"

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
    
    if desvantagem_var.get() == 1:
            numeros_aleatorios20 = random.choices(range(1, 21))
            numeros_aleatorios201 = random.choices(range(1, 21))

            if numeros_aleatorios20[0] != numeros_aleatorios201[0]:
                if numeros_aleatorios20[0] < numeros_aleatorios201[0]:
                    numeros_aleatorios20[0] = f"[{numeros_aleatorios20[0]}]"
                else:
                    numeros_aleatorios201[0] = f"[{numeros_aleatorios201[0]}]"
                
                texto_resposta_d20["text"] = f"{numeros_aleatorios20[0]} / {numeros_aleatorios201[0]}"
            else: 
                texto_resposta_d20["text"] = f"{numeros_aleatorios20[0]} / {numeros_aleatorios201[0]}"


    elif vantagem_var.get() == 1:
        
        numeros_aleatorios20 = random.choices(range(1, 21))
        numeros_aleatorios201 = random.choices(range(1, 21))

        if numeros_aleatorios20[0] != numeros_aleatorios201[0]:
            if numeros_aleatorios20[0] > numeros_aleatorios201[0]:
                numeros_aleatorios20[0] = f"[{numeros_aleatorios20[0]}]"
            else:
                numeros_aleatorios201[0] = f"[{numeros_aleatorios201[0]}]"
                
            texto_resposta_d20["text"] = f"{numeros_aleatorios20[0]} / {numeros_aleatorios201[0]}"
        else: 
            texto_resposta_d20["text"] = f"{numeros_aleatorios20[0]} / {numeros_aleatorios201[0]}"

        if 20 in numeros_aleatorios20[0] or 20 in numeros_aleatorios201[0]:
            texto_resposta_d20["foreground"] = "green"
        elif numeros_aleatorios20[0] == numeros_aleatorios201[0] == 1:
            texto_resposta_d20["foreground"] = "red"
        else:
            texto_resposta_d20["foreground"] = "black"
    

    
    else:
        numero_aleatorio20 = random.randint(1, 20)
        if bonus_valor and bonus_var.get() == 1:
            resposta=numero_aleatorio20 + int(bonus_valor)

            texto_resposta_d20["text"] = f"{resposta}"
            Tooltip(texto_resposta_d20,f"{numero_aleatorio20} + {bonus_valor} = {resposta}")

        else: texto_resposta_d20["text"] =f"{numero_aleatorio20}"
        if numero_aleatorio20 == 20:
            texto_resposta_d20["fg"] = "green"
        elif numero_aleatorio20 == 1:
            texto_resposta_d20["fg"] = "red"
        else:
            texto_resposta_d20["fg"] = "black"
       

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


app = Tk()

app.title("Sistema de Dados")
app.geometry("700x500")



texto_d20 = Label(app, text="D20")
texto_d20.grid(column=0, row=2, padx=10, pady=10)

botao_d20 = Button(app, text="Aperte para rolar", command=rolar_d20)
botao_d20.grid(column=0, row=3, padx=10, pady=10)

texto_resposta_d20 = Label(app, text="")
texto_resposta_d20.grid(column=0, row=4, padx=10, pady=10)


texto_d12 = Label(app, text="D12")
texto_d12.grid(column=1, row=2, padx=10, pady=10)

botao_d12 = Button(app, text="Aperte para rolar", command=rolar_d12)
botao_d12.grid(column=1, row=3, padx=10, pady=10)

texto_resposta_d12 = Label(app, text="")
texto_resposta_d12.grid(column=1, row=4, padx=10, pady=10)

texto_d8 = Label(app, text="D8")
texto_d8.grid(column=2, row=2, padx=10, pady=10)

botao_d8 = Button(app, text="Aperte para rolar", command=rolar_d8)
botao_d8.grid(column=2, row=3, padx=10, pady=10)

texto_resposta_d8 = Label(app, text="")
texto_resposta_d8.grid(column=2, row=4, padx=10, pady=10)

texto_d6 = Label(app, text="D6")
texto_d6.grid(column=3, row=2, padx=10, pady=10)

botao_d6 = Button(app, text="Aperte para rolar", command=rolar_d6)
botao_d6.grid(column=3, row=3, padx=10, pady=10)

texto_resposta_d6 = Label(app, text="")
texto_resposta_d6.grid(column=3, row=4, padx=10, pady=10)

texto_d4 = Label(app, text="D4")
texto_d4.grid(column=4, row=2, padx=10, pady=10)

botao_d4 = Button(app, text="Aperte para rolar", command=rolar_d4)
botao_d4.grid(column=4, row=3, padx=10, pady=10)

texto_resposta_d4 = Label(app, text="")
texto_resposta_d4.grid(column=4, row=4, padx=10, pady=10)

vantagem_var = IntVar()
desvantagem_var = IntVar()
bonus_var = IntVar()
bonus_valor = 0




checkboxvantagem=Checkbutton(app, text="Vantagem", onvalue=1,variable=vantagem_var, offvalue=0,command=alternar_desalternar)
checkboxvantagem.grid(column=0,row=1,padx=10,pady=10)

checkboxdesvantagem=Checkbutton(app, text="Desvantagem",variable=desvantagem_var, onvalue=1, offvalue=0, command=alternar_desalternar)
checkboxdesvantagem.grid(column=1,row=1,padx=10,pady=10)


checkboxbonusd20 = Checkbutton(app, text="Bonus", onvalue=1, offvalue=0, command=alternar_desalternar, variable=bonus_var)
checkboxbonusd20.grid(column=0, row=7, padx=10, pady=10)

vcmd = app.register(on_validate)

textobonus = Entry(app, state="disabled", validate="key", validatecommand=(vcmd, '%P'))
textobonus.grid(column=0, row=8, padx=10, pady=10)

botao_armazenar = Button(app, text="Adicionar bônus", command=armazenar_bonus)
botao_armazenar.grid(column=1, row=8, padx=10, pady=10)

botao_remover= Button(app, text="Remover bônus", command=remover_bonus)
botao_remover.grid(column=1, row=9, padx=10, pady=10)


app.mainloop()
