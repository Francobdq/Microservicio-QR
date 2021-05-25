from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
import qr
from flask import Flask, send_file,request

app = Flask(__name__)

def serve_pil_image(pil_img):
    tempFileObj = NamedTemporaryFile(mode='w+b',suffix='jpg')
    pilImage = open(pil_img,'rb')
    copyfileobj(pilImage,tempFileObj)
    pilImage.close()
    remove(pil_img)
    tempFileObj.seek(0,0)
    return send_file(tempFileObj, as_attachment=True, attachment_filename='permisoUNSAdA.jpg')

# 323211b14abdab454cd

def salidaQR(hash_qr,data):
    respuesta = qr.crearQR(hash_qr, data)
    return serve_pil_image(respuesta)

@app.route('/<hash_qr>/<actividad>/<nombre>/<sede>/<edificio>/<direccion>/<aula>/<fecha>/<hora>')
def getMain(hash_qr,actividad, nombre,sede,edificio,direccion,aula,fecha,hora):
    data = {"actividad":actividad, "nombre":nombre,"sede":sede,"edificio":edificio,"direccion":direccion, "aula" : aula, "fecha":fecha,"hora":hora}
    return salidaQR(hash_qr, data)


@app.route('/<hash_qr>/<actividad>/<nombre>/<sede>/<edificio>/<direccion>/<aula>/<fecha_hora>')
def iqrCorto(hash_qr,actividad, nombre,sede,edificio,direccion,aula,fecha_hora):
    fecha = ""
    hora = ""

    if(len(fecha_hora)== 29):
        fecha = fecha_hora[8:10] + fecha_hora[4:8] + fecha_hora[:4]
        hora = fecha_hora[11:16]

    data = {"actividad":actividad, "nombre":nombre,"sede":sede,"edificio":edificio,"direccion":direccion, "aula" : aula, "fecha":fecha,"hora":hora}
    return salidaQR(hash_qr, data)

@app.route('/')
def indexMain():
    return "no hay nada que ver, accede a /hash_qr/actividad/nombre/sede/edificio/direccion/aula/fecha/hora"

    
