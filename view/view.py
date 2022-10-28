import os
import time
from os.path import exists

from controller import controller

prog_name = "PW-MANAGER 0.1"


def print_head(db_name=""):
    if len(db_name) > 0:
        db_name = " (" + db_name + ")"
    frame = len(prog_name + db_name) * 2
    print("=" * frame)
    print(f"{' ' * (frame // 4)}" + prog_name + db_name)
    print("=" * frame)


def end_program():
    exit()


class View:
    c = controller.Controller()

    def __init__(self):
        pass

    @classmethod
    def print_main_menu(cls):
        print_head()
        choices = ["1) Create new password database",
                   "2) Import an existing database from a file",
                   "3) Export an existing database to a file",
                   "4) End program",
                   ""]
        for choice in choices:
            print(choice)
        choice = input("What do you want to do? \n")
        cls.choose_main_menu(choice)

    @classmethod
    def print_sub_menu(cls, db_name=""):
        print_head(db_name)
        choices = ["1) Show existing passwords",
                   "2) Add a new password",
                   "3) Delete an existing password",
                   "4) Update an existing password",
                   "5) Back to main menu",
                   ""]
        for choice in choices:
            print(choice)
        choice = input("What do you want to do? \n")
        cls.choose_sub_menu(choice, db_name)

    @classmethod
    def choose_main_menu(cls, num):
        if num == "1":
            cls.set_db_name()
        elif num == "2":
            cls.load_db(),
        elif num == "3":
            cls.save_db(),
        elif num == "4":
            end_program()
        else:
            print("Please enter a valid number.\n")
            time.sleep(1)
        cls.print_main_menu()

    @classmethod
    def choose_sub_menu(cls, num, db_name):
        if num == "1":
            cls.show_pws()
        elif num == "2":
            cls.add_pw()
        elif num == "3":
            cls.delete_pw()
        elif num == "4":
            cls.update_pw()
        elif num == "5":
            cls.quit_sub_menu()
        else:
            print("Please enter a valid number.\n")
            time.sleep(1)
        cls.print_sub_menu(db_name)

    @classmethod
    def set_db_name(cls):
        name = input("Please enter the name of the database you want to create: ")
        cls.c.create_new_database(name)
        cls.print_sub_menu(name)

    @classmethod
    def load_db(cls):
        name = input("Please enter the filename of an existing database (directory: " + os.getcwd() + "): ")
        db_name = cls.c.load_db(name)
        cls.print_sub_menu(db_name)
        pass

    @classmethod
    def save_db(cls):
        filename = input("Please enter the filename of the database you want to save (directory: " + os.getcwd() + "): ")
        if exists(filename):
            key = input("File already exists. Overwrite? (y/n)")
            if key == "y":
                cls.c.clear_file(filename)
        cls.c.save_db(filename)
        print("Database successfully saved!")
        time.sleep(1)
        cls.print_main_menu()
        pass

    @classmethod
    def show_pws(cls):
        passwords = cls.c.show_entries()
        print("-" * 75)
        print(f"Index{' ' * 10}Name{' ' * 11}Password{' ' * 7}URL{' ' * 12}Note{' ' * 11}")
        print("-" * 75)
        for password in passwords:
            ind = str(password.get_ind()) + " " * (15 - len(str(password.get_ind())) - 1)
            name = password.get_name() + " " * (15 - len(password.get_name()) - 1)
            passwd = password.get_pw() + " " * (15 - len(password.get_pw()) - 1)
            url = password.get_url() + " " * (15 - len(password.get_url()) - 1)
            note = password.get_note() + " " * (15 - len(password.get_note()) - 1)
            print(f"{ind} {name} {passwd} {url} {note}")
        print("-" * 75)

    @classmethod
    def add_pw(cls):
        print("Please enter the required information: ")
        name = input("Name: ")
        password = input("Password: ")
        url = input("URL: ")
        note = input("Note: ")
        cls.c.add_entry(name, password, url, note)

    @classmethod
    def delete_pw(cls):
        cls.show_pws()
        ind = input("Enter the index of the entry you want to delete: ")
        cls.c.delete_entry(ind)

    @classmethod
    def update_pw(cls):
        cls.show_pws()
        ind = input("Enter the index of the entry you want to update: ")
        name = input("Name: ")
        password = input("Password: ")
        url = input("URL: ")
        note = input("Note: ")
        cls.c.update_entry(ind, name, password, url, note)

    @classmethod
    def quit_sub_menu(cls):
        cls.print_main_menu()
