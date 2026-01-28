# Projet_Python

# Git and PC - Collection de projets Python

Collection de petits projets et scripts Python variés, incluant des jeux, des outils de dessin et des expériences avec différentes bibliothèques.

## 📁 Structure du projet

### 📄 Fichiers principaux

#### Dessin et Géométrie

- **`Dessinetoiles.py`** - Outil interactif pour dessiner des formes géométriques avec des étoiles
  - Pyramides (normales, inversées, avec trous)
  - Carrés, rectangles, cercles (avec ou sans trous)
  - Utilise PIL pour l'image

- **`calculer aire hexagone.py`** - Calcul de l'aire d'un hexagone
  - Utilise Turtle pour le dessin
  - Formule : (3√3/2) × côté²

- **`créateur indentation.py`** - Générateur de code avec indentation automatique
  - Crée des boucles imbriquées en Python
  - Utile pour générer des structures de code complexes

#### Jeux et Graphiques

- **`Pygale balle qui rebondi.py`** - Simulation d'une balle qui rebondit
  - Utilise Pygame
  - Balle avec physique de gravité et collisions
  - Résolution 1000x600 pixels

- **`jeu tiktok ball escape.py`** - Jeu TikTok inspiré (fichier vide - à développer)

- **`jeux avec turtle.py`** - Suite d'expériences avec Turtle
  - Dessins interactifs
  - Contrôle de la couleur, taille du stylo
  - Mode normal et mode lent
  - Captures d'écran

#### Interface Tkinter

- **`Tkinter test button.py`** - Bouton qui grandit en réaction à l'interaction
  - Interface humoristique : "Veux-tu me donner 10 000€ ?"
  - Le bouton "Non" grandit en cliquant
  - Le bouton "Oui" reprend sa taille après validation

- **`Tkinter test button qui bouge.py`** - Bouton qui fuit à l'approche de la souris
  - Interface avec suivi de la souris
  - Bouton qui se déplace pour échapper au curseur
  - Résolution 1200x900 pixels

#### Utilitaires

- **`cestmonpote.py`** - Mini projet avec pyramides ASCII
  - Affichage de pyramides normales et inversées

- **`programme de sport.py`** - Générateur d'exercices aléatoires
  - Liste d'exercices de musculation/fitness
  - Nombre de répétitions aléatoire (1-20)
  - Exercices : pompes, tractions, squats, gainage, dips, etc.

### 📁 Sous-dossiers

#### `for os/`

Scripts pour la création de fichiers et dossiers :

- **`créateur_dossier.py`** - Crée des dossiers automatiquement
- **`créateur_fichier.py`** - Crée des fichiers automatiquement

#### `With Claude/`

Projets avancés développés avec assistance :

- **`déssin spacial.py`** - Dessin spatial/3D
- **`PNG to ASCII.py`** - Convertir une image PNG en texte ASCII
- **`PNG_to_ASCII_detailled.py`** - Version détaillée de la conversion PNG → ASCII
- **`pygame jeux tiktok ball escape.py`** - Jeu Pygame inspiré de TikTok (balle qui échappe)
- **`img_for_ascii/`** - Dossier contenant les images pour la conversion ASCII

## 🔧 Dépendances

Les projets utilisent les bibliothèques suivantes :

- `turtle` - Dessins interactifs (standard library)
- `PIL` (Pillow) - Manipulation d'images
- `pygame` - Jeux et graphiques 2D
- `tkinter` - Interfaces graphiques (standard library)
- `keyboard` - Capture des entrées clavier
- `math` - Calculs mathématiques (standard library)
- `random` - Nombres aléatoires (standard library)

## 🚀 Comment utiliser

### Exemple avec Dessinetoiles.py

```bash
python "Dessinetoiles.py"
# Suivre les instructions du menu pour choisir la forme
```

### Exemple avec le programme de sport

```bash
python "programme de sport.py"
# Affiche des exercices aléatoires avec nombre de répétitions
```

### Exemple avec les jeux Tkinter

```bash
python "Tkinter test button.py"
# Interface humoristique avec bouton interactif
```

## 📝 Notes

- Certains fichiers sont des expériences/brouillons
- Les noms sont en français (convention personnelle)
- Plusieurs projets utilisent des interfaces graphiques (Turtle, Tkinter, Pygame)
- Des projets sont des jeux ou des simulations
- Voir le dossier "With Claude/" pour des projets plus avancés

## 📅 Statut

Collection en cours de développement avec des projets variés de tous niveaux de complexité.
