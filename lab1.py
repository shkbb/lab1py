import requests

response = requests.get("https://api.quotable.io/random", verify=False)

if response.status_code == 200:
    quote = response.json()["content"]
    author = response.json()["author"]
    print(f'Цитата: "{quote}"\nАвтор: {author}')
    
    with open("quote.txt", "w") as file:
        file.write(f'Цитата: "{quote}"\nАвтор: {author}')
else:
    print(f"Не вдалося отримати цитату. Статус: {response.status_code}")
