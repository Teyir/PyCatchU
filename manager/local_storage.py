from localStoragePy import localStoragePy


class LocalStorage:
    def __init__(self):
        super().__init__()
        self.localStorage = localStoragePy('fr.pycatchu', 'sqlite')

    def get_data(self, item):
        if self.localStorage.getItem(item=item) != "None":
            return self.localStorage.getItem(item=item)
        else:
            return False

    def set_data(self, item, value):
        self.localStorage.setItem(item=item, value=value)

    def remove_data(self, item):
        self.localStorage.removeItem(item=item)

    def clear_data(self):
        self.localStorage.clear()
