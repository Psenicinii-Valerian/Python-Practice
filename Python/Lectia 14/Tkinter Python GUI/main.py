import tkinter as tk
# Tkinter este o bibliotecă standard de interfață grafică pentru limbajul de programare Python,
# oferind un set de instrumente pentru crearea și gestionarea aplicațiilor cu interfață grafică.
# tk in cazul dat este un alias sau o abreviere pentru modulul Tkinter din Python.

from tkinter import colorchooser
# colorchooser este un Modul care oferă clasa Chooser ca interfață către dialogul nativ de selectare a culorii.
# Clasa Chooser implementează o fereastră modală de selectare a culorii.


                                                # GUI Functions
# functiile care le scriem pentru elementele GUI de obicei se plaseaza deasupra codului de GUI
# *aceasta se face pentru comoditatea citirii codului ulterior
#                                               # Frame 1 Functions
def change_text_1():
    text = input_1.get()
    # input_1.get() - va returna textul care se afla in input_1
    label_1.config(text=text)
    # label_1.config(text=newTextValue) - metoda ce va modifica valoarea textului curent din label_1
    # in valoarea unui nou text setat/extras de undeva

def change_color_1():
    color = colorchooser.askcolor()[1]
    # Metoda principală utilizată din clasa Chooser este askcolor(), care deschide fereastra de dialog
    # și permite utilizatorului să selecteze o culoare.  Această metodă returnează o tuplă
    # care conține două elemente: o valoare de culoare în format RGB și codul hexazecimal asociat culorii selectate.
    if color:
        root.config(background=color)
        # root.config(background=color) - metoda ce va modifica valoarea culorii curente din fereastra principala(root)
        # in valoarea unei noi culori extrase de pe paleta de culori oferite de metoda colorchooser.askcolor()[1]
        # (*daca in aceasta fereastra principala root se contin alte elemente(divuri, inputuri, etc.), acestea nu se vor modifica)

                                                 # Frame 2 Functions
def change_text_2():
    text = input_2.get()
    label_2.config(text=text)

def change_color_2():
    color = colorchooser.askcolor()[1]
    if color:
        frame_2.config(background=color)
        # frame_2.config(background=color) - metoda ce va modifica valoarea culorii curente din <divul> frame_2

def reset():
    # in aceasta functie vom reseta toate valorile initiale ale label-urilor(textul),
    # a input-urilor(stergerea textului scris in cadrul acestora),
    # a root-ului(background color) si a <divului> frame_2(background color)
    label_1.config(text="Hello, GUI")
    input_text_1.set("")
    # input_text_1.set("") - setează valoarea variabilei input_text_1 la un șir vid (""),
    # ceea ce duce la ștergerea sau golirea textului din câmpul de intrare (Entry - *sau input) asociat cu această variabilă.
    input_text_2.set("")
    root.config(background="white")
    label_2.config(text="Click buttons below me")
    frame_2.config(background="white")


                                                    # GUI Elements
root = tk.Tk()
# root = tk.Tk() - Tkinter root este o instanță principală a clasei Tk din biblioteca Tkinter în Python,
# reprezentând fereastra principală a unei aplicații cu interfață grafică.
# exista o conventie, confirm careia fereastra principala se numeste in practica root sau app
# (respectiv nu este de dorit sa ii dam alte denumiri ferestrei noastre principale)

root.geometry("1920x720")
# root.geometry("500x300") - seteaza marimea ferestrei noastre(widthxheight)

# root.resizable(False, False)
# resizable(False, False) - nu ne permite sa schimbam dimensiunea ecranului

# root.resizable(False, True)
# root.resizable(False, True) - ne va permite as schimbam dimensiunea doar a inaltimii ferestrei

root.resizable(True, True)
# root.resizable(True, True) - ne permite sa schimbam ambele dimensiuni ale ferestrei

                                                    # Frame 1
frame_1 = tk.Frame(root, bg="white")
frame_1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
# tk.Frame() - Frame weste o clasă din biblioteca Tkinter în Python, folosită pentru a crea un container sau un cadru
# în care se pot plasa și organiza alte elemente de interfață grafică, precum butoane, etichete sau casete de text.
# cu alte cuvinte, este un fel de <div></div> din HTML
# frame_1 = tk.Frame(root, bg="white") - am indicat ca frame_1(divul) se va afla in root, si va avea background-color white

# frame_1.pack() - metoda care face sa apara <divul> in cadrul parintelui sau(in fereastra principala)
# fill=tk.BOTH - fill este un keyword care va lua in consideratie stilizarea atat pe insusi frame-ul nostru(frame_1), cat si pe intreaga fereastra

