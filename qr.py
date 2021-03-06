import qrcode
import numpy as np
from PIL import Image, ImageFont, ImageDraw


posInicioTexto = [30,350]
posTexto = [30,350]
espaciadoDeTexto = [0,40]

# acerca de fuente
nombreFuente = "fonts/abel-regular.ttf"
sizeTexto = 16
sizeTitulo = 24
posTitulo = (55, 310)


def crearTexto(fondoDraw, font, texto):
    fondoDraw.text(posTexto,text=texto,font=font)
    posTexto[0] += espaciadoDeTexto[0]
    posTexto[1] += espaciadoDeTexto[1]



def crearQR(textoQR, json):
    posTexto[0] = posInicioTexto[0]
    posTexto[1] = posInicioTexto[1]
    if(not isinstance(textoQR, str)):
        print("No es un string.")
        return None
# CREO EL QR    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(textoQR)
    qr.make(fit=True)

    imgQR = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    size = imgQR.size

# CREO EL FONDO DONDE SE COLOCARA TODO
    fondo = Image.new("L",(size[0],590),255)
    fondo.paste(imgQR)

# COMIENZO A AGREGAR EL TEXTO
    fondoDraw = ImageDraw.Draw(fondo)
    font = ImageFont.truetype(nombreFuente,sizeTexto)
    fontTitulo = ImageFont.truetype(nombreFuente, sizeTitulo)

    fondoDraw.text(posTitulo,text="Permiso acceso UNSAdA",font=fontTitulo)
    crearTexto(fondoDraw, font, "Nombre: " + json["nombre"])
    crearTexto(fondoDraw, font, "actividad: " + json["actividad"])
    crearTexto(fondoDraw, font, "Sede: " + json["sede"])
    crearTexto(fondoDraw, font, "Edificio: " + json["edificio"]+ " en " + json["direccion"])
    crearTexto(fondoDraw, font, "Aula: " + json["aula"])
    crearTexto(fondoDraw, font, "Permiso para día " + json["fecha"] + " a las " + json["hora"] + "hs")
    guardadoEn = "sample.png"
    fondo.save(guardadoEn)
    return guardadoEn