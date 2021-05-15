import qrcode
import numpy as np
from PIL import Image, ImageFont, ImageDraw

# CREO EL QR

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('323211b14abdab454cd')
qr.make(fit=True)

imgQR = qr.make_image(fill_color="black", back_color="white").convert('RGB')

size = imgQR.size

# CREO EL FONDO DONDE SE COLOCARA TODO

fondo = Image.new("L",(size[0],570),255)
fondo.paste(imgQR)
print(size[1])
# COMIENZO A AGREGAR EL TEXTO



posTexto = [30,350]
espaciadoDeTexto = [0,40]

# acerca de fuente
nombreFuente = "fonts/abel-regular.ttf"
sizeTexto = 16
sizeTitulo = 24
posTitulo = (100, 310)

def crearTexto(texto):
    fondoDraw.text(posTexto,text=texto,font=font)
    posTexto[0] += espaciadoDeTexto[0]
    posTexto[1] += espaciadoDeTexto[1]



fondoDraw = ImageDraw.Draw(fondo)
font = ImageFont.truetype(nombreFuente,sizeTexto)
fontTitulo = ImageFont.truetype(nombreFuente, sizeTitulo)

fondoDraw.text(posTitulo,text="Turno UNSAdA",font=fontTitulo)

crearTexto("Nombre: " + "Franco Bernaldo de Quirós")
crearTexto("Sede: " + "Baradero")
crearTexto("Edificio: " + "Edificio principal"+ " en " + "Araoz 1234")
crearTexto("Aula: " + "Edificio principal ")
crearTexto("Turno: el día " + "12/05/2021" + " a las " + "20:30" + "hs")
fondo.save("sample.png")

