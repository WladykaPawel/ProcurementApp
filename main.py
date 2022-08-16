# ======================Python program for creating pdf with procurement===================================

#!/usr/bin/env python
# -*- coding: utf8 -*-
from tkinter import filedialog
from fpdf import FPDF
from datetime import date
import tkinter as Apka_do_zamówień
import PIL.Image
from PIL import ImageTk
import os
from tkinter import *



fdate = date.today().strftime('%d.%m.%Y')


# ============================APLICATION==========================================
root = Apka_do_zamówień.Tk()
root.title("Aplikacja do zamównień publicznych")
root.iconbitmap("favicon.ico")


canvas1 = Apka_do_zamówień.Canvas(root, width=1400, height=900)

logo = PIL.Image.open("logo.png")
logo_resized = logo.resize((50, 50))  # new width & height
logo = ImageTk.PhotoImage(logo_resized)
Logo = Apka_do_zamówień.Label(text='Upload File', image=logo)
canvas1.create_window(1200, 50, window=Logo)

title = Apka_do_zamówień.Label(root, text='LEGENDARY ROVER')
title.config(font=('helvetica', 15))
canvas1.create_window(1200, 90, window=title)

title = Apka_do_zamówień.Label(root, text='   TEAM   ')
title.config(font=('helvetica', 15))
canvas1.create_window(1200, 120, window=title)


label1 = Apka_do_zamówień.Label(root, text='Opiekun:')
label1.config(font=('helvetica', 10))
canvas1.create_window(50, 20, window=label1)

entry1 = Apka_do_zamówień.Entry(root, width=40)
entry1.place(x=10, y=440, width=40, height=20000)
canvas1.create_window(150, 40, window=entry1)

label2 = Apka_do_zamówień.Label(root, text='Katedra:')
label2.config(font=('helvetica', 10))
canvas1.create_window(400, 20, window=label2)

entry2 = Apka_do_zamówień.Entry(root, width=40)
canvas1.create_window(500, 40, window=entry2)

label3 = Apka_do_zamówień.Label(root, text='Specyfikacja produktu (opis):')
label3.config(font=('helvetica', 10))
canvas1.create_window(110, 80, window=label3)

entry3 = Apka_do_zamówień.Entry(root, width=150)
canvas1.create_window(480, 100, window=entry3)


Title1 = Apka_do_zamówień.Label(root, text='Pierwszy Produkt:')
Title1.config(font=('helvetica', 15))
canvas1.create_window(600, 140, window=Title1)



label4 = Apka_do_zamówień.Label(root, text='Nazwa oferty:')
label4.config(font=('helvetica', 10))
canvas1.create_window(65, 180, window=label4)
entry4 = Apka_do_zamówień.Entry(root, width=70)
canvas1.create_window(240, 200, window=entry4)

label5 = Apka_do_zamówień.Label(root, text='Link:')
label5.config(font=('helvetica', 10))
canvas1.create_window(45, 240, window=label5)
entry5 = Apka_do_zamówień.Entry(root, width=70)
canvas1.create_window(240, 260, window=entry5)

label6 = Apka_do_zamówień.Label(root, text='Cena:')
label6.config(font=('helvetica', 10))
canvas1.create_window(45, 300, window=label6)
entry6 = Apka_do_zamówień.Entry(root, width=70)
canvas1.create_window(240, 320, window=entry6)



button1 = Apka_do_zamówień.Button(text='Upload File', width=20, height=2, command = lambda:upload_file())
canvas1.create_window(1000, 220, window=button1)



Title2 = Apka_do_zamówień.Label(root, text='Drugi Produkt:')
Title2.config(font=('helvetica', 15))
canvas1.create_window(600, 460, window=Title2)



label7 = Apka_do_zamówień.Label(root, text='Nazwa kontroferty:')
label7.config(font=('helvetica', 10))
canvas1.create_window(85, 500, window=label7)
entry7 = Apka_do_zamówień.Entry(root, width=70)
canvas1.create_window(240, 520, window=entry7)

label8 = Apka_do_zamówień.Label(root, text='Link:')
label8.config(font=('helvetica', 10))
canvas1.create_window(45, 560, window=label8)
entry8 = Apka_do_zamówień.Entry(root, width=70)
canvas1.create_window(240, 580, window=entry8)

label9 = Apka_do_zamówień.Label(root, text='Cena:')
label9.config(font=('helvetica', 10))
canvas1.create_window(45, 620, window=label9)
entry9 = Apka_do_zamówień.Entry(root, width=70)
canvas1.create_window(240, 640, window=entry9)


button2 = Apka_do_zamówień.Button(text='Upload File', width=20, height=2, command = lambda:upload_file2())
canvas1.create_window(1000, 520, window=button2)

label10 = Apka_do_zamówień.Label(root, text='Ostateczny wybór oferty:')
label10.config(font=('helvetica', 10))
canvas1.create_window(100, 670, window=label10)
entry10 = Apka_do_zamówień.Entry(root, width=70)
canvas1.create_window(400, 670, window=entry10)

label11 = Apka_do_zamówień.Label(root, text='Przeznaczone środki:')
label11.config(font=('helvetica', 10))
canvas1.create_window(92, 700, window=label11)
entry11 = Apka_do_zamówień.Entry(root, width=70)
canvas1.create_window(400, 700, window=entry11)

label12 = Apka_do_zamówień.Label(root, text='Źródło finansowania:')
label12.config(font=('helvetica', 10))
canvas1.create_window(88, 730, window=label12)
entry12 = Apka_do_zamówień.Entry(root, width=70)
canvas1.create_window(400, 730, window=entry12)

