import random

CRNA = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
RDECA = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}


def zavrti():
    ''' Funkcija zavrti zavrti kolo in nam pove katera stevilka je padla.
        Vrne nam seznam ki nam pove [barvo,stevilo,stolpec,tretino,polovico,sodost]
        stevilke ki je padla'''
    stevilo = random.randint(0, 36)
    if 0 < stevilo <= 18:
        polovica = 1
    elif 18 < stevilo <= 36:
        polovica = 2
    else:
        polovica = 0
    if stevilo % 2 == 0:
        sodost = 'Soda'
    elif stevilo == 0:
        sodost = 'Soda'
    else:
        sodost = 'Liha'
    if 0 < stevilo <= 12:
        tretina = 1
    elif 13 <= stevilo <= 24:
        tretina = 2
    elif 25 <= stevilo <= 36:
        tretina = 3
    else:
        tretina = 0
    if stevilo == 0:
        stolpec = 0
    elif stevilo % 3 == 0:
        stolpec = 3
    elif stevilo in range(2, 35, 3):
        stolpec = 2
    else:
        stolpec = 1
    if stevilo == 0:
        print (stevilo)
        return ['ZELENA', stevilo, stolpec, tretina, polovica, sodost]
    elif stevilo in CRNA:
        print (stevilo)
        return ['CRNA', stevilo, stolpec, tretina, polovica, sodost]
    else:
        print (stevilo)
        return ['RDECA', stevilo, stolpec, tretina, polovica, sodost]


stevilo = 0


def preverjanje_stave():
    ''' Funkcija preverjanje stave preveri kaj smo zadeli in naredi kartoncek za pomoc pri izplacilu '''
    global stevilo
    vrtljaj = zavrti()
    stevilo = 0
    stevilo += vrtljaj[1]
    Karton = []
    for Stava, Cifra in zip(Vrsta_stave, vrtljaj):
        if Stava == Cifra:
            Karton += [1]
        else:
            Karton += [0]
    print (Karton)
    print (Vrsta_stave)
    return Karton


def izplaCilo():
    ''' Funkcija izplacilo iz stave in mnozitelja zadetkov izracuna znesek za izplacilo '''
    izplaCilo = 0
    pravilno = []
    mnozitelj_zadetkov = [2, 36, 3, 3, 2, 2]
    '''Funkcija nam pove koliko smo zasluzili oziroma izgubili pri vrtenju rulete'''
    for Denar, Stava in zip(Stavljena_vsota, preverjanje_stave()):
        pravilno += [Denar * Stava]
    for Zadetek, Mnozitelj in zip(pravilno, mnozitelj_zadetkov):
        izplaCilo += Zadetek * Mnozitelj
    return izplaCilo


#---------------------------------------TKINTER---------------------------

import tkinter as tk
from tkinter import *

master = tk.Tk()
master.title('Ruleta')
master.configure(bg='dark green')

image = tk.PhotoImage(file='//Users//Jan//Documents//Ruleta//4.gif')
label = tk.Label(image=image, compound=CENTER)
label.pack(side='right')
label.grid(row=0, column=4, sticky=W, rowspan=6)

Denarnica = 0


def igraj():
    ''' Funkcija igraj pricne igro '''
    global Denarnica
    global tisk
    premozenje = ('Na voljo imate: ', Denarnica, ' evrov.')

    if Denarnica > 0:
        if Denarnica >= sum(Stavljena_vsota):
            Denarnica -= sum(Stavljena_vsota)
            i = izplaCilo()
            Denarnica += i
            Label(
                master,
                text=(
                    'Zadeli ste ' +
                    str(i) +
                    ' evrov.' +
                    'Vlozili pa ste ' +
                    str(
                        sum(Stavljena_vsota)) +
                    'evrov'),
                bg='dark green',
                font="Verdana 13 bold",
                fg='white').grid(
                row=8,
                column=4)
            posodobi_stanje()
            padla_je()
            return Denarnica

        else:
            Label(
                master,
                text='Za tako stavo nimate dovolj denarja, kupite nove zetone ali pa spremenite stavo',
                bg='dark green',
                font="Verdana 13 bold",
                fg='white').grid(
                row=8,
                column=4)

    else:
        Label(
            master,
            text='Nimate veC denarja, kupite nove zetone',
            bg='dark green',
            font="Verdana 13 bold",
            fg='white').grid(
            row=8,
            column=4)


def start():
    ''' Funkcija start pobere vnesene stave '''
    global Vrsta_stave
    global Stavljena_vsota
    Vrsta_stave = [
        var1.get(), int(
            e2.get()), int(
            var3.get()), int(
                var4.get()), int(
                    var5.get()), var6.get()]
    Stavljena_vsota = [
        int(
            e7.get()), int(
            e8.get()), int(
                e9.get()), int(
                    e10.get()), int(
                        e11.get()), int(
                            e12.get())]
    igraj()

''' Naslednje funkcije pripravijo izpise za v tkinter '''

def padla_je():
    global stevilo
    Label(master, text=('Padla je stevilka ' + str(stevilo)), bg='dark green', font="Verdana 13 bold", fg='white').grid(row=7, column=4)


