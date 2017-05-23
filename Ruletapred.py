import random

ČRNA={2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}
RDEČA={1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}



def zavrti():
    ''' Funkcija zavrti zavrti kolo in nam pove katera številka je padla.
        Vrne nam seznam ki nam pove [barvo,število,stolpec,tretino,polovico,sodost]
        številke ki je padla'''
    število=random.randint(0,36)
    if 0 < število <= 18:
        polovica = 1
    elif 18 < število <= 36:
        polovica = 2
    else:
        polovica = 0
    if število % 2 == 0:
        sodost = 'Soda'
    else:
        sodost = 'Liha'
    if 0 < število <= 12:
        tretina = 1
    elif 13 <= število <= 24:
        tretina = 2
    elif 25 <= število <= 36:
        tretina = 3
    else:
        tretina = 0
    if število == 0:
        stolpec = 0
    elif število % 3 == 0:
        stolpec = 3
    elif število in range(2,35,3):
        stolpec = 2
    else:
        stolpec = 1
    if število == 0:
        print (število)
        return ['ZELENA',število,stolpec,tretina,polovica,sodost]
    elif število in ČRNA:
        print (število)
        return ['ČRNA',število,stolpec,tretina,polovica,sodost]
    else:
        print (število)
        return ['RDEČA',število,stolpec,tretina,polovica,sodost]

število=0

def preverjanje_stave():
    global število
    vrtljaj=zavrti()
    število=0
    število += vrtljaj[1]
    Karton=[]
    for Stava, Cifra in zip(Vrsta_stave,vrtljaj):
        if Stava == Cifra:
            Karton += [1]
        else:
            Karton += [0]
    print (Karton)
    print (Vrsta_stave)
    return Karton


            
def izplačilo():
    izplačilo = 0
    pravilno = []
    množitelj_zadetkov = [2,36,3,3,2,2]
    '''Funkcija nam pove koliko smo zaslužili oziroma izgubili pri vrtenju rulete'''
    for Denar,Stava in zip(Stavljena_vsota,preverjanje_stave()):
        pravilno += [Denar * Stava]
    for Zadetek,Množitelj in zip(pravilno,množitelj_zadetkov):
        izplačilo += Zadetek*Množitelj
    return izplačilo

 





#---------------------------------------TKINTER--------------------------------------------------

import tkinter as tk	
from tkinter import *

master= tk.Tk()
master.title('Ruleta')
master.configure(bg='dark green')

image = tk.PhotoImage(file='//Users//Jan//Documents//4.gif')
label = tk.Label(image=image,compound=CENTER)
label.pack(side='right')
label.grid(row=0, column=4,sticky=W,rowspan = 6)

Denarnica=0

def igraj():
    global Denarnica
    global tisk
    premoženje=('Na voljo imate: ', Denarnica,' evrov.')
    
    if Denarnica > 0 :
        if Denarnica >= sum(Stavljena_vsota):
            Denarnica -= sum(Stavljena_vsota)
            i = izplačilo()
            Denarnica += i
            Label(master, text=('Zadeli ste '+ str(i)+' evrov.'+'Vložili pa ste '+str(sum(Stavljena_vsota))+'evrov'),bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=8,column=4)
            posodobi_stanje()
            padla_je()
            return Denarnica
            
        else:
            Label(master, text='Za tako stavo nimate dovolj denarja, kupite nove žetone ali pa spremenite stavo',bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=8,column=4)
    
    else:
        Label(master, text='Nimate več denarja, kupite nove žetone',bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=8,column=4)
 
def start():
    global Vrsta_stave
    global Stavljena_vsota
    Vrsta_stave=  [var1.get(), int(e2.get()), int(var3.get()), int(var4.get()), int(var5.get()), var6.get()]
    Stavljena_vsota= [int(e7.get()), int(e8.get()), int(e9.get()), int(e10.get()), int(e11.get()), int(e12.get())]
    igraj()
    

def padla_je():
    global število
    Label(master, text=('Padla je številka '+str(število)),bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=7,column=4)


def menjaj():
    global Denarnica
    Denarnica += int(e13.get())
    posodobi_stanje()
    
