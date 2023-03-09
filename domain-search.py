import requests

extensions = [".com", ".org", ".net", ".io", ".in", ".gov" ".tk"]

name = input("Enter a name: ")

for extension in extensions:
    url = "https://www." + name + extension
    try:
        response = requests.get(url)
        print("Response code for", url, ":", response.status_code)
    except Exception as e:
        print("Error:", e)
