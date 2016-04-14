import gi
import functions
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("trabalho1.glade")

window = builder.get_object("janela")
caixaTexto = builder.get_object("CaixaDeEntrada")
window.show_all()

functions.teste()
texto = caixaTexto.get_text()

builder.connect_signals({
    "gtk_main_quit": Gtk.main_quit,
    })

Gtk.main()