# Dacă expand=True, widget-ul (în acest caz, frame_1) va crește și se va extinde pentru a umple orice spațiu liber disponibil
# în containerul părinte pe axa specificată. Dacă containerul părinte este redimensionat (de exemplu, dacă fereastra principală este redimensionată),
# widget-ul va rămâne extins pe acea axă, încercând să mențină dimensiunea maximă.
# Dacă expand=False sau nu este specificat deloc, widget-ul va păstra dimensiunea sa naturală și nu se va extinde pentru
# a umple spațiul disponibil în containerul părinte.

# padx=10 - setam ca padding-ul pe axa x(atat dreapta cat si stanga) sa fie de 10px
# pady=10 - setam ca padding-ul pe axa y(atat sus cat si jos) sa fie de 10px
# padding-urile ne permit sa cream un chenar de 10px in jurul la frame_1 al nostru

label_1 = tk.Label(frame_1, text="Hello, GUI", font=("Arial", 17), bg="white")
label_1.grid(row=0, column=0)
label_1.pack(pady=20)
# tk.Label() - Label este o clasă în Tkinter Python, utilizată pentru a crea etichete (labels) care afișează text sau imagini
# într-un container al aplicației cu interfață grafică.

# label_1.grid(row=0, column=0) - această instrucțiune poziționeaza eticheta în containerul părinte utilizând sistemul de poziționare "grid"
# al bibliotecii Tkinter. Prin specificarea row=0 și column=0, eticheta va fi plasată în celula din coloana 0 și rândul 0 al grilei.
# Această metodă de poziționare permite aranjarea controlului (în acest caz, eticheta) într-o matrice de celule cu rânduri și coloane,
# oferind mai mult control asupra layout-ului interfeței grafice.

# label_1.pack() - metoda care face sa apara eticheta/label-ul label_1 in cadrul parintelui sau

input_text_1 = tk.StringVar()
# input_text_1 = tk.StringVar() - această linie de cod creează o variabilă specială de tip StringVar
# din biblioteca Tkinter din Python, numită input_text_1, care va fi utilizată pentru a păstra și gestiona textul
# introdus într-un câmp de intrare (Entry) din interfața grafică(intr-un input)

input_1 = tk.Entry(frame_1, textvariable=input_text_1, width=20, font=("Arial", 15))
input_1.pack()
# tk.Entry() - Entry este o clasă din biblioteca Tkinter din Python, care reprezintă un câmp de intrare (input field) în interfața grafică
# utilizand tk.Entry(frame_1) vom crea inputul input_1 in interiorul <divului> frame_1

# textvariable=input_text_1 - keyword care ne permite legarea(atasarea) variabilei input_text_1 de textul introdus în câmpul de intrare,
# astfel încât să putem obține și seta valoarea textului utilizând această variabilă.

# input_1.pack() - metoda care face sa apara inputul input_1 in cadrul parintelui sau(frame_1)

change_text_btn_1 = tk.Button(frame_1, text="Change Text", command=change_text_1)
change_text_btn_1.pack(pady=10)
# tk.Button()- Button este o clasă din biblioteca Tkinter din Python, care reprezintă un buton în interfața grafică,
# fiind utilizată pentru a crea un element interactiv ce poate executa acțiuni la apăsarea sa.
# utilizand tk.Button(frame_1) vom crea butonul change_text_btn_1 in interiorul <divului> frame_1

# pack(pady=10) - metoda care face sa apara butonul change_text_btn_1 in cadrul parintelui sau(frame_1) cu un padding sus, jos de 10px
# command=change_text_1 - command este un keyword care ne permite ca la apasare, butonul sa execute
# logica indicata in functia change_text_1() definita mai sus

change_color_btn_1 = tk.Button(frame_1, text="Change Color", command=change_color_1)
change_color_btn_1.pack(pady=10)

                                                    # Frame 2
frame_2 = tk.Frame(root, bg="white")
frame_2.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label_2 = tk.Label(frame_2, text="Click buttons below me", font=("Arial", 17), bg="white")
label_2.grid(row=0, column=0)
label_2.pack(pady=20)

input_text_2 = tk.StringVar()
input_2 = tk.Entry(frame_2, textvariable=input_text_2, width=20, font=("Arial", 15))
input_2.pack()

change_text_btn_2 = tk.Button(frame_2, text="Change Second Text", command=change_text_2)
change_text_btn_2.pack(pady=10)

change_color_btn_2 = tk.Button(frame_2, text="Change Color", command=change_color_2)
change_color_btn_2.pack(pady=10)

reset_btn = tk.Button(root, text="Reset", command=reset)
reset_btn.pack(pady=20)



root.mainloop()
# root.mainloop() - metoda care porneste aplicatia noastra(fereastra) (pe variabila root) si ramane vizibila pana nu o inchidem(apasam X)
# *lucreaza ca un fel de end program(ne porneste aplicatia cu codul scris deasupra ei), din acest motiv nu trebuie sa scriem nimic sub aceasta
# (codul scris sub aceasta functie nu va fi luat in consideratie de catre interpretator la lansarea programului)