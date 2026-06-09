import tkinter as tk

#variáveis:
seg = 0
min = 0
hrs = 0

rodando = True

#Janela:
janela = tk.Tk() #cria a janela
janela.geometry("400x200") #tamanho da janela

#Contador:
"""janela.after(tempo em ms, fumção)-> executa uma função depois de tantos ms"""

def atualizar():
    global seg, min, hrs

    if rodando:
        seg += 1 #aumenta o tempo
        if seg == 60:
            seg = 0
            min +=1
        if min == 60:
            min = 0
            hrs += 1

        label.config(text = f"{hrs:02}:{min:02}:{seg:02}") #atualiza na tela / :02 faz o valor ter dois dígitos

    janela.after(1000, atualizar)#1000ms=1s, a cada 1s executa a função atualizar

#Pausar:
def pausar():
    global rodando
    rodando = not rodando

#Botão:
botao = tk.Button(janela, text = "Pausar / Continuar", command = pausar)
botao.pack()

#Resetar:
def reset():
    global seg, min, hrs
    seg = 0
    min = 0
    hrs = 0

    label.config(text = "00:00:00")

bttreset = tk.Button(janela, text = "Reset", command = reset)
bttreset.pack()

#Texto:
label = tk.Label(janela, text = "00:00:00")
label.pack()#faz o texto aparecer

atualizar() # inicia o processo enuanto o after(...) mantém ele rodando
janela.mainloop() #mantém a janela aberta