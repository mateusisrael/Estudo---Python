import tkinter as tk

janela = tk.Tk()
janela.title("CALCULADORA")
janela.geometry("700x400")

#-----Label---------
label1 = tk.Label(text="CALCULADORA", font=20)
label1.grid(column=0, row=0)



#----Entradas-------
entry1 = tk.Entry()
entry1.grid(column=0, row=1)

#----Button---------
button1 = tk.Button(text="Clique aqui")
button1.grid(column=1, row=1)

janela.mainloop()
