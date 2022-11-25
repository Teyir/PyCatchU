
# PyCatchU
![logo PyCatchU](https://github.com/Teyir/PyCatchU/blob/dev/assets/logo.png)

Projet Python pokédex B3 dév

Made with 🍆 by Thomas.T / Thomas.Gry / Axel.B / Valentin.B

## Installation

Pour installer cette application, il faut cloner ce repository puis excuser les commande `pip` suivante :
```bash
$ pip install requests
$ pip install customtkinter
$ pip install Pillow
$ pip install localStoragePy
```
Pour lancer ce programme vous devez exécuter avec python le fichier main.py 


## Librairies utilisée 
- [tkinter](https://docs.python.org/3/library/tkinter.html) Librairie **Instalée par default** d'interface graphique 
- [pillow](https://pillow.readthedocs.io/en/stable/) Librairie utilisée pour affiher des images dans l'interface graphique
- [customTkinter](https://github.com/TomSchimansky/CustomTkinter) Librairie graphique  de préfabriqués pour tkinter
- [localStoragePy](https://pypi.org/project/localStoragePy/) Librairie pour le local storage

Nous avons choisit d'utiliser Tkinter car c'est une librairie graphique compatible sur beaucoup de plateforme (Windows, OS X, Linux, etc.). Elle permet de créer des applications très simplement et entièrement personnalisable et de façon native en Python sans avoir de soucis de performance.

Par rapport à l'utilisation de customTkinter, nous l'avons choisit pour gagner du temps au niveau UI, ses préfabriqués pouvant être personnalisable à souhait et comblant nos besoin en terme d'UI.

LocalStoragePy nous permet de sauvegarder l'équipe lors de sa formation et un fichier sqlite nous permet de persister ces données pendant qua l'application est fermer 
