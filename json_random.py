import random
import json

def random_json():
    # on tire sort la longueur; attention
    # avec randint la borne supérieure est exclue
    length = random.randint(2, 6)
    # on tire au sort la liste
    # avec une compréhension 
    items = [ random.uniform(2, 5) for i in range(length) ]
    # on encode en JSON
    return json.dumps(items)

