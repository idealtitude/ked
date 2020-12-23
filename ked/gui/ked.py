import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

class Ked:
    def __init__(self, app_path, ufile=None):
        glade_layout = f'{app_path}/data/ked_layout.glade'
        self.builder = gtk.Builder()
        self.builder.add_from_file(glade_layout)

        win = self.builder.get_object("KedMain")
        win.connect("delete-event", gtk.main_quit)

        win.show()

    def echo(self, msg):
        print(f'Message: {msg}')


def start_ked(app_path, user_file=None):
    main = Ked(app_path)
    gtk.main()