def menjaj():
    global Denarnica
    Denarnica += int(e13.get())
    posodobi_stanje()


def posodobi_stanje():
    global Denarnica
    premozenje = ('Na voljo imate: ' + str(Denarnica) + ' evrov.')
    Label(master, text=premozenje, bg='dark green', font="Verdana 13 bold", fg='white').grid(row=6, column=4)


global tisk
Label(
    master,
    text="Barva",
    bg='dark green',
    font="Verdana 13 bold",
    fg='white').grid(
        row=0)
Label(
    master,
    text="stevilo",
    bg='dark green',
    font="Verdana 13 bold",
    fg='white').grid(
        row=1)
Label(
    master,
    text="Stolpec",
    bg='dark green',
    font="Verdana 13 bold",
    fg='white').grid(
        row=2)
Label(
    master,
    text="Tretina",
    bg='dark green',
    font="Verdana 13 bold",
    fg='white').grid(
        row=3)
Label(
    master,
    text="Polovica",
    bg='dark green',
    font="Verdana 13 bold",
    fg='white').grid(
        row=4)
Label(
    master,
    text="Sodost",
    bg='dark green',
    font="Verdana 13 bold",
    fg='white').grid(
        row=5)
Label(
    master,
    text="Stava",
    bg='dark green',
    font="Verdana 13 bold",
    fg='white').grid(
        row=0,
    column=2)
Label(
    master,
    text="Stava",
    bg='dark green',
    font="Verdana 13 bold",
    fg='white').grid(
        row=1,
    column=2)
Label(
    master,
    text="Stava",
    bg='dark green',
    font="Verdana 13 bold",
    fg='white').grid(
        row=2,
    column=2)
Label(
    master,
    text="Stava",
    bg='dark green',
    font="Verdana 13 bold",
    fg='white').grid(
        row=3,
    column=2)
Label(
    master,
    text="Stava",
    bg='dark green',
    font="Verdana 13 bold",
    fg='white').grid(
        row=4,
    column=2)
Label(
    master,
    text="Stava",
    bg='dark green',
    font="Verdana 13 bold",
    fg='white').grid(
        row=5,
    column=2)
Label(
    master,
    text="Menjaj za zetone",
    bg='dark green',
    font="Verdana 13 bold",
    fg='white').grid(
        row=6)


var1 = StringVar(master)
var1.set("0")
option1 = OptionMenu(master, var1, "0", "RDECA", "CRNA")
option1.pack()
option1.config(width=10, bg='dark green')

v = IntVar()
e2 = Entry(master, text=v)
e2.config(width=10, bg='green4', fg='white', highlightbackground='black')
v.set(0)

var3 = StringVar(master)
var3.set("0")
option3 = OptionMenu(master, var3, "0", "1", "2", "3")
option3.pack()
option3.config(width=10, bg='dark green')

var4 = StringVar(master)
var4.set("0")
option4 = OptionMenu(master, var4, "0", "1", "2", "3")
option4.pack()
option4.config(width=10, bg='dark green')

var5 = StringVar(master)
var5.set("0")
option5 = OptionMenu(master, var5, "0", "1", "2")
option5.pack()
option5.config(width=10, bg='dark green')

var6 = StringVar(master)
var6.set("0")
option6 = OptionMenu(master, var6, "0", "Soda", "Liha")
option6.pack()
option6.config(width=10, bg='dark green')

v = IntVar()
e7 = Entry(master, text=v)
e7.config(width=10, fg='white', bg='green4', highlightbackground='black')
v.set(0)

v = IntVar()
e8 = Entry(master, text=v)
e8.config(width=10, fg='white', bg='green4', highlightbackground='black')
v.set(0)

v = IntVar()
e9 = Entry(master, text=v)
e9.config(width=10, fg='white', bg='green4', highlightbackground='black')
v.set(0)

v = IntVar()
e10 = Entry(master, text=v)
e10.config(width=10, fg='white', bg='green4', highlightbackground='black')
v.set(0)

v = IntVar()
e11 = Entry(master, text=v)
e11.config(width=10, fg='white', bg='green4', highlightbackground='black')
v.set(0)

v = IntVar()
e12 = Entry(master, text=v)
e12.config(width=10, fg='white', bg='green4', highlightbackground='black')
v.set(0)

v = IntVar()
e13 = Entry(master, text=v)
e13.config(width=10, fg='white', bg='green4', highlightbackground='black')
v.set(0)

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

Button(
    master,
    text='Zapusti mizo',
    bg='dark green',
    font="Verdana 13 bold",
    fg='white',
    highlightbackground='dark green',
    command=master.quit()).grid(
        row=8,
        column=0,
        sticky=EW,
    pady=4)
Button(
    master,
    text='Zavrti',
    bg='dark green',
    font="Verdana 13 bold",
    fg='white',
    highlightbackground='dark green',
    command=start).grid(
        row=8,
        column=1,
        sticky=EW,
        pady=4,
)
Button(
    master,
    text='Zamenjaj zetone',
    bg='dark green',
    font="Verdana 13 bold",
    fg='white',
    highlightbackground='dark green',
    command=menjaj).grid(
        row=8,
        column=2,
        sticky=EW,
    pady=4)

mainloop()
