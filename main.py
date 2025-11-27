from tkinter import *
import tkintermapview

from notes import add_employees

#OKNO GLOWNE APLIKACJI
root = Tk()
root.title("ParkManager")
root.geometry("1500x700")
root.configure(bg="green")

def okno_park():
    popup = Toplevel(root)
    popup.title("Szczegóły parku/ogrodu")
    popup.geometry("400x200")


def okno_ogrodnik():
    popup = Toplevel(root)
    popup.title("Szczegóły pracownika")
    popup.geometry("400x200")


def get_employee_info():
    name:str=entry_name.get()
    workplace:str=entry_workplace.get()
    birth:int=int(entry_birth.get())
    photo:str=entry_photo.get()

    add_employees(name,workplace,birth,photo)

    entry_name.delete(0, END)
    entry_workplace.delete(0, END)
    entry_birth.delete(0, END)
    entry_photo.delete(0, END)
    entry_name.focus()

#DEFINICJA RAMEK

ramka_lista_pracownikow = Frame(root, bg="green")
ramka_lista_parkow = Frame(root, bg="green")
ramka_formularz_parkow = Frame(root, bg="green")
ramka_formularz_pracownikow = Frame(root, bg="green")
ramka_mapa = Frame(root)


ramka_lista_pracownikow.grid(row=0, column=0)
ramka_formularz_pracownikow.grid(row=0, column=1)

ramka_lista_parkow.grid(row=0, column=3)
ramka_formularz_parkow.grid(row=0, column=2)


ramka_mapa.grid(row=2, column=0, columnspan=5)


#RAMKA FORMULARZ OGRODNIKOW

label_form=Label(ramka_formularz_pracownikow, text="Wprowadź ogrodnika: ")
label_form.grid(row=0, column=0, columnspan=2)

label_name=Label(ramka_formularz_pracownikow, text="Imie: ")
label_name.grid(row=1, column=0)

label_workplace=Label(ramka_formularz_pracownikow, text="Przypisany obiekt: ")
label_workplace.grid(row=2, column=0)

label_birth=Label(ramka_formularz_pracownikow, text="Rok urodzenia: ")
label_birth.grid(row=3, column=0)

label_photo=Label(ramka_formularz_pracownikow, text="Zdjęcie: ")
label_photo.grid(row=4, column=0)

entry_name=Entry(ramka_formularz_pracownikow)
entry_name.grid(row=1, column=1)

entry_workplace=Entry(ramka_formularz_pracownikow)
entry_workplace.grid(row=2, column=1)

entry_birth=Entry(ramka_formularz_pracownikow)
entry_birth.grid(row=3, column=1)

entry_photo=Entry(ramka_formularz_pracownikow)
entry_photo.grid(row=4, column=1)

button_dodaj_ogrodnika=Button(ramka_formularz_pracownikow, text="Dodaj ogrodnika", command=get_employee_info)
button_dodaj_ogrodnika.grid(row=5, column=0, columnspan=2)


#RAMKA LISTA PRACOWNIKOW

label_lista_pracownikow=Label(ramka_lista_pracownikow, text="Lista ogrodników")
label_lista_pracownikow.grid(row=0, column=0, columnspan=3)

listbox_lista_pracownikow=Listbox(ramka_lista_pracownikow)
listbox_lista_pracownikow.grid(row=1, column=0, columnspan=3)

button_pokaz_szczegoly=Button(ramka_lista_pracownikow, text="Pokaż szczegóły", command=lambda: okno_ogrodnik())
button_pokaz_szczegoly.grid(row=2, column=0)

button_usun_ogrodnika=Button(ramka_lista_pracownikow, text="Usuń ogrodnika")
button_usun_ogrodnika.grid(row=2, column=1)

button_edytuj_pracownika=Button(ramka_lista_pracownikow, text="Edytuj ogrodnika")
button_edytuj_pracownika.grid(row=2, column=2)


#RAMKA FORMULARZ PARKOW I OGRODOW

label_form=Label(ramka_formularz_parkow, text="Wprowadź park/ogród: ")
label_form.grid(row=0, column=0, columnspan=2)

label_alias=Label(ramka_formularz_parkow, text="Nazwa: ")
label_alias.grid(row=1, column=0)

label_adress=Label(ramka_formularz_parkow, text="Adres: ")
label_adress.grid(row=2, column=0)

label_type=Label(ramka_formularz_parkow, text="Typ: ")
label_type.grid(row=3, column=0)

label_logo=Label(ramka_formularz_parkow, text="Logo: ")
label_logo.grid(row=4, column=0)

entry_alias=Entry(ramka_formularz_parkow)
entry_alias.grid(row=1, column=1)

entry_adress=Entry(ramka_formularz_parkow)
entry_adress.grid(row=2, column=1)

entry_type=Entry(ramka_formularz_parkow)
entry_type.grid(row=3, column=1, sticky=E)

entry_logo=Entry(ramka_formularz_parkow)
entry_logo.grid(row=4, column=1, sticky=E)

button_dodaj_park=Button(ramka_formularz_parkow, text="Dodaj park/ogród")
button_dodaj_park.grid(row=5, column=0, columnspan=2, sticky=E)


#RAMKA LISTA PARKOW I OGRODOW
label_lista_parkow=Label(ramka_lista_parkow, text="Lista parków/ogrodów")
label_lista_parkow.grid(row=0, column=0, columnspan=3)

listbox_lista_parkow=Listbox(ramka_lista_parkow)
listbox_lista_parkow.grid(row=1, column=0, columnspan=3)

button_pokaz_szczegoly=Button(ramka_lista_parkow, text="Pokaż szczegóły", command=lambda:okno_park())
button_pokaz_szczegoly.grid(row=2, column=0, sticky=E)

button_usun_park=Button(ramka_lista_parkow, text="Usuń obiekt")
button_usun_park.grid(row=2, column=1, sticky=E)

button_edytuj_park=Button(ramka_lista_parkow, text="Edytuj obiekt")
button_edytuj_park.grid(row=2, column=2, sticky=E)


#RAMKA MAPY

map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1500, height=600, corner_radius=0)

map_widget.set_position(52.0, 21.3)
map_widget.set_zoom(6)
map_widget.grid(row=0, column=0)


root.mainloop()