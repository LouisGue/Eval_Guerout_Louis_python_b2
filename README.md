# Eval_Python : API d'une stations de controle de vélos

## Prérequis

- Python 3.12
- Git

## Installation

```bash
git clone https://github.com/LouisGue/Eval_Guerout_Louis_python_b2.git
cd Eval_Guerout_Louis_python_b2
python3.12 -m venv .venv
source .venv/bin/activate # source\Scripts\activate pour windows
pip install -r requirements.txt
```

## Lancer l'API

```bash
uvicorn app.main:app --reload
```

L'API est disponible sur http://127.0.0.1:8000 et la documentation interactive sur http://127.0.0.1:8000/docs.

La base SQLite `stations.db` est créée automatiquement au premier lancement.

## Lancer les tests

J'ai pas eu le temps de finir, et je sais plus comment on fait une fixture
