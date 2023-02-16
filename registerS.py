import string
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkcalendar import *
from tkinter import filedialog
from tkinter import ttk, filedialog

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

    file = open("trener.csv", "a")
    file.write(ime_info + ",")
    file.write(prezime_info + ",")
    file.write(sifra_info + ",")
    file.write(email_info + ",")
    file.write(telbroj_info + ",")
    file.write(adresa_info + ",")
    file.write(brkartice_info + ",")
    file.write(osjezik_info + ",")
    file.write(dodjezik_info)
    file.write("\n")
    file.close()

    ime_entry.delete(0, END)
    prezime_entry.delete(0, END)
    sifra_entry.delete(0, END)
    email_entry.delete(0, END)
    telbroj_entry.delete(0, END)
    adresa_entry.delete(0, END)
    brkartice_entry.delete(0, END)
    osjezik_entry.delete(0, END)
    dodjezik_entry.delete(0, END)

    Label(screen1, text="Registration successfull", fg="green", font=("calibri", 11)).pack()


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
    ime_entry = Entry(screen1, textvariable=ime)
    ime_entry.pack()
    Label(screen1, text="Prezime").pack()
    prezime_entry = Entry(screen1, textvariable=prezime)
    prezime_entry.pack()
    Label(screen1, text="Sifra").pack()
    sifra_entry = Entry(screen1, textvariable=sifra)
    sifra_entry.pack()
    Label(screen1, text="E-mail").pack()
    email_entry = Entry(screen1, textvariable=email)
    email_entry.pack()
    Label(screen1, text="Kontakt telefon").pack()
    telbroj_entry = Entry(screen1, textvariable=telbroj)
    telbroj_entry.pack()
    Label(screen1, text="Adresa").pack()
    adresa_entry = Entry(screen1, textvariable=adresa)
    adresa_entry.pack()
    Label(screen1, text="Broj platne kartice").pack()
    brkartice_entry = Entry(screen1, textvariable=brkartice)
    brkartice_entry.pack()
    Label(screen1, text="Osnovni jezik").pack()
    osjezik_entry = Entry(screen1, textvariable=osjezik)
    osjezik_entry.pack()
    Label(screen1, text="Dodatni jezici").pack()
    dodjezik_entry = Entry(screen1, textvariable=dodjezik)
    dodjezik_entry.pack()
    Label(screen1, text="").pack()

    Button(screen1, text="Unos Diplome", width=10, height=1, command=diploma).pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def diploma():  # prozor za unos diplome/sertifikata Trenera
    root = Tk()
    root.title('Verifikacija')

    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))

    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    Label(image=my_image).pack()

    root.mainloop()


def login():  # login/prijava prozor
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")

    Label(screen2, text="Unesite detalje ispod").pack()
    Label(screen2, text="").pack()

    global email_verify
    global sifra_verify

    email_verify = StringVar()
    sifra_verify = StringVar()

    global email_entry1
    global sifra_entry1

    Label(screen2, text="E-mail").pack()
    email_entry1 = Entry(screen2, textvariable=email_verify)
    email_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Sifra").pack()
    sifra_entry1 = Entry(screen2, textvariable=sifra_verify, show="*")
    sifra_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def login_verify():  # Verifikacija logina
    email = email_verify.get()
    password = sifra_verify.get()
    email_entry1.delete(0, END)
    sifra_entry1.delete(0, END)

    df = pd.read_csv('trener.csv')

    login_check = df[["email", "Sifra"]]
    if email == "":
        Label(screen2, text="Field cannot be empty!", fg="red", font=("calibri", 11)).pack()

    elif password == "":
        Label(screen2, text="Field cannot be empty!", fg="red", font=("calibri", 11)).pack()

    elif (login_check == email, password):
        new_screen()
        screen3.deiconify()
        screen2.destroy()
    else:
        Label(screen2, text="Login unsuccessfull", fg="red", font=("calibri", 11)).pack()


def new_screen():  # Prozor za ulogovanog Trenera
    global screen3
    screen3 = Toplevel()
    screen3.geometry("600x500")
    screen3.title("Trener meni")

    Label(screen3, text="Prikaz termina").pack()

    cal = Calendar(screen3, selectmode="day", year=2023, day=17, month=2)
    cal.pack(pady=10)

    def grab_date():
        my_label.config(text="Slobodan termin" + cal.get_date())

    my_button = Button(screen3, text="Proveri dostupnost termina",
                       command=grab_date)  # svi su slobodni, jer inicijalizujemo samo trenera, nemamo klijnt deo
    my_button.pack(pady=5)

    my_label = Label(screen3, text="")
    my_label.pack(pady=5)

    Button(screen3, text="Osmisli trening", width=15, height=1, command=create_training).pack()
    Button(screen3, text="Oceni klijenta", width=15, height=1, command=rate_client).pack()


