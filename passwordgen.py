import random
import string
from tkinter import *

# création de la fenêtre
app = Tk()
app.title("Générateur de Mots de Passe")
app.geometry("360x480") # dimension de la fenêtre
app.configure(bg='#1e1e1e') # couleur du fond de la fenêtre
app.resizable(False, False) # permet de ne pas pouvoir redimesionner la fenêtre

# variable pour stocker le mot de passe et les options
longueur_var = IntVar(value=12)
majuscules_var = BooleanVar(value=True)
minuscules_var = BooleanVar(value=True)
chiffres_var = BooleanVar(value=True)
symboles_var = BooleanVar(value=True)
mot_de_passe_var = StringVar(value="")

# dictionnaire de styles des boutons
btn_primary = {"bg": "#ff9f0a", "fg": "white", "activebackground": "#cc7f08", "activeforeground": "white", "bd": 0, "font": ('Arial', 11, 'bold')}
btn_sec = {"bg": "#333333", "fg": "white", "activebackground": "#555555", "activeforeground": "white", "bd": 0, "font": ('Arial', 10)}
style_check = {"bg": "#1e1e1e", "fg": "white", "activebackground": "#1e1e1e", "activeforeground": "white", "selectcolor": "#333333", "font": ('Arial', 10), "anchor": "w"}

# affichage du mot de passe en haut de la fenêtre
champ_mdp = Entry(app, textvariable=mot_de_passe_var, font=("Arial", 14), bg="#2d2d2d", fg="#ff9f0a", bd=0, justify="center")
champ_mdp.pack(fill=X, padx=20, pady=(20, 5), ipady=8)

label_force = Label(app, text="", bg="#1e1e1e", font=('Arial', 9, 'bold'))
label_force.pack(pady=(0, 10))

# fonction pour les boutons
def evaluer_force(longueur):
    nb_options = sum([majuscules_var.get(), minuscules_var.get(), chiffres_var.get(), symboles_var.get()])
    if longueur < 10 or nb_options < 2:
        label_force.config(text="Force : Faible", fg="#ff453a")
    elif longueur < 14 or nb_options < 3:
        label_force.config(text="Force : Moyenne", fg="#ff9f0a")
    else:
        label_force.config(text="Force : Forte", fg="#30d158")

def generer():
    caracteres = ""
    if majuscules_var.get():
        caracteres += string.ascii_uppercase
    if minuscules_var.get():
        caracteres += string.ascii_lowercase
    if chiffres_var.get():
        caracteres += string.digits
    if symboles_var.get():
        caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not caracteres:
        mot_de_passe_var.set("Coche au moins 1 option !")
        label_force.config(text="")
        return

    longueur = longueur_var.get()
    mdp = "".join(random.choice(caracteres) for _ in range(longueur))
    mot_de_passe_var.set(mdp)
    evaluer_force(longueur)

def copier():
    mdp = mot_de_passe_var.get()
    if mdp and mdp != "Coche au moins 1 option !":
        app.clipboard_clear()
        app.clipboard_append(mdp)
        btn_copier.config(text="Copié !")
        app.after(1500, lambda: btn_copier.config(text="Copier dans le presse-papier"))

# création des boutons
btn_copier = Button(app, text="Copier dans le presse-papier", **btn_sec, command=copier)
btn_copier.pack(fill=X, padx=20, pady=(0, 15), ipady=4)

Label(app, text="Longueur du mot de passe :", bg="#1e1e1e", fg="white", font=('Arial', 10, 'bold')).pack(anchor="w", padx=20)
curseur = Scale(app, from_=6, to=32, orient=HORIZONTAL, variable=longueur_var, bg="#1e1e1e", fg="white", highlightthickness=0, troughcolor="#333333", activebackground="#ff9f0a")
curseur.pack(fill=X, padx=20, pady=(0, 15))

frame_options = Frame(app, bg="#1e1e1e")
frame_options.pack(fill=X, padx=20, pady=5)

Checkbutton(frame_options, text="Majuscules (A-Z)", variable=majuscules_var, **style_check).pack(fill=X, pady=2)
Checkbutton(frame_options, text="Minuscules (a-z)", variable=minuscules_var, **style_check).pack(fill=X, pady=2)
Checkbutton(frame_options, text="Chiffres (0-9)", variable=chiffres_var, **style_check).pack(fill=X, pady=2)
Checkbutton(frame_options, text="Symboles (!@#$)", variable=symboles_var, **style_check).pack(fill=X, pady=2)

Button(app, text="GÉNÉRER LE MOT DE PASSE", **btn_primary, command=generer).pack(fill=X, padx=20, pady=20, ipady=8)

# génère un mot de passe au lancement
generer()

app.mainloop()