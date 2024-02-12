# CNI-watermark-generator
This small script allows French "Carte nationale d'Identité" (national identity card) holders to add a watermark to their ID so that they can track their id if their document gets online stolen.

Ce simple script permet aux détenteurs de la "Carte nationale d'identité" française d'ajouter un léger filigrane à leur document d'identité afin de tracer les copies qu'ils donnent s'il venait à être volé.
## English guide
### Getting started
#### Cloning the repo
```git clone https://github.com/oooooooorion/CNI-watermark-generator.git```

#### Installing dependencies 
First of all, make sure you have Python and Pip (comes with Python) installed on your machine.

Install dependencies (only pillow and pandas)

```pip install -r requirements.txt```
#### Setting the right font path (if not on macOS)
If you don't use Apple's macOS, edit the `arial_font_path` variable. I set it up for macOS. Replace the variable content with the path of your font of choice in ttf format (I chose Arial). If you don't know the path on your system, google it. 

/!\ Must be in ttf format
#### Placing your ID card on the right folder
Your input images must respect the following format :
 - input images MUST be in a .png format
 - height of the image MUST be 1000px
 - front image must be named exactly `CNI-recto-original.png` and back image `CNI-verso-original.png`

Place your files in the `original` folder

If you struggle to resize, convert or rename your ID scans, there is a script to resize (but not crop) your scans. Your scans must roughly have a 3:2 ratio. The script will convert if necessary to png, resize pics to a 1000px height and files will be correctly named.

```cd original/```

```python3 resize.py```
#### Making your script executable (on *NIX systems)
On macOS, BSD or GNU/Linux, please make your script executable.

```sudo chmod +x main.py```
### Running the script
Open a command line and type

```python3 main.py```
When prompt, enter the watermark text.

Et voilà !

## Guide en français
### Configuration 
#### Clonage du dépot 
```git clone https://github.com/pgchenu/CNI-watermark-generator.git```

#### Installation  des dépendances

Avant tout, soyez sûr d'avoir Python et Pip d'installés sur votre ordinateur (Pip vient normalement avec python)
Installez les dépendances.

```pip install -r requirements.txt```
#### Définir la bonne police d'écriture (si pas sur macOS)
Si vous n'utilisez pas macOS, éditez la variable `arial_font_path` dans `main.py`. Remplacez le contenu de la variable par le chemin vers la police de votre choix au format TTF sur votre ordinateur (J'ai personnellement choisi Arial). Si vous ne savez pas où trouver la variable du chemin vers la police Arial sur votre système, recherchez sur Google.

/!\ Dans tous les cas, la police d'écriture doit être au format .ttf
#### Déplacer le scan de votre CNI dans le bon dossier

Vos images de votre CNI doivent respecter impérativement les conditions suivantes :
 - les images originales doivent être au format PNG
 - la hauteur des images doit être de 1000 pixels
 - l'image recto doit être renommée en `CNI-recto-original.png` et le verso en `CNI-verso-original.png`.

Vous pouvez maintenant placer les images dans le dossier `original`

Si vous avez du mal à convertir, renommer et adapter à la bonne taille vos scan, un script est fait pour cela. Cependant, vos scans doivent être recadrés en un format 3:2 avant d'exécuter le script. 
Pour exécuter le script :

```cd original/```

```python3 resize.py```
#### Rendre le script exécutable (sur les systèmes *NIX)
Sur macOS, BSD ou encore GNU/Linux, rendez votre script exécutable

```sudo chmod +x main.py```
### Exécuter le script
Ouvrez votre terminal et lancez la commande suivante : 

```python3 main.py```

Quand le script vous le demande, tapez le nom du filigrane.

Et voilà !
