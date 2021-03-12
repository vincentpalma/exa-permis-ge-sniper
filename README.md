# Script Examen Pratique/Théorique Genève
Bot qui vérifie les dates disponibles toutes les 10 secondes et peut modifier la date de son examen s'il y en a une disponible dans la fourchette choisie.

## Setup
- Installer python 3.8 avec pip : https://www.python.org/downloads/
- Cloner ce repo (bouton vert --> download archive) et extraire l'archive zip
- Ouvrir un terminal (chercher cmd.exe sous Windows) et se deplacer a l'emplacement du dossier a l'aide de la commande ```cd C:\Users\{votre chemin}\exa-permis-ge-sniper-master``` 
- Faites ```pip install -r requirements.txt```
- Télécharger la version adéquate du chromedriver selon votre version de Chrome (Paramètres -> A propos de chrome -> Version {Numéro de votre version}) :
  https://chromedriver.chromium.org/downloads
- Placer chromedriver.exe dans le même dossier que pratique.py
- Modifier les informations en haut du fichier pratique.py (avec un editeur de texte) en specifiant le mois, les jours, votre date de naissance votre numero de personne (il faut deja avoir payé et choisi une date)
- Lancer ```python pratique.py```

Ca ne sert a rien de laisser tourner h24, les gens se desistent le plus souvent en soiree/fin d'apres-midi.

## Issues
- Pour que le script fonctionne, il doit y avoir au moins 5 places disponibles (peu importe la date). Au moment ou j'ai initialement codé ca, ce n'était pas un probleme. Maintenant, oui (parfois) a cause du covid. Si vous modifiez l'algorithme pour enlever cette contrainte, un pull request est le bienvenu. En attendant, **une solution est de changer la ligne 41 en remplacant 5 par 1**, mais cela veut dire que si la premiere date disponible se trouve avant la fourchette choisie, le script ne continue pas a chercher.
