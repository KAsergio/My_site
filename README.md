# Portfolio Personnel - Sergio ASSOGBA

Ce site web est mon portfolio personnel présentant mes projets, articles et contributions open source.

## Technologies utilisées

- Django
- Bootstrap
- HTML/CSS
- JavaScript
- Font Awesome
- AOS (Animate On Scroll)

## Fonctionnalités

- Page d'accueil avec présentation
- Section projets
- Blog d'articles
- Projets open source
- Formulaire de contact

## Installation

1. Cloner le dépôt :
```bash
git clone [URL_DU_REPO]
```

2. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

4. Configurer la base de données :
```bash
python manage.py migrate
```

5. Lancer le serveur de développement :
```bash
python manage.py runserver
```

## Structure du projet

- `templates/` : Templates HTML
- `static/` : Fichiers statiques (CSS, JS, images)
- `articles/` : Application pour le blog
- `projects/` : Application pour les projets
- `collaborative_projects/` : Application pour les projets open source

## Licence

Ce projet est sous licence MIT. 