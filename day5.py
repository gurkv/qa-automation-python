import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

assert response.status_code == 200

data = response.json()

print(data["title"])

response_404 = requests.get("https://jsonplaceholder.typicode.com/posts/9999")
assert response_404.status_code == 404

