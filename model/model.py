class Password:
    def __init__(self, ind=None, name=None, password=None, url=None, note=None):
        self.__ind = ind
        self.__name = name
        self.__password = password
        self.__url = url
        self.__note = note

    def __str__(self):
        return self.__ind + ";" + self.__name + ";" + self.__password + ";" + self.__url + ";" + self.__note

    def set_ind(self, ind):
        self.__ind = ind

    def set_name(self, name):
        self.__name = name

    def set_pw(self, password):
        self.__password = password

    def set_url(self, url):
        self.__url = url

    def set_note(self, note):
        self.__note = note

    def get_ind(self):
        return self.__ind

    def get_name(self):
        return str(self.__name)

    def get_pw(self):
        return str(self.__password)

    def get_url(self):
        return str(self.__url)

    def get_note(self):
        return str(self.__note)


class Database:
    __entries = list()

    def __init__(self, name=None, entry=None):
        self.__name = name
        self.__entry = entry

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return str(self.__name)

    def set_entry(self, entry):
        self.__entries.append(entry)

    def get_entries(self):
        return self.__entries

    def update_entry(self, ind, entry):
        self.__entries.insert(ind, entry)
