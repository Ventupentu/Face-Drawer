import requests

def generate_image(url, file_name):
  response = requests.get(url)
  if response.status_code == 200:
    with open(file_name, 'wb') as file:
      file.write(response.content)
  else:
    print("Error generating the image")
