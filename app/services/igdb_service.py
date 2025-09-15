import os
import requests, random


def get_random_games(limit=10):
    
    url = "https://api.igdb.com/v4/games"
    
    headers = {
        "Client-ID": os.getenv("IGDB_CLIENT_ID"),
        "Authorization": f"Bearer {os.getenv("IGDB_ACCESS_TOKEN")}"
        
    }
    
    max_offset = 10000
    offset = random.randint(0, max_offset)
    
    body = f"""
    fields name, summary, rating, cover.url;
    offset {offset};
    limit {limit};
    """
    
    response = requests.post(url, headers=headers, data=body)
    
    if response.status_code == 200:
        #data = response.json()
        #print(data)
        return response.json()
    
    else:
        print(f"Erro de requisição: {response.status_code} - {response.text}")
        return []


def get_best_rated_games(limit=100):
    
    url = "https://api.igdb.com/v4/games"
    
    headers = {
        "Client-ID": os.getenv("IGDB_CLIENT_ID"),
        "Authorization": f"Bearer {os.getenv("IGDB_ACCESS_TOKEN")}"
        
    }
    
    body = f"""
    fields name, summary, rating, cover.url;
    sort rating desc;
    limit {limit};
    """
    
    response = requests.post(url, headers=headers, data=body)
    
    if response.status_code == 200:
        #data = response.json()
        #print(data)
        return response.json()
    
    else:
        print(f"Erro de requisição: {response.status_code} - {response.text}")
        return []
    

