from tkinter import *
from tkinter import messagebox
import tkintermapview
from ParkManager_lib.controller import employees, add_employee, show_employee, remove_employee, update_employee, get_employee_by_name
from ParkManager_lib.controller import parks, add_park, show_park, remove_park, update_park, get_park_by_alias
from ParkManager_lib.controller import users, add_user, show_user, remove_user, update_user, get_user_by_username


def start_app():
    # OKNO GLOWNE APLIKACJI
    root = Tk()
    root.title("ParkManager")
    root.geometry("1500x700")
    root.configure(bg="green")


    def okno_uzytkownik():
        popup = Toplevel(root)
        popup.title("Użytkownicy")
        popup.geometry("580x270")
        popup.transient(root)

        def okno_szczegoly_uzytkownika():
            selection = listbox_lista_obiektow.curselection()
            if not selection:
                messagebox.showwarning("Uwaga", "Wybierz użytkownika z listy!")
                return

            selected_text = listbox_lista_obiektow.get(selection[0])
            username = selected_text.split(" - ")[0]

            user = get_user_by_username(users, username)
            if not user:
                return

            popup_szcz = Toplevel(popup)
            popup_szcz.title(f"Szczegóły użytkownika - {user.username}")
            popup_szcz.geometry("400x250")

            Label(popup_szcz, text=f"Username: {user.username}", font=("Arial", 12)).pack(pady=5)
            Label(popup_szcz, text=f"Lokalizacja: {user.location}", font=("Arial", 12)).pack(pady=5)
            Label(popup_szcz, text=f"Typ: {user.user_type}", font=("Arial", 12)).pack(pady=5)
            Label(popup_szcz, text=f"Ulubiony park: {user.fav_park}", font=("Arial", 12)).pack(pady=5)
            Label(popup_szcz,text=f"Współrzędne: {user.coords[0]:.4f}, {user.coords[1]:.4f}",font=("Arial", 10)).pack(pady=5)




        ramka_lista_uzytkownikow = Frame(popup)
        ramka_formularz_uzytkownikow = Frame(popup)
        ramka_lista_uzytkownikow.grid(row=0, column=0)
        ramka_formularz_uzytkownikow.grid(row=0, column=1)


        def odswiez_liste_uzytkownikow():
            listbox_lista_obiektow.delete(0, END)
            for idx, user in enumerate(show_user(users)):
                listbox_lista_obiektow.insert(idx, user)

        def dodaj_uzytkownika():
            username = entry_imie.get()
            location = entry_lokalizacja.get()
            user_type = entry_typ.get()
            fav_park = entry_fav_park.get()

            add_user(users, username, location, user_type, fav_park)

            messagebox.showinfo("Sukces", f"Dodano użytkownika: {username}")
            odswiez_liste_uzytkownikow()

            entry_imie.delete(0, END)
            entry_lokalizacja.delete(0, END)
            entry_typ.delete(0, END)
            entry_fav_park.delete(0, END)

        def edytuj_uzytkownika():
            selection = listbox_lista_obiektow.curselection()
            if not selection:
                messagebox.showwarning("Uwaga", "Wybierz użytkownika do edycji!")
                return

            i = listbox_lista_obiektow.index(ACTIVE)
            user = users[i]

            entry_imie.delete(0, END)
            entry_imie.insert(0, user.username)

            entry_lokalizacja.delete(0, END)
            entry_lokalizacja.insert(0, user.location)

            entry_typ.delete(0, END)
            entry_typ.insert(0, user.user_type)

            entry_fav_park.delete(0, END)
            entry_fav_park.insert(0, user.fav_park)

            button_dodaj_obiekt.config(
                text="Zapisz zmiany",
                command=lambda: zaktualizuj_uzytkownika(i)
            )

        def zaktualizuj_uzytkownika(i):
            username = entry_imie.get()
            location = entry_lokalizacja.get()
            user_type = entry_typ.get()
            fav_park = entry_fav_park.get()

            update_user(users, i, username, location, user_type, fav_park)
            messagebox.showinfo("Sukces", "Zaktualizowano użytkownika")

            odswiez_liste_uzytkownikow()

            button_dodaj_obiekt.config(text="Dodaj użytkownika",command=dodaj_uzytkownika)

            entry_imie.delete(0, END)
            entry_lokalizacja.delete(0, END)
            entry_typ.delete(0, END)
            entry_fav_park.delete(0, END)
            entry_imie.focus()

        def usun_uzytkownika():
            selection = listbox_lista_obiektow.curselection()
            if not selection:
                messagebox.showwarning("Uwaga", "Wybierz użytkownika do usunięcia!")
                return

            i = listbox_lista_obiektow.index(ACTIVE)
            username = users[i].username

            if messagebox.askyesno("Potwierdzenie", f"Czy na pewno chcesz usunąć użytkownika {username}?"):
                remove_user(users, i)
                odswiez_liste_uzytkownikow()

        label_lista_uzytkownikow=Label(ramka_lista_uzytkownikow, text="Lista użytkowników")
        label_lista_uzytkownikow.grid(row=0, column=0, columnspan=3)

        listbox_lista_obiektow = Listbox(ramka_lista_uzytkownikow)
        listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)

        button_pokaz_szczegoly = Button(ramka_lista_uzytkownikow, text="Pokaż szczegóły",command=okno_szczegoly_uzytkownika)
        button_pokaz_szczegoly.grid(row=2, column=0)

        button_usun_obiekt = Button(ramka_lista_uzytkownikow, text="Usuń użytkownika", command=usun_uzytkownika)
        button_usun_obiekt.grid(row=2, column=1)

        button_edytuj_obiekt = Button(ramka_lista_uzytkownikow, text="Edytuj użytkownika", command=edytuj_uzytkownika)
        button_edytuj_obiekt.grid(row=2, column=2)

        label_formularz = Label(ramka_formularz_uzytkownikow, text="Formularz: ")
        label_formularz.grid(row=0, column=0, columnspan=2)

        label_imie = Label(ramka_formularz_uzytkownikow, text="Imie: ")
        label_imie.grid(row=1, column=0, sticky=W)

        label_lokalizacja = Label(ramka_formularz_uzytkownikow, text="Lokalizacja: ")
        label_lokalizacja.grid(row=2, column=0, sticky=W)

        label_typ = Label(ramka_formularz_uzytkownikow, text="Typ: ")
        label_typ.grid(row=3, column=0, sticky=W)

        label_fav_park = Label(ramka_formularz_uzytkownikow, text="Ulubiony park: ")
        label_fav_park.grid(row=4, column=0, sticky=W)

        entry_imie = Entry(ramka_formularz_uzytkownikow)
        entry_imie.grid(row=1, column=1)

        entry_lokalizacja = Entry(ramka_formularz_uzytkownikow)
        entry_lokalizacja.grid(row=2, column=1)

        entry_typ = Entry(ramka_formularz_uzytkownikow)
        entry_typ.grid(row=3, column=1)

        entry_fav_park = Entry(ramka_formularz_uzytkownikow)
        entry_fav_park.grid(row=4, column=1)

        button_dodaj_obiekt = Button(ramka_formularz_uzytkownikow, text="Dodaj użytkownika", command=dodaj_uzytkownika)
        button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

        odswiez_liste_uzytkownikow()

    def okno_park():
        selection = listbox_lista_parkow.curselection()
        if not selection:
            messagebox.showwarning("Uwaga", "Wybierz park z listy!")
            return

        selected_text = listbox_lista_parkow.get(selection[0])
        park_alias = selected_text.split(" - ")[0]
        park = get_park_by_alias(parks, park_alias)
        if park:
            popup = Toplevel(root)
            popup.title("Szczegóły parku/ogrodu")
            popup.geometry("400x250")

            Label(popup, text=f"Nazwa: {park.alias}", font=("Arial", 12)).pack(pady=5)
            Label(popup, text=f"Adres: {park.address}", font=("Arial", 12)).pack(pady=5)
            Label(popup, text=f"Typ: {park.category}", font=("Arial", 12)).pack(pady=5)
            Label(popup, text=f"Logo: {park.logo}", font=("Arial", 12)).pack(pady=5)
            Label(popup, text=f"Współrzędne: {park.coords[0]:.4f}, {park.coords[1]:.4f}", font=("Arial", 10)).pack(
                pady=5)

        map_widget.set_position(park.coords[0], park.coords[1])
        map_widget.set_zoom(17)

    def odswiez_liste_parkow():
        listbox_lista_parkow.delete(0, END)
        park_list = show_park(parks)
        for idx, park in enumerate(park_list):
            listbox_lista_parkow.insert(idx, park)

    def dodaj_park():
        alias = entry_alias.get()
        address = entry_address.get()
        category = entry_category.get()
        logo = entry_logo.get()

        add_park(parks, alias, address, category, logo, map_widget)
        messagebox.showinfo("Sukces", f"Dodano park: {alias}")
        entry_alias.delete(0, END)
        entry_address.delete(0, END)
        entry_category.delete(0, END)
        entry_logo.delete(0, END)
        entry_alias.focus()
        odswiez_liste_parkow()

    def edytuj_park():
        selection = listbox_lista_parkow.curselection()
        if not selection:
            messagebox.showwarning("Uwaga", "Wybierz park do edycji!")
            return

        i = listbox_lista_parkow.index(ACTIVE)

        entry_alias.delete(0, END)
        entry_alias.insert(0, parks[i].alias)

        entry_address.delete(0, END)
        entry_address.insert(0, parks[i].address)

        entry_category.delete(0, END)
        entry_category.insert(0, parks[i].category)

        entry_logo.delete(0, END)
        entry_logo.insert(0, parks[i].logo)

        # ZMIANA PRZYCISKU

        button_dodaj_park.config(text='Zapisz zmiany', command=lambda: zaktualizuj_park(i))

    def zaktualizuj_park(i):
        alias = entry_alias.get()
        address = entry_address.get()
        category = entry_category.get()
        logo = entry_logo.get()

        update_park(parks, i, alias, address, category, logo)
        messagebox.showinfo("Sukces", f"Zaktualizowano dane parku!")
        odswiez_liste_parkow()

        button_dodaj_park.config(text='Dodaj park', command=dodaj_park)

        entry_alias.delete(0, END)
        entry_address.delete(0, END)
        entry_category.delete(0, END)
        entry_logo.delete(0, END)
        entry_alias.focus()

    def usun_park():
        selection = listbox_lista_parkow.curselection()
        if not selection:
            messagebox.showwarning("Uwaga", "Wybierz park do usunięcia!")
            return

        i = listbox_lista_parkow.index(ACTIVE)
        park_alias = parks[i].alias

        if messagebox.askyesno("Potwierdzenie", f"Czy na pewno chcesz usunąć park: {park_alias}?"):
            remove_park(parks, i)
            messagebox.showinfo("Sukces", f"Usunięto park: {park_alias}")
            odswiez_liste_parkow()

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
            Label(popup, text=f"Współrzędne: {employee.coords[0]:.4f}, {employee.coords[1]:.4f}",
                  font=("Arial", 10)).pack(pady=5)

        map_widget.set_position(employee.coords[0], employee.coords[1])
        map_widget.set_zoom(17)

    def odswiez_liste_pracownikow():
        listbox_lista_pracownikow.delete(0, END)
        employee_list = show_employee(employees)
        for idx, employee in enumerate(employee_list):
            listbox_lista_pracownikow.insert(idx, employee)

    def dodaj_ogrodnika():
        name = entry_name.get()
        workplace = entry_workplace.get()
        birth = int(entry_birth.get())
        photo = entry_photo.get()

        add_employee(employees, name, workplace, birth, photo, map_widget)
        messagebox.showinfo("Sukces", f"Dodano ogrodnika: {name}")
        entry_name.delete(0, END)
        entry_workplace.delete(0, END)
        entry_birth.delete(0, END)
        entry_photo.delete(0, END)
        entry_name.focus()
        odswiez_liste_pracownikow()

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
        entry_birth.insert(0, employees[i].birth)

        entry_photo.delete(0, END)
        entry_photo.insert(0, employees[i].photo)

        # ZMIANA PRZYCISKU

        button_dodaj_ogrodnika.config(text='Zapisz zmiany', command=lambda: zaktualizuj_ogrodnika(i))

    def zaktualizuj_ogrodnika(i):
        name = entry_name.get()
        workplace = entry_workplace.get()
        birth = int(entry_birth.get())
        photo = entry_photo.get()

        update_employee(employees, i, name, workplace, birth, photo)
        messagebox.showinfo("Sukces", f"Zaktualizowano dane ogrodnika!")
        odswiez_liste_pracownikow()

        button_dodaj_ogrodnika.config(text='Dodaj ogrodnika', command=dodaj_ogrodnika)

        entry_name.delete(0, END)
        entry_workplace.delete(0, END)
        entry_birth.delete(0, END)
        entry_photo.delete(0, END)
        entry_name.focus()

    def usun_ogrodnika():
        selection = listbox_lista_pracownikow.curselection()
        if not selection:
            messagebox.showwarning("Uwaga", "Wybierz ogrodnika do usunięcia!")
            return

        i = listbox_lista_pracownikow.index(ACTIVE)
        employee_name = employees[i].name

        if messagebox.askyesno("Potwierdzenie", f"Czy na pewno chcesz usunąć ogrodnika: {employee_name}?"):
            remove_employee(employees, i)
            messagebox.showinfo("Sukces", f"Usunięto ogrodnika: {employee_name}")
            odswiez_liste_pracownikow()


    def filtruj_pracownikow():
        selection = listbox_lista_parkow.curselection()
        if not selection:
            return

        selected_text = listbox_lista_parkow.get(selection[0])
        park_alias = selected_text.split(" - ")[0].strip()
        park = get_park_by_alias(parks, park_alias)
        if not park:
            return

        listbox_lista_pracownikow.selection_clear(0, END)

        for idx, employee in enumerate(employees):
            if employee.workplace.lower() == park.alias.lower():
                listbox_lista_pracownikow.selection_set(idx)

        map_widget.set_position(park.coords[0], park.coords[1])
        map_widget.set_zoom(17)

    # DEFINICJA RAMEK

    ramka_lista_pracownikow = Frame(root, bg="green")
    ramka_lista_parkow = Frame(root, bg="green")
    ramka_uzytkownicy = Frame(root, bg="green")
    ramka_formularz_parkow = Frame(root, bg="green")
    ramka_formularz_pracownikow = Frame(root, bg="green")
    ramka_mapa = Frame(root)

    ramka_lista_pracownikow.grid(row=0, column=0)
    ramka_formularz_pracownikow.grid(row=0, column=1)

    ramka_uzytkownicy.grid(row=0, column=2)

    ramka_lista_parkow.grid(row=0, column=4)
    ramka_formularz_parkow.grid(row=0, column=3)

    ramka_mapa.grid(row=2, column=0, columnspan=5)

    # RAMKA FORMULARZ OGRODNIKOW

    label_form = Label(ramka_formularz_pracownikow, text="Wprowadź ogrodnika: ")
    label_form.grid(row=0, column=0, columnspan=2)

    label_name = Label(ramka_formularz_pracownikow, text="Imie: ")
    label_name.grid(row=1, column=0)

    label_workplace = Label(ramka_formularz_pracownikow, text="Przypisany obiekt: ")
    label_workplace.grid(row=2, column=0)

    label_birth = Label(ramka_formularz_pracownikow, text="Rok urodzenia: ")
    label_birth.grid(row=3, column=0)

    label_photo = Label(ramka_formularz_pracownikow, text="Zdjęcie: ")
    label_photo.grid(row=4, column=0)

    entry_name = Entry(ramka_formularz_pracownikow)
    entry_name.grid(row=1, column=1)

    entry_workplace = Entry(ramka_formularz_pracownikow)
    entry_workplace.grid(row=2, column=1)

    entry_birth = Entry(ramka_formularz_pracownikow)
    entry_birth.grid(row=3, column=1)

    entry_photo = Entry(ramka_formularz_pracownikow)
    entry_photo.grid(row=4, column=1)

    button_dodaj_ogrodnika = Button(ramka_formularz_pracownikow, text="Dodaj ogrodnika", command=dodaj_ogrodnika)
    button_dodaj_ogrodnika.grid(row=5, column=0, columnspan=2)


    #RAMKA UZYTKOWNICY

    button_pokaz_uzytkownika = Button(ramka_uzytkownicy, text="Pokaż użytkowników", command=okno_uzytkownik)
    button_pokaz_uzytkownika.grid(row=0, column=0)

    # RAMKA LISTA PRACOWNIKOW

    label_lista_pracownikow = Label(ramka_lista_pracownikow, text="Lista ogrodników")
    label_lista_pracownikow.grid(row=0, column=0, columnspan=3)

    listbox_lista_pracownikow = Listbox(ramka_lista_pracownikow, selectmode=MULTIPLE)
    listbox_lista_pracownikow.grid(row=1, column=0, columnspan=3)

    button_pokaz_szczegoly = Button(ramka_lista_pracownikow, text="Pokaż szczegóły", command=lambda: okno_ogrodnik())
    button_pokaz_szczegoly.grid(row=2, column=0)

    button_usun_pracownika = Button(ramka_lista_pracownikow, text="Usuń ogrodnika", command=usun_ogrodnika)
    button_usun_pracownika.grid(row=2, column=1)

    button_edytuj_pracownika = Button(ramka_lista_pracownikow, text="Edytuj ogrodnika", command=edytuj_ogrodnika)
    button_edytuj_pracownika.grid(row=2, column=2)

    # RAMKA FORMULARZ PARKOW I OGRODOW

    label_form = Label(ramka_formularz_parkow, text="Wprowadź park/ogród: ")
    label_form.grid(row=0, column=0, columnspan=2)

    label_alias = Label(ramka_formularz_parkow, text="Nazwa: ")
    label_alias.grid(row=1, column=0)

    label_adress = Label(ramka_formularz_parkow, text="Adres: ")
    label_adress.grid(row=2, column=0)

    label_type = Label(ramka_formularz_parkow, text="Typ: ")
    label_type.grid(row=3, column=0)

    label_logo = Label(ramka_formularz_parkow, text="Logo: ")
    label_logo.grid(row=4, column=0)

    entry_alias = Entry(ramka_formularz_parkow)
    entry_alias.grid(row=1, column=1)

    entry_address = Entry(ramka_formularz_parkow)
    entry_address.grid(row=2, column=1)

    entry_category = Entry(ramka_formularz_parkow)
    entry_category.grid(row=3, column=1, sticky=E)

    entry_logo = Entry(ramka_formularz_parkow)
    entry_logo.grid(row=4, column=1, sticky=E)

    button_dodaj_park = Button(ramka_formularz_parkow, text="Dodaj park/ogród", command=dodaj_park)
    button_dodaj_park.grid(row=5, column=0, columnspan=2, sticky=E)

    # RAMKA LISTA PARKOW I OGRODOW
    label_lista_parkow = Label(ramka_lista_parkow, text="Lista parków/ogrodów")
    label_lista_parkow.grid(row=0, column=0, columnspan=3)

    listbox_lista_parkow = Listbox(ramka_lista_parkow)
    listbox_lista_parkow.grid(row=1, column=0, columnspan=3)

    button_pokaz_szczegoly = Button(ramka_lista_parkow, text="Pokaż szczegóły", command=lambda: okno_park())
    button_pokaz_szczegoly.grid(row=2, column=0, sticky=E)

    button_usun_park = Button(ramka_lista_parkow, text="Usuń obiekt", command=usun_park)
    button_usun_park.grid(row=2, column=1, sticky=E)

    button_edytuj_park = Button(ramka_lista_parkow, text="Edytuj obiekt", command=edytuj_park)
    button_edytuj_park.grid(row=2, column=2, sticky=E)

    button_filtruj_pracownikow = Button(ramka_lista_parkow, text="Filtruj pracowników", bg="blue", command=filtruj_pracownikow)
    button_filtruj_pracownikow.grid(row=3, column=0, columnspan=2, sticky=E)

    # RAMKA MAPY

    map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1500, height=600, corner_radius=0)

    map_widget.set_position(52.0, 21.3)
    map_widget.set_zoom(6)
    map_widget.grid(row=0, column=0)

    root.mainloop()