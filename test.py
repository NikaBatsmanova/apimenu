import requests

payload = {"id": 9,
           "day": "Sunday",
           "breakfast": ["tea", "corn porridge"],
           "dinner": ["jelly", "potato soup", "meat with vegetables"],
           "lunch": ["apple juice", "burgers"]}
payload1 = {"id": 8}
r = requests.post("http://192.168.1.105:5000/menu", params=payload1)
print(r.text)