def upload_file():
    if os.path.exists("img1.png"):
        os.remove("img1.png")
    global img
    global Pimg
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = PIL.Image.open(filename)
    Pimg = PIL.Image.open(filename)
    Pimg_resized=Pimg.resize((280,200)) # new width & height
    Pimg=ImageTk.PhotoImage(Pimg_resized)
    picture1 = Apka_do_zamówień.Label(text='Upload File', image=Pimg)
    canvas1.create_window(1000, 280, window=picture1)

def upload_file2():
    if os.path.exists("img2.png"):
        os.remove("img2.png")
    global img2
    global Pimg2
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img2 = PIL.Image.open(filename)
    Pimg2 = PIL.Image.open(filename)
    Pimg2_resized=Pimg2.resize((280,200)) # new width & height
    Pimg2=ImageTk.PhotoImage(Pimg2_resized)
    picture2 = Apka_do_zamówień.Label(text='Upload File', image=Pimg2)
    canvas1.create_window(1000, 580, window=picture2)
canvas1.pack()




def getSquareRoot():
    opiekun = entry1.get()
    katedra = entry2.get()
    opis = entry3.get()
    nazwa = entry4.get()
    link = entry5.get()
    cena = entry6.get()
    nazwa2 = entry7.get()
    link2 = entry8.get()
    cena2 = entry9.get()
    wybor = entry10.get()
    srodki = entry11.get()
    zrodlo = entry12.get()

    img.save("img1.png","PNG")
    img2.save("img2.png", "PNG")


    # ============================CREATE PDF==========================================

    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()
    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    # pdf.set_font("Times", size=12)

    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 12)

    # # create a cell
    pdf.cell(164, 10, txt="Rzeszów, dnia", ln=0, align='R')
    pdf.cell(0, 10, txt=fdate, ln=1, align='R')
    # # add another cell
    pdf.set_font('DejaVu', size=12)
    pdf.cell(20, 10, txt="Studenckie Koło", ln=1, align='L')
    pdf.cell(20, 10, txt="Naukowe Lotników", ln=1, align='L')
    pdf.cell(160, 10, txt="Opiekun: ", ln=0, align='R')
    pdf.cell(0, 10, txt=opiekun, ln=1, align='R')
    pdf.cell(160, 10, txt="Katedra: ", ln=0, align='R')
    pdf.cell(0, 10, txt=katedra, ln=1, align='R')

    pdf.add_font('DejaVu', 'B', 'DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', 'B', size=14)
    pdf.cell(180, 10, txt="Zamównienie", ln=1, align='C')

    pdf.set_font('DejaVu', size=12)
    pdf.cell(20, 10, txt=" ", ln=1, align='L')
    pdf.cell(50, 10, txt="Specyfikacja produktu (opis): ", ln=1, align='L')
    pdf.multi_cell(140, 10, txt=opis, align='J')

    pdf.cell(20, 10, txt=" ", ln=1, align='L')

    pdf.cell(35, 10, txt="Nazwa oferty: ", ln=0, align='L')
    pdf.cell(140, 10, txt=nazwa, ln=1, align='L')
    pdf.cell(20, 10, txt="Link: ", ln=0, align='L')
    pdf.cell(140, 10, txt=link, ln=1, align='L')
    pdf.cell(20, 10, txt="Cena: ", ln=0, align='L')
    pdf.cell(140, 10, txt=cena, ln=1, align='L')
    pdf.cell(20, 10, txt=" ", ln=1, align='L')
    pdf.cell(20, 10, txt="Zdjęcia: ", ln=1, align='L')
    pdf.image('img1.png', x = None, y = None, w = 130, h = 80)
    pdf.cell(20, 10, txt=" ", ln=1, align='L')
    pdf.cell(20, 10, txt=" ", ln=1, align='L')

    pdf.cell(50, 10, txt="Nazwa kontroferty:", ln=0, align='L')
    pdf.cell(140, 10, txt=nazwa2, ln=1, align='L')
    pdf.cell(20, 10, txt="Link: ", ln=0, align='L')
    pdf.cell(140, 10, txt=link2, ln=1, align='L')
    pdf.cell(20, 10, txt="Cena: ", ln=0, align='L')
    pdf.cell(140, 10, txt=cena2, ln=1, align='L')
    pdf.cell(20, 10, txt=" ", ln=1, align='L')
    pdf.cell(20, 10, txt="Zdjęcia: .", ln=1, align='L')
    pdf.image('img2.png', x=None, y=None, w=130, h=80)
    pdf.cell(20, 10, txt=" ", ln=1, align='L')

    pdf.set_font('DejaVu', 'B', size=12)
    pdf.cell(20, 10, txt="Ostateczny wybór oferty: ", ln=1, align='L')
    pdf.cell(140, 10, txt=wybor, ln=1, align='L')
    pdf.set_font('DejaVu', size=12)
    pdf.cell(20, 10, txt="Przeznaczone środki: ", ln=1, align='L')
    pdf.cell(140, 10, txt=srodki, ln=1, align='L')
    pdf.cell(20, 10, txt="Źródło finansowania: ", ln=1, align='L')
    pdf.cell(140, 10, txt=zrodlo, ln=1, align='L')

    # save the pdf with name .pdf
    pdf.output("Zamównie Publiczne.pdf")


buttonend = Apka_do_zamówień.Button(text='Stwórz PDF-a', command=getSquareRoot, width=20, height=2)
canvas1.create_window(600, 780, window=buttonend)

root.mainloop()





