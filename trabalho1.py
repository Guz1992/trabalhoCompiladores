import gi
#importa a biblioteca de interface
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
# chama o controlador de interface
builder.add_from_file("trabalho1.glade")
# chama o arquivo xml do glade

window = builder.get_object("janela")
caixaTexto = builder.get_object("CaixaDeEntrada")
# cria uma variável que recebe a janela principal
window.show_all()
#mostra a janela principal e tudo que está dentro dela

texto = caixaTexto.get_text()

#recebe os signals criados no glade
builder.connect_signals({
    "gtk_main_quit": Gtk.main_quit,
    })

Gtk.main()
#instancia seu programa dentro da interface gtk