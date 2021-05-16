from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
import logging
import qr
from flask import Flask, send_file,request

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
logging.debug("Log habilitad!")

def serve_pil_image(pil_img):
    tempFileObj = NamedTemporaryFile(mode='w+b',suffix='jpg')
    pilImage = open(pil_img,'rb')
    copyfileobj(pilImage,tempFileObj)
    pilImage.close()
    remove(pil_img)
    tempFileObj.seek(0,0)
    return send_file(tempFileObj, as_attachment=True, attachment_filename='TurnoUNSAdA.jpg')

# 323211b14abdab454cd

def salidaQR(hash_qr,data):
    respuesta = qr.crearQR(hash_qr, data)
    return serve_pil_image(respuesta)

@app.route('/<hash_qr>/<nombre>/<sede>/<edificio>/<direccion>/<aula>/<fecha>/<hora>')
def getMain(hash_qr,nombre,sede,edificio,direccion,aula,fecha,hora):
    data = {"nombre":nombre,"sede":sede,"edificio":edificio,"direccion":direccion, "aula" : aula, "fecha":fecha,"hora":hora}
    return salidaQR(hash_qr, data)

@app.route('/<hash_qr>', methods=['GET', 'POST'])
def main(hash_qr):
    data = request.get_json()
    return salidaQR(hash_qr, data)


    
