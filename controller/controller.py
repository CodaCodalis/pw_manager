from model import model


class Controller:
    db = model.Database()

    def __init__(self):
        pass

    @classmethod
    def show_entries(cls):
        return cls.db.get_entries()

    @classmethod
    def add_entry(cls, name, password, url, note):
        ind = cls.get_last_index() + 1
        cls.db.set_entry(model.Password(ind, name, password, url, note))

    @classmethod
    def delete_entry(cls, ind):
        for i, password in enumerate(cls.db.get_entries()):
            if password.get_ind() == int(ind):
                del cls.db.get_entries()[i]

    @classmethod
    def get_last_index(cls):
        db = cls.db.get_entries()
        if len(db) < 1:
            return 1
        else:
            last_ind = db[len(db) - 1].get_ind()
            return last_ind

    @classmethod
    def update_entry(cls, ind, name, pw, url, note):
        entries_ind = 0
        pw = model.Password(int(ind), name, pw, url, note)
        cls.delete_entry(ind)
        for i, password in enumerate(cls.db.get_entries()):
            if password.get_ind() == int(ind):
                entries_ind = i
        cls.db.update_entry(entries_ind, pw)

    @classmethod
    def create_new_database(cls, name):
        cls.db.set_name(name)

    @classmethod
    def open_existing_database(cls, name):
        if cls.db.get_name() == name:
            return cls.db

    @classmethod
    def load_db(cls, name):
        cls.db.set_name(name)
        file = open(name, "r")
        while True:
            line = file.readline().rstrip('\n')
            if line == "":
                break
            item = line.split(";")
            entry = model.Password(int(item[0]), item[1], item[2], item[3], item[4])
            cls.db.set_entry(entry)
        file.close()
        return cls.db.get_name()

    @classmethod
    def save_db(cls, filename):
        db = cls.db.get_entries()
        file = open(filename, "a")
        for e in db:
            ln = str(e.get_ind()) + ";" + e.get_name() + ";" + e.get_pw() + ";" + e.get_url() + ";" + e.get_note() + "\n"
            file.write(ln)
        file.close()

    @classmethod
    def clear_file(cls, filename):
        file = open(filename, "r+")
        file.seek(0)
        file.truncate()
