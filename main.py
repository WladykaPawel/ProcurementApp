# ======================Python program for creating pdf with procurement===================================
from fpdf import FPDF
from datetime import date
import tkinter as tk
from tkinter import *

fdate = date.today().strftime('%d.%m.%Y')

# ============================APLICATION==========================================

root = tk.Tk()

canvas1 = tk.Canvas(root, width=1200, height=900)


label1 = tk.Label(root, text='Opiekun:')
label1.config(font=('helvetica', 10))
canvas1.create_window(50, 20, window=label1)

entry1 = tk.Entry(root, width=40)
entry1.place(x=10, y=440, width=40, height=20000)
canvas1.create_window(150, 40, window=entry1)

label2 = tk.Label(root, text='Katedra:')
label2.config(font=('helvetica', 10))
canvas1.create_window(400, 20, window=label2)

entry2 = tk.Entry(root, width=40)
canvas1.create_window(500, 40, window=entry2)

label3 = tk.Label(root, text='Specyfikacja produktu (opis):')
label3.config(font=('helvetica', 10))
canvas1.create_window(110, 80, window=label3)

entry3 = tk.Entry(root, width=180)
canvas1.create_window(570, 100, window=entry3)

canvas1.pack()
def getSquareRoot():
    opiekun = entry1.get()
    katedra = entry2.get()
    opis = entry3.get()

    # ============================CREATE PDF==========================================

    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()
    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Times", size=12)

    # # create a cell
    pdf.cell(170, 10, txt="Rzeszow, dnia", ln=0, align='R')
    pdf.cell(0, 10, txt=fdate, ln=1, align='R')
    # # add another cell
    pdf.set_font("Times", 'B', size=12)
    pdf.cell(20, 10, txt="Studenckie Kolo", ln=1, align='L')
    pdf.cell(20, 10, txt="Naukowe Lotnikow", ln=1, align='L')
    pdf.cell(160, 10, txt="Opiekun: ", ln=0, align='R')
    pdf.cell(0, 10, txt=opiekun, ln=1, align='R')
    pdf.cell(160, 10, txt="Katedra: ", ln=0, align='R')
    pdf.cell(0, 10, txt=katedra, ln=1, align='R')

    pdf.set_font("Times", 'B', size=14)
    pdf.cell(180, 10, txt="Zamownienie", ln=1, align='C')

    pdf.set_font("Times", size=12)
    pdf.cell(20, 10, txt=" ", ln=1, align='L')
    pdf.cell(50, 10, txt="Specyfikacja produktu (opis): ", ln=1, align='L')
    pdf.multi_cell(140, 10, txt=opis, align='J')

    pdf.cell(20, 10, txt=" ", ln=1, align='L')

    pdf.cell(20, 10, txt="Nazwa oferty: ......................", ln=1, align='L')
    pdf.cell(20, 10, txt="Link: .......................", ln=1, align='L')
    pdf.cell(20, 10, txt="Cena: .......................", ln=1, align='L')
    pdf.cell(20, 10, txt=" ", ln=1, align='L')
    pdf.cell(20, 10, txt="Zdjecia: ...................", ln=1, align='L')
    pdf.cell(20, 10, txt=" ", ln=1, align='L')

    pdf.cell(20, 10, txt="Nazwa kontroferty: ......................", ln=1, align='L')
    pdf.cell(20, 10, txt="Link: ......................", ln=1, align='L')
    pdf.cell(20, 10, txt="Cena: ......................", ln=1, align='L')
    pdf.cell(20, 10, txt=" ", ln=1, align='L')
    pdf.cell(20, 10, txt="Zdjecia: ...................", ln=1, align='L')
    pdf.cell(20, 10, txt=" ", ln=1, align='L')

    pdf.set_font("Times", 'B', size=12)
    pdf.cell(20, 10, txt="Ostateczny wybor oferty: ...................", ln=1, align='L')
    pdf.set_font("Times", size=12)
    pdf.cell(20, 10, txt="Przeznaczone srodki: ...................", ln=1, align='L')
    pdf.cell(20, 10, txt="Zrodlo finansowania: ...................", ln=1, align='L')

    # save the pdf with name .pdf
    pdf.output("Zamównie Publiczne.pdf")


button1 = tk.Button(text='Stwórz PDF-a', command=getSquareRoot, width=20, height=5)
canvas1.create_window(600, 800, window=button1)

root.mainloop()





