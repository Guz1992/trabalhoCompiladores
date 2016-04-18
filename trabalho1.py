import gi
import functions
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("trabalho1.glade")

window = builder.get_object("janela")
caixaTexto = builder.get_object("CaixaDeEntrada")
CaixaSaida = builder.get_object("CaixaDeSaida")
window.show_all()

def ConverterActSignal(self):
    texto = caixaTexto.get_text()   
    if functions.verificaParenteses(texto) == 0:
        convertido = functions.infixaParaPosfixa(texto)  
        CaixaSaida.set_text("".join(convertido))
    else:
        CaixaSaida.set_text("Expressão com erros nos parênteses!")

builder.connect_signals({
    "gtk_main_quit": Gtk.main_quit,
    "ConverterAct": ConverterActSignal,
    })
#teste

Gtk.main()