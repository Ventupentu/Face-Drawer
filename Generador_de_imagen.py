import requests
def generar_imagen(url,nombre_archivo):
  respuesta=requests.get(url)
  if respuesta.status_code==200:
    with open(nombre_archivo,'wb') as archivo:
      archivo.write(respuesta.content)
  else:
    print("Error al generar la imagen")
url='https://www.ikea.com/es/es/images/products/bravur-reloj-pared-baja-tension-negro__0633568_pe695902_s5.jpg' #The url of the jpg you want
nombre_archivo="Imagen.jpg"
