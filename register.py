import string
from tkinter import * 
import os
import pandas as pd


def register_user():
    ime_info = ime.get()
    prezime_info = prezime.get()
    sifra_info = sifra.get()
    email_info = email.get()
    telbroj_info = telbroj.get()
    adresa_info = adresa.get()
    brkartice_info = brkartice.get()
    osjezik_info = osjezik.get()
    dodjezik_info = dodjezik.get()

    file=open("trener.csv", "a")
    file.write(ime_info+",")
    file.write(prezime_info+",")
    file.write(sifra_info+",")
    file.write(email_info+",")
    file.write(telbroj_info+",")
    file.write(adresa_info+",")
    file.write(brkartice_info+",")
    file.write(osjezik_info+",")
    file.write(dodjezik_info)
    file.write("\n")
    file.close()

    ime_entry.delete(0, END)
    prezime_entry.delete(0, END)
    sifra_entry.delete(0,END)
    email_entry.delete(0, END)
    telbroj_entry.delete(0, END)
    adresa_entry.delete(0, END)
    brkartice_entry.delete(0, END)
    osjezik_entry.delete(0, END)
    dodjezik_entry.delete(0, END)

    Label(screen1, text= "Registration successfull", fg = "green", font=("calibri", 11)).pack()

def register():
    global screen1
    global ime
    global prezime
    global email
    global telbroj
    global adresa
    global brkartice
    global osjezik
    global dodjezik
    global ime_entry
    global prezime_entry
    global email_entry
    global telbroj_entry
    global adresa_entry
    global brkartice_entry
    global osjezik_entry
    global dodjezik_entry
    global sifra
    global sifra_entry
    
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x450")

    ime = StringVar()
    prezime = StringVar() 
    email = StringVar() 
    telbroj = StringVar()
    adresa = StringVar() 
    brkartice = StringVar()
    osjezik = StringVar() 
    dodjezik = StringVar() 
    sifra = StringVar()

    Label(screen1, text="Ime").pack()
    ime_entry =  Entry(screen1, textvariable= ime)
    ime_entry.pack()
    Label(screen1, text="Prezime").pack()
    prezime_entry =  Entry(screen1, textvariable= prezime)
    prezime_entry.pack()
    Label(screen1, text="Sifra").pack()
    sifra_entry =  Entry(screen1, textvariable= sifra)
    sifra_entry.pack()
    Label(screen1, text="E-mail").pack()
    email_entry =  Entry(screen1, textvariable= email)
    email_entry.pack()
    Label(screen1, text="Kontakt telefon").pack()
    telbroj_entry =  Entry(screen1, textvariable= telbroj)
    telbroj_entry.pack()
    Label(screen1, text="Adresa").pack()
    adresa_entry =  Entry(screen1, textvariable= adresa)
    adresa_entry.pack()
    Label(screen1, text="Broj platne kartice").pack()
    brkartice_entry =  Entry(screen1, textvariable= brkartice)
    brkartice_entry.pack()
    Label(screen1, text="Osnovni jezik").pack()
    osjezik_entry =  Entry(screen1, textvariable= osjezik)
    osjezik_entry.pack()
    Label(screen1, text="Dodatni jezici").pack()
    dodjezik_entry =  Entry(screen1, textvariable= dodjezik)
    dodjezik_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register",width=10,height=1, command=register_user).pack()


def login():
   global screen2
   screen2 = Toplevel(screen)
   screen2.title("Login")
   screen2.geometry("300x250")

   Label(screen2, text = "Unesite detalje ispod").pack()
   Label(screen2, text = "").pack()

   global email_verify
   global sifra_verify

   email_verify = StringVar()
   sifra_verify = StringVar()

   global email_entry1
   global sifra_entry1


   Label(screen2, text = "E-mail").pack()
   email_entry1 = Entry(screen2, textvariable = email_verify)
   email_entry1.pack()
   Label(screen2, text="").pack()
   Label(screen2, text = "Sifra").pack()
   sifra_entry1 = Entry(screen2, textvariable = sifra_verify, show="*")
   sifra_entry1.pack()
   Label(screen2, text="").pack()
   Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()
   
def login_verify():
    email = email_verify.get()
    password = sifra_verify.get()
    email_entry1.delete(0,END)
    sifra_entry1.delete(0,END)
   
    df = pd.read_csv('trener.csv')

    login_check = df[["email","Sifra"]]
    if email == "": 
        Label(screen2, text= "Field cannot be empty!", fg = "red", font=("calibri", 11)).pack()

    elif password == "":
        Label(screen2, text= "Field cannot be empty!", fg = "red", font=("calibri", 11)).pack()

    elif (login_check == email,password): 
        new_screen()
        screen3.deiconify()
        screen2.destroy()
    else:
        Label(screen2, text= "Login unsuccessfull", fg = "red", font=("calibri", 11)).pack()
        

def new_screen():
    global screen3
    screen3 = Toplevel() 
    screen3.geometry("600x500")
    screen3.title("Trener")

    Label(screen3, text="TEST").pack()


        

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0", bg = "grey", width = "300",height="2", font = ("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height = "2", width="30", command = login ).pack()
    Label(text="").pack()
    Button(text="Register", height = "2", width="30", command= register).pack()

    screen.mainloop()

main_screen()