def rate_client_user():
    ime_info = ime.get()
    prezime_info = prezime.get()
    ocena_info = ocena.get()
    komentar_info = komentar.get()

    file = open("ocenaKlijenta.csv", "a")
    file.write(ime_info + ",")
    file.write(prezime_info + ",")
    file.write(ocena_info + ",")
    file.write(komentar_info)
    file.write("\n")
    file.close()

    ime_entry.delete(0, END)
    prezime_entry.delete(0, END)
    ocena_entry.delete(0, END)
    komentar_entry.delete(0, END)

    Label(screen5, text="Uspesno ocenjen klijent!", fg="green", font=("calibri", 11)).pack()


def rate_client():
    global screen5
    screen5 = Toplevel()
    screen5.geometry("600x500")
    screen5.title("Oceni klijenta")

    global screen1
    global ime
    global prezime
    global ocena
    global komentar
    global ime_entry
    global prezime_entry
    global ocena_entry
    global komentar_entry

    ime = StringVar()
    prezime = StringVar()
    ocena = StringVar()
    komentar = StringVar()

    Label(screen5, text="Ime").pack()
    ime_entry = Entry(screen5, textvariable=ime)
    ime_entry.pack()
    Label(screen5, text="Prezime").pack()
    prezime_entry = Entry(screen5, textvariable=prezime)
    prezime_entry.pack()
    Label(screen5, text="Ocena(u zvezdicama)").pack()
    ocena_entry = Entry(screen5, textvariable=ocena)
    ocena_entry.pack()
    Label(screen5, text="Komentar").pack()
    komentar_entry = Entry(screen5, textvariable=komentar)
    komentar_entry.pack()
    Label(screen5, text="").pack()

    Button(screen5, text="Potvrdi", width=15, height=1, command=rate_client_user).pack()

def create_training():  # Kreiranje treninga klijentu prozor
    global screen4
    screen4 = Toplevel()
    screen4.geometry("1200x700")
    screen4.title("Kreiranje treninga")

    # Create frame
    my_frame = Frame(screen4)
    my_frame.pack(pady=10)

    # Create treeview
    my_tree = ttk.Treeview(my_frame)

    # File open function
    def file_open():
        filename = filedialog.askopenfilename(
            initialdir="C:/gui/",
            title="Open A File",
            filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*"))
        )

        if filename:
            try:
                filename = r"{}".format(filename)
                df = pd.read_csv(filename)
            except ValueError:
                my_label.config(text="File Couldn't Be Opened...try again!")
            except FileNotFoundError:
                my_label.config(text="File Couldn't Be Found...try again!")
        # Clear old treeview
        clear_tree()

        # Set up new treeview
        my_tree["column"] = list(df.columns)
        my_tree["show"] = "headings"
        # Loop thru column list for headers
        for column in my_tree["column"]:
            my_tree.heading(column, text=column)

        # Put data in treeview
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            my_tree.insert("", "end", values=row)

        # Pack the treeview finally
        my_tree.pack()

    def clear_tree():
        my_tree.delete(*my_tree.get_children())

    # Add a menu
    my_menu = Menu(screen4)
    screen4.config(menu=my_menu)

    # Add menu dropdown
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Klijenti", menu=file_menu)
    file_menu.add_command(label="Otvori fajl", command=file_open)

    my_label = Label(screen4, text='')
    my_label.pack(pady=20)

    # UPISIVANJE OPISA TRENINGA
    Label(screen4, text="Osmislite trening na osnovi podataka klijenta iznad").pack()

    def open_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File",
                                               filetypes=(("Text Files", "*.txt"),))
        name = text_file
        name = name.replace("C:/gui/", "")
        name = name.replace(".txt", "")

        text_file = open(text_file, 'r')
        stuff = text_file.read()

        my_text.insert(END, stuff)
        text_file.close()

        screen4.title(f'{name} - Textpad')

    def save_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Save To Text File",
                                               filetypes=(("Text Files", "*.txt"),))
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))

    my_frame = Frame(screen4)
    my_frame.pack(pady=5)

    # Create scrollbar
    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow",
                   selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
    my_text.pack()

    # Configure our scrollbar
    text_scroll.config(command=my_text.yview)

    open_button = Button(screen4, text="Open Text File", command=open_txt)
    open_button.pack(pady=10)

    save_button = Button(screen4, text="Save File", command=save_txt)
    save_button.pack(pady=5)

    my_label = Label(screen4, text="")
    my_label.pack()


def main_screen():  # Pocetni/glavni prozor
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Welcome")
    Label(text="Welcome", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()
