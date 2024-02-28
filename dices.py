import random
from tkinter import *


def alternar_desalternar():
    if vantagem_var.get() == 1:
        checkboxdesvantagem["state"] = "disabled"
    else:
        checkboxdesvantagem["state"] = "normal"

    if desvantagem_var.get() == 1:
        checkboxvantagem["state"] = "disabled"
    else:
        checkboxvantagem["state"] = "normal"


def rolar_d20():
    
    if vantagem_var.get() == 1:
        
        numeros_aleatorios20 = random.choices(range(1, 21), k=2)
        texto_resposta_d20["text"] = f"{numeros_aleatorios20[0]} / {numeros_aleatorios20[1]}"
        if 20 in numeros_aleatorios20:
            texto_resposta_d20["foreground"] = "green"
            texto_resposta_d20["text"] = f"{numeros_aleatorios20[0]} / {numeros_aleatorios20[1]}"
        elif numeros_aleatorios20[0] == numeros_aleatorios20[1] == 1:
            texto_resposta_d20["foreground"] = "red"
            texto_resposta_d20["text"] = f"{numeros_aleatorios20[0]} / {numeros_aleatorios20[1]}"
        else:
            texto_resposta_d20["foreground"] = "black"
            texto_resposta_d20["text"] = f"{numeros_aleatorios20[0]} / {numeros_aleatorios20[1]}"
    

    
    else:
        numero_aleatorio20 = random.randint(1, 20)
        texto_resposta_d20["text"] = f"{numero_aleatorio20}"
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
app.geometry("600x500")

texto_d20 = Label(app, text="D20")
texto_d20.grid(column=0, row=0, padx=10, pady=10)

botao_d20 = Button(app, text="Aperte para rolar", command=rolar_d20)
botao_d20.grid(column=0, row=1, padx=10, pady=10)

texto_resposta_d20 = Label(app, text="")
texto_resposta_d20.grid(column=0, row=2, padx=10, pady=10)


texto_d12 = Label(app, text="D12")
texto_d12.grid(column=1, row=0, padx=10, pady=10)

botao_d12 = Button(app, text="Aperte para rolar", command=rolar_d12)
botao_d12.grid(column=1, row=1, padx=10, pady=10)

texto_resposta_d12 = Label(app, text="")
texto_resposta_d12.grid(column=1, row=2, padx=10, pady=10)

texto_d8 = Label(app, text="D8")
texto_d8.grid(column=2, row=0, padx=10, pady=10)

botao_d8 = Button(app, text="Aperte para rolar", command=rolar_d8)
botao_d8.grid(column=2, row=1, padx=10, pady=10)

texto_resposta_d8 = Label(app, text="")
texto_resposta_d8.grid(column=2, row=2, padx=10, pady=10)

texto_d6 = Label(app, text="D6")
texto_d6.grid(column=3, row=0, padx=10, pady=10)

botao_d6 = Button(app, text="Aperte para rolar", command=rolar_d6)
botao_d6.grid(column=3, row=1, padx=10, pady=10)

texto_resposta_d6 = Label(app, text="")
texto_resposta_d6.grid(column=3, row=2, padx=10, pady=10)

texto_d4 = Label(app, text="D4")
texto_d4.grid(column=4, row=0, padx=10, pady=10)

botao_d4 = Button(app, text="Aperte para rolar", command=rolar_d4)
botao_d4.grid(column=4, row=1, padx=10, pady=10)

texto_resposta_d4 = Label(app, text="")
texto_resposta_d4.grid(column=4, row=2, padx=10, pady=10)

vantagem_var = IntVar()
desvantagem_var = IntVar()


checkboxvantagem=Checkbutton(app, text="Vantagem", onvalue=1,variable=vantagem_var, offvalue=0,command=alternar_desalternar)
checkboxvantagem.grid(column=0,row=5,padx=10,pady=10)

checkboxdesvantagem=Checkbutton(app, text="Desvantagem",variable=desvantagem_var, onvalue=1, offvalue=0, command=alternar_desalternar)
checkboxdesvantagem.grid(column=4,row=5,padx=10,pady=10)




app.mainloop()