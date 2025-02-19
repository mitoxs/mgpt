#!/usr/bin/env python3

import os
import sys
from mistralai import Mistral

def ask_mistral(query):

    prompt = "Répond en Français : "
   
    api_key = os.getenv("MISTRAL_API_KEY")

    if api_key is None:
        raise ValueError("La clé API MISTRAL_API_KEY n'a pas été trouvée dans les variables d'environnement.")

    model = "mistral-large-latest"  

    client = Mistral(api_key=api_key)

    try:
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt + query  
                }
            ]
        )
        
        return chat_response.choices[0].message.content

    except Exception as e:
        return f"Erreur lors de l'appel à l'API : {str(e)}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Veuillez entrer une question après 'mgpt'. Par exemple: mgpt '4+4'")
        sys.exit(1)

    query = " ".join(sys.argv[1:])  

    result = ask_mistral(query)

    print(result)
