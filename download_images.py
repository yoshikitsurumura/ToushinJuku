import requests

urls = {
    "https://i.imgur.com/4lPYfoq.jpg": "images/teacher_male.jpg",
    "https://i.imgur.com/Lr8yqIg.jpg": "images/teacher_female.jpg"
}

for url, path in urls.items():
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        with open(path, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded {url} to {path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")