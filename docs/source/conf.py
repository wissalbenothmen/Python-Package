import os
import sys
# Ajoutez cette ligne en haut du fichier
import sphinx_rtd_theme

# Modifiez la ligne suivante pour utiliser le thème
html_theme = 'sphinx_rtd_theme'

# Ajoutez cette ligne pour inclure le chemin du thème
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# Ajouter le chemin du projet pour que Sphinx puisse importer les modules
sys.path.insert(0, os.path.abspath('../'))

# Informations sur le projet
project = 'package_creation_tutorial'
copyright = '2024, wissal'
author = 'wissal'
release = '0.1.0'

# Extensions Sphinx
extensions = [
    'sphinx.ext.autodoc',  # Documentation automatique
    'sphinx.ext.viewcode',  # Lien vers le code source
    'sphinx.ext.napoleon',  # Support des docstrings Google/NumPy
    'sphinx.ext.githubpages',  # Publier sur GitHub Pages
]