def posodobi_stanje():
    global Denarnica
    premoženje= ('Na voljo imate: '+ str(Denarnica) +' evrov.')
    Label(master, text=premoženje,bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=6,column=4)
   

   

global tisk
Label(master, text="Barva",bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=0)
Label(master, text="Število",bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=1)
Label(master, text="Stolpec",bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=2)
Label(master, text="Tretina",bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=3)
Label(master, text="Polovica",bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=4)
Label(master, text="Sodost",bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=5)
Label(master, text="Stava",bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=0, column=2)
Label(master, text="Stava",bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=1, column=2)
Label(master, text="Stava",bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=2, column=2)
Label(master, text="Stava",bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=3, column=2)
Label(master, text="Stava",bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=4, column=2)
Label(master, text="Stava",bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=5, column=2)
Label(master, text="Menjaj za žetone",bg='dark green',font = "Verdana 13 bold",fg='white').grid(row=6)



var1 = StringVar(master)
var1.set("0")
option1 = OptionMenu(master, var1, "0", "RDEČA", "ČRNA")
option1.pack()
option1.config(width=10,bg='dark green')

e2 = Entry(master)
e2.config(width=10,bg='green4',fg='white',highlightbackground='black')

var3 = StringVar(master)
var3.set("0")
option3 = OptionMenu(master, var3, "0", "1", "2","3")
option3.pack()
option3.config(width=10,bg='dark green')

var4 = StringVar(master)
var4.set("0")
option4 = OptionMenu(master, var4, "0", "1", "2","3")
option4.pack()
option4.config(width=10,bg='dark green')

var5 = StringVar(master)
var5.set("0")
option5 = OptionMenu(master, var5, "0", "1", "2")
option5.pack()
option5.config(width=10,bg='dark green')

var6 = StringVar(master)
var6.set("0")
option6 = OptionMenu(master, var6, "0", "Soda", "Liha")
option6.pack()
option6.config(width=10,bg='dark green')

e7 = Entry(master)
e7.config(width=10,fg='white', bg='green4',highlightbackground='black')

e8 = Entry(master)
e8.config(width=10,fg='white', bg='green4',highlightbackground='black')

e9 = Entry(master)
e9.config(width=10,fg='white', bg='green4',highlightbackground='black')

e10 = Entry(master)
e10.config(width=10,fg='white', bg='green4',highlightbackground='black')

e11 = Entry(master)
e11.config(width=10,fg='white', bg='green4',highlightbackground='black')

e12 = Entry(master)
e12.config(width=10,fg='white', bg='green4',highlightbackground='black')

e13 = Entry(master)
e13.config(width=10,fg='white', bg='green4',highlightbackground='black')

option1.grid(row=0, column=1, sticky=EW)
e2.grid(row=1, column=1, sticky=EW)
option3.grid(row=2, column=1, sticky=EW)
option4.grid(row=3, column=1, sticky=EW)
option5.grid(row=4, column=1, sticky=EW)
option6.grid(row=5, column=1, sticky=EW)
e7.grid(row=0, column=3, sticky=EW)
e8.grid(row=1, column=3, sticky=EW)
e9.grid(row=2, column=3, sticky=EW)
e10.grid(row=3, column=3, sticky=EW)
e11.grid(row=4, column=3, sticky=EW)
e12.grid(row=5, column=3, sticky=EW)
e13.grid(row=6, column=1, sticky=EW)

Button(master, text='Zapusti mizo',bg='dark green',font = "Verdana 13 bold",fg='white',highlightbackground='dark green', command=master.quit).grid(row=8, column=0, sticky=EW, pady=4)
Button(master, text='Zavrti',bg='dark green',font = "Verdana 13 bold",fg='white',highlightbackground='dark green',  command=start).grid(row=8, column=1, sticky=EW, pady=4,)
Button(master, text='Zamenjaj žetone',bg='dark green',font = "Verdana 13 bold",fg='white',highlightbackground='dark green',  command=menjaj).grid(row=8, column=2, sticky=EW, pady=4)

mainloop()






