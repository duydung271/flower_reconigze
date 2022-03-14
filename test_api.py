import requests

url = 'http://127.0.0.1:8000/images/'

image_path = 'rose.jpg'
response = requests.post(url, files = {'file':open(image_path,'rb')})
print(response.text)