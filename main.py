from tkinter import *
from tkinter import messagebox
import tkintermapview
from ParkManager_lib.controller import employees, add_employee, show_employee, remove_employee, update_employee, get_employee_by_name



#OKNO GLOWNE APLIKACJI
root = Tk()
root.title("ParkManager")
root.geometry("1500x700")
root.configure(bg="green")

def okno_park():
    popup = Toplevel(root)
    popup.title("Szczegóły parku/ogrodu")
    popup.geometry("400x250")


def okno_ogrodnik():
    selection = listbox_lista_pracownikow.curselection()
    if not selection:
        messagebox.showwarning("Uwaga", "Wybierz ogrodnika z listy!")
        return

    selected_text = listbox_lista_pracownikow.get(selection[0])
    employee_name = selected_text.split(" - ")[0]
    employee = get_employee_by_name(employees, employee_name)
    if employee:
        popup = Toplevel(root)
        popup.title(f"Szczegóły ogrodnika - {employee_name}")
        popup.geometry("400x250")

        Label(popup, text=f"Imię: {employee.name}", font=("Arial", 12)).pack(pady=5)
        Label(popup, text=f"Miejsce pracy: {employee.workplace}", font=("Arial", 12)).pack(pady=5)
        Label(popup, text=f"Rok urodzenia: {employee.birth}", font=("Arial", 12)).pack(pady=5)
        Label(popup, text=f"Zdjęcie: {employee.photo}", font=("Arial", 12)).pack(pady=5)
        Label(popup, text=f"Współrzędne: {employee.coords[0]:.4f}, {employee.coords[1]:.4f}", font=("Arial", 10)).pack(pady=5)

    map_widget.set_position(employee.coords[0], employee.coords[1])
    map_widget.set_zoom(12)


def odswiez_liste_pracownikow():
    listbox_lista_pracownikow.delete(0, END)
    employee_list = show_employee(employees)
    for idx, employee_str in enumerate(employee_list):
        listbox_lista_pracownikow.insert(idx, employee_str)


def dodaj_ogrodnika():
    name = entry_name.get().strip()
    workplace = entry_workplace.get().strip()
    birth_str = entry_birth.get().strip()
    photo = entry_photo.get().strip()

    if not name or not workplace or not birth_str:
        messagebox.showwarning("Uwaga", "Wypełnij wszystkie wymagane pola!")
        return

    try:
        birth = int(birth_str)
    except ValueError:
        messagebox.showerror("Błąd", "Rok urodzenia musi być liczbą!")
        return

    if add_employee(employees, name, workplace, birth, photo, map_widget):
        messagebox.showinfo("Sukces", f"Dodano ogrodnika: {name}")
        entry_name.delete(0, END)
        entry_workplace.delete(0, END)
        entry_birth.delete(0, END)
        entry_photo.delete(0, END)
        entry_name.focus()
        odswiez_liste_pracownikow()
    else:
        messagebox.showerror("Błąd", "Nie udało się dodać ogrodnika")


def edytuj_ogrodnika():
    selection = listbox_lista_pracownikow.curselection()
    if not selection:
        messagebox.showwarning("Uwaga", "Wybierz ogrodnika do edycji!")
        return

    i = listbox_lista_pracownikow.index(ACTIVE)

    entry_name.delete(0, END)
    entry_name.insert(0, employees[i].name)

    entry_workplace.delete(0, END)
    entry_workplace.insert(0, employees[i].workplace)

    entry_birth.delete(0, END)
    entry_birth.insert(0,employees[i].birth)

    entry_photo.delete(0, END)
    entry_photo.insert(0,employees[i].photo)

    #ZMIANA PRZYCISKU

    button_dodaj_ogrodnika.config(text='Zapisz zmiany', command=lambda: zaktualizuj_ogrodnika(i))


def zaktualizuj_ogrodnika(i):
    name = entry_name.get().strip()
    workplace = entry_workplace.get().strip()
    birth_str = entry_birth.get().strip()
    photo = entry_photo.get().strip()

    if not name or not workplace or not birth_str:
        messagebox.showwarning("Uwaga", "Wypełnij wszystkie wymagane pola!")
        return
    try:
        birth = int(birth_str)
    except ValueError:
        messagebox.showerror("Błąd", "Rok urodzenia musi być liczbą!")
        return


    if update_employee(employees, i, name, workplace, birth, photo):
        messagebox.showinfo("Sukces", f"Zaktualizowano dane ogrodnika!")
        odswiez_liste_pracownikow()

        button_dodaj_ogrodnika.config(text='Dodaj ogrodnika', command=dodaj_ogrodnika)

        entry_name.delete(0, END)
        entry_workplace.delete(0, END)
        entry_birth.delete(0, END)
        entry_photo.delete(0, END)
        entry_name.focus()

    else:
        messagebox.showerror("Błąd", "Nie udało się zaktualizować ogrodnika!")


def usun_ogrodnika():
    selection = listbox_lista_pracownikow.curselection()
    if not selection:
        messagebox.showwarning("Uwaga", "Wybierz ogrodnika do usunięcia!")
        return

    i = listbox_lista_pracownikow.index(ACTIVE)
    employee_name = employees[i].name

    if messagebox.askyesno("Potwierdzenie", f"Czy na pewno chcesz usunąć ogrodnika: {employee_name}?"):
        if remove_employee(employees, i):
            messagebox.showinfo("Sukces", f"Usunięto ogrodnika: {employee_name}")
            odswiez_liste_pracownikow()
        else:
            messagebox.showerror("Błąd", "Nie udało się usunąć ogrodnika!")

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

button_dodaj_ogrodnika=Button(ramka_formularz_pracownikow, text="Dodaj ogrodnika", command=dodaj_ogrodnika)
button_dodaj_ogrodnika.grid(row=5, column=0, columnspan=2)


#RAMKA LISTA PRACOWNIKOW

label_lista_pracownikow=Label(ramka_lista_pracownikow, text="Lista ogrodników")
label_lista_pracownikow.grid(row=0, column=0, columnspan=3)

listbox_lista_pracownikow=Listbox(ramka_lista_pracownikow)
listbox_lista_pracownikow.grid(row=1, column=0, columnspan=3)

button_pokaz_szczegoly=Button(ramka_lista_pracownikow, text="Pokaż szczegóły", command=lambda: okno_ogrodnik())
button_pokaz_szczegoly.grid(row=2, column=0)

button_usun_pracownika=Button(ramka_lista_pracownikow, text="Usuń ogrodnika", command=usun_ogrodnika)
button_usun_pracownika.grid(row=2, column=1)

button_edytuj_pracownika=Button(ramka_lista_pracownikow, text="Edytuj ogrodnika", command=edytuj_ogrodnika)
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