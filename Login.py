#Importar tkinter e armazenar na varaiavel "root"
from tkinter import *
root = Tk()

#Funcao para indicar sucesso do cadastro
def getvals():
    print("Cadastro realizado!")

#Definir o tamanho da janela (Height and width)
root.geometry("500x300")

#Definindo "Label" com titulo, fonte e localizacao
Label(root, text="Se registre aqui!", font="ar 15 bold").grid(row=0,column=3)

#Definindo variaveis e seu parametros
name=Label(root, text="Nome")
phone=Label(root, text="Telefone")
gender=Label(root, text="Genero")
emergency=Label(root, text="Emergencia")
paymentmood=Label(root, text="Pagamento")

#Localizcao da variavel na janela
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmood.grid(row=5,column=2)

#Novas variaveis para armazenar os valores
namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
emergencyvalue=StringVar
paymentmoodvalue=StringVar
checkvalue=IntVar

#Variaveis de entrada e definindo onde vao ser armazenadas
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymentmoodentry=Entry(root,textvariable=paymentmoodvalue)

#Localizacao das variaveis de entrada na janela
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmoodentry.grid(row=5,column=3)

#Butao para lembrar das infos
checkbtn=Checkbutton(text="Lembrar de mim?",variable=checkvalue)
checkbtn.grid(row=6,column=3)

#Butao para enviar os dados
Button(text="Enviar", command=getvals).grid(row=7,column=3)








root.mainloop()