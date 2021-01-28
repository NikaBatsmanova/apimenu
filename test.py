import requests

payload = {"id": 9,
           "day": "Sunday",
           "breakfast": ["tea", "corn porridge"],
           "dinner": ["jelly", "potato soup", "meat with vegetables"],
           "lunch": ["apple juice", "burgers"]}
payload1 = {"id": 7}
r = requests.delete("http://127.0.0.1:5000/menu", data=payload1)
print(r.text)
