# Générateur de Grilles de Mots Mêlés

Cette application crée une grille de mots mêlés personnalisée en fonction des préférences de l'utilisateur. Les mots sont insérés dans une grille de taille configurable, et l'interface graphique affiche la grille avec des mots aléatoirement choisis et des lettres de remplissage.

---

## Fonctionnalités principales

1. **Chargement de listes de mots** :
   - Option pour utiliser différents types de mots :
     - Tous les mots.
     - Noms d'animaux.
     - Mots communs.
   - Chargement depuis des fichiers texte :
     - `dict.txt` : Dictionnaire complet.
     - `animaux.txt` : Liste des noms d'animaux.
     - `mots_comun.txt` : Liste des mots communs.

2. **Personnalisation de la grille** :
   - Taille configurable de la grille.
   - Nombre de mots à insérer configurable.
   - Filtrage des mots par longueur (supérieure à 4 lettres).

3. **Affichage graphique** :
   - Affichage de la grille et des mots insérés avec `Tkinter`.
   - Les mots sont affichés avec des couleurs aléatoires.
   - Emplacements vides remplis avec des lettres aléatoires.

4. **Placement des mots** :
   - Les mots sont insérés dans la grille dans des directions aléatoires :
     - Haut, bas, gauche, droite.
     - Diagonales.
   - Validation des emplacements pour éviter les conflits entre mots.

---

## Prérequis

1. **Python 3.8 ou supérieur**
2. **Bibliothèque nécessaire** :
   - `tkinter` (intégré dans Python).

3. **Fichiers nécessaires** :
   - `dict.txt` : Liste complète de mots.
   - `animaux.txt` : Liste des noms d'animaux.
   - `mots_comun.txt` : Liste des mots communs.

---

## Utilisation

### Étape 1 : Lancer le script
Exécutez le script avec Python :
```bash
python mots_meles.py

