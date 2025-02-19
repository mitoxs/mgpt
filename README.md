# MGPT - Interface CLI pour Mistral AI

MGPT est un script Python permettant d'interagir avec l'API Mistral AI en ligne de commande. Il permet d'obtenir rapidement des réponses générées par l'IA directement dans le terminal.

![MGPT Screenshot](https://github.com/user-attachments/assets/90932c5a-e102-4538-8608-d237c8803786)

## 1️⃣ Obtenir un Accès à l'API Mistral

- Rendez-vous sur le site officiel : [Mistral AI API Keys](https://console.mistral.ai/api-keys/)
- Accédez à la section API Keys
- Cliquez sur **"Créer une clé"**

## 2️⃣ Installation

Suivez ces étapes pour installer et configurer MGPT :

```bash
sudo apt install python3
pip install mistralai
mkdir mistralgpt
ls
cd mistralgpt/
nano mgpt.py
```

Collez le script dans **mgpt.py**

Ou

wget https://github.com/mitoxs/mgpt/blob/main/mgpt.py

```bash
nano ~/.bashrc
export MISTRAL_API_KEY="VOTRE_API_KEY"
source ~/.bashrc
echo $MISTRAL_API_KEY
mgpt "salut !"
