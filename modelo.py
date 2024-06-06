from datetime import datetime
import mysql.connector
import os
import json
from bson import json_util
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import sys 

puntos: dict[str, int] = {
    "A": 3,
    "B": 2,
    "C": 1,
    "D": 0
}
def obtener_puntos(respuesta: str) -> int:
    return puntos[respuesta]

def contador() -> int:
    precont: int = 0
    for filename in os.listdir('Perfiles_Exportados'):
        if filename.endswith('.json'):
            subcont: int = int(filename.split(".")[0].split("_")[-1])
            if precont < subcont:
                precont = subcont
            elif precont >= subcont:
                cont = precont
    cont = precont
    return cont

def crear_BDSQL():
    cnx = mysql.connector.connect(
        user='root',
        password='',
        host='localhost'
    )
    cursorSQL = cnx.cursor()
    cursorSQL.execute('CREATE DATABASE IF NOT EXISTS alzcare;')
    cursorSQL.execute("CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY '1234';")
    cursorSQL.execute("GRANT ALL PRIVILEGES ON alzcare.* TO 'admin'@'localhost';")
    cursorSQL.close()
    cnx.close()
  
def conectar_SQL():
    SERVIDOR = 'localhost'
    USUARIO = 'admin'
    CONTRASEÑA = '1234'
    DB  = 'alzcare'
    cnx = mysql.connector.connect(user=USUARIO,password=CONTRASEÑA,host=SERVIDOR,database=DB)
    cursorSQL = cnx.cursor()
    return cursorSQL,cnx

def desconectar_SQL(cnx,cursor):
    cnx.commit()
    cursor.close()
    cnx.close()

def crear_tablasSQL():
    cursorSQL, cnx = conectar_SQL()
    cursorSQL.execute("USE alzcare;")
    cursorSQL.execute("CREATE TABLE IF NOT EXISTS cuidador (ID INT UNSIGNED PRIMARY KEY,Nombre VARCHAR(225) NOT NULL,Apellido VARCHAR(225) NOT NULL,Telefono BIGINT(10) NOT NULL,Cedula BIGINT(10) NOT NULL,Formacion VARCHAR(225) NOT NULL,Usuario VARCHAR(225) NOT NULL,Contraseña VARCHAR(225) NOT NULL)")
    cursorSQL.execute("CREATE TABLE IF NOT EXISTS paciente (ID INT UNSIGNED PRIMARY KEY,ID_Cuidador INT UNSIGNED NOT NULL,Nombre VARCHAR(225) NOT NULL,Apellido VARCHAR(225) NOT NULL,Edad INT(3) NOT NULL,Telefono BIGINT(10) NOT NULL,Cedula BIGINT(10) NOT NULL,Nacimiento VARCHAR(225) NOT NULL,Procedencia VARCHAR(225) NOT NULL,Fase VARCHAR(225) NOT NULL,Escolaridad VARCHAR(225) NOT NULL,Mano_dominante VARCHAR(225) NOT NULL,Tiempo_Alz VARCHAR(225) NOT NULL,FOREIGN KEY (ID_Cuidador) REFERENCES cuidador(ID) ON UPDATE CASCADE ON DELETE CASCADE)")
    cursorSQL.execute("CREATE TABLE IF NOT EXISTS seguimiento (ID INT UNSIGNED PRIMARY KEY,ID_Paciente INT UNSIGNED NOT NULL,Fecha_Registro VARCHAR(225) NOT NULL,Pregunta_1 VARCHAR(1) NOT NULL,Pregunta_2 VARCHAR(1) NOT NULL,Pregunta_3 VARCHAR(1) NOT NULL,Pregunta_4 VARCHAR(1) NOT NULL,Pregunta_5 VARCHAR(1) NOT NULL,Pregunta_6 VARCHAR(1) NOT NULL,Pregunta_7 VARCHAR(1) NOT NULL,Pregunta_8 VARCHAR(1) NOT NULL,Pregunta_9 VARCHAR(1) NOT NULL,Pregunta_10 VARCHAR(1) NOT NULL,Puntos_Totales INT(3) NOT NULL,FOREIGN KEY (ID_Paciente) REFERENCES paciente(ID) ON UPDATE CASCADE ON DELETE CASCADE)")
    desconectar_SQL(cnx,cursorSQL)
    
def obtener_dataSQL():
    cursorSQL, cnx = conectar_SQL()
    listcui = []
    listpac = []
    listreg = []
    cuidador = "SELECT * FROM  cuidador"
    pacientes = "SELECT * FROM  paciente"
    seguimiento = "SELECT * FROM seguimiento"
    cursorSQL.execute(cuidador)
    resultado = cursorSQL.fetchall()    
    for i in resultado:
        diccui = {}
        diccui = {
            "ID": (i[0]),
            "Nombre": (i[1]),
            "Apellido": (i[2]),
            "Telefono": (i[3]),
            "Cedula": (i[4]),
            "Formacion": (i[5]),
            "Usuario": (i[6]),
            "Contraseña": (i[7])
            }
        listcui.append(diccui)       
    cursorSQL.execute(pacientes)
    resultado = cursorSQL.fetchall()
    for i in resultado:
            dicpac = {}
            dicpac = {
                "ID": (i[0]),
                "ID_Cuidador": (i[1]),
                "Nombre": (i[2]),
                "Apellido": (i[3]),
                "Edad": (i[4]),
                "Telefono": (i[5]),
                "Cedula": (i[6]),
                "Nacimiento": (i[7]),
                "Procedencia": (i[8]),                                             
                "Fase": (i[9]),
                "Escolaridad": (i[10]),
                "Mano_Dominante": (i[11]),
                "Tiempo_Alz": (i[12])
                }
            listpac.append(dicpac) 
    cursorSQL.execute(seguimiento)
    resultado = cursorSQL.fetchall()
    for i in resultado:
            dicreg = {}
            dicreg = {
                "ID": (i[0]),
                "ID_Paciente": (i[1]),
                "Fecha_Registro": (i[2]),
                "Pregunta_1": (i[3]),
                "Pregunta_2": (i[4]),
                "Pregunta_3": (i[5]),
                "Pregunta_4": (i[6]),
                "Pregunta_5": (i[7]),
                "Pregunta_6": (i[8]),
                "Pregunta_7": (i[9]),
                "Pregunta_8": (i[10]),
                "Pregunta_9": (i[11]),
                "Pregunta_10": (i[12]),
                "Puntos_Totales": (i[13])
                }
            listreg.append(dicreg) 
    desconectar_SQL(cnx,cursorSQL)
    return listcui, listpac, listreg

def añadir_cuidador(nombre: str, apellido: str,
                    telefono: int, cedula: int, formacion: str, usuario: str,contraseña: str, i: int
                   ) -> bool:
    '''Se ingresa un cuidador a la base de datos'''
    try:
        cursorSQL, cnxSQL = conectar_SQL()
        listdatareg = []
        listreg = ()
        listreg = (i,nombre,apellido,telefono,cedula,formacion,usuario,contraseña)
        listdatareg.append(listreg)
        cursorSQL.executemany("""INSERT INTO cuidador (ID, Nombre, Apellido, Telefono, Cedula, Formacion, Usuario, Contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", listdatareg)
        desconectar_SQL(cnxSQL,cursorSQL)
        return True
    except mysql.connector.errors.IntegrityError:
        cursorSQL, cnxSQL = conectar_SQL()
        listdatareg = []
        listreg = ()
        listreg = (i+1,nombre,apellido,telefono,cedula,formacion,usuario,contraseña)
        listdatareg.append(listreg)
        cursorSQL.executemany("""INSERT INTO cuidador (ID, Nombre, Apellido, Telefono, Cedula, Formacion, Usuario, Contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", listdatareg)
        desconectar_SQL(cnxSQL,cursorSQL)
        return True
    except: 
        print("Dato ingresado no valido")
        return False

def añadir_paciente(id_cuidador,
    nombre: str, apellido: str,
    edad: int, telefono: int, cedula: int, nacimiento: str, procedencia: str, fase: str, escolaridad: str, mano_dominante: str, tiempo_alz: str, i: int 
) -> bool:
    '''Se ingresa un paciente a la base de datos'''
    try:            
        cursorSQL, cnxSQL = conectar_SQL()
        listdatareg = []
        listus = ()        
        listus = (i,id_cuidador,nombre,apellido,edad,telefono,cedula,nacimiento,procedencia,fase,escolaridad,mano_dominante,tiempo_alz)
        listdatareg.append(listus)
        cursorSQL.executemany("""INSERT INTO paciente (ID, ID_Cuidador, Nombre, Apellido, Edad, Telefono, Cedula, Nacimiento, Procedencia, Fase, Escolaridad, Mano_dominante, Tiempo_Alz) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", listdatareg)
        desconectar_SQL(cnxSQL,cursorSQL)
        return True
    except mysql.connector.errors.IntegrityError:
        cursorSQL, cnxSQL = conectar_SQL()
        listdatareg = []
        listus = ()        
        listus = (i+1,id_cuidador,nombre,apellido,edad,telefono,cedula,nacimiento,procedencia,fase,escolaridad,mano_dominante,tiempo_alz)
        listdatareg.append(listus)
        cursorSQL.executemany("""INSERT INTO paciente (ID, ID_Cuidador, Nombre, Apellido, Edad, Telefono, Cedula, Nacimiento, Procedencia, Fase, Escolaridad, Mano_dominante, Tiempo_Alz) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", listdatareg)
        desconectar_SQL(cnxSQL,cursorSQL)
        return True
    except: 
        print("Dato ingresado no valido")
        return False

def añadir_respuestas(id,fecha,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,total,i):    
    '''Se ingresan las respuestas de las 10 preguntas en fio'''
    try:            
        cursorSQL, cnxSQL = conectar_SQL()
        listdatareg = []
        listus = ()        
        listus = (i,id,fecha,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,total)
        listdatareg.append(listus)
        cursorSQL.executemany("""INSERT INTO seguimiento (ID,ID_Paciente, Fecha_Registro, Pregunta_1, Pregunta_2, Pregunta_3, Pregunta_4, Pregunta_5, Pregunta_6, Pregunta_7, Pregunta_8, Pregunta_9, Pregunta_10, Puntos_Totales) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", listdatareg)
        desconectar_SQL(cnxSQL,cursorSQL)
        return True
    except mysql.connector.errors.IntegrityError: 
        cursorSQL, cnxSQL = conectar_SQL()
        listdatareg = []
        listus = ()        
        listus = (i+1,id,fecha,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,total)
        listdatareg.append(listus)
        cursorSQL.executemany("""INSERT INTO seguimiento (ID,ID_Paciente, Fecha_Registro, Pregunta_1, Pregunta_2, Pregunta_3, Pregunta_4, Pregunta_5, Pregunta_6, Pregunta_7, Pregunta_8, Pregunta_9, Pregunta_10, Puntos_Totales) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", listdatareg)
        desconectar_SQL(cnxSQL,cursorSQL)
        return True
    except: 
        print("Dato ingresado no valido")
        return False
    
def exportar_perfil(usuario):
    '''Exporta el perfil del usuario en formato json'''
    cursorSQL, cnx = conectar_SQL()
    direccion = (f"Perfiles_Exportados\Perfil_{contador()+1}.json")
    cursorSQL.execute("SELECT * FROM cuidador WHERE Usuario = '"+usuario+"'")
    resultado = cursorSQL.fetchall()
    diccui = []
    for i in resultado:
        cuidador = {
            "ID": (i[0]),
            "Nombre": (i[1]),
            "Apellido": (i[2]),
            "Telefono": (i[3]),
            "Cedula": (i[4]),
            "Formacion": (i[5]),
            "Usuario": (i[6]),
            "Contraseña": (i[7])
        }
        diccui.append(cuidador)
        
    cursorSQL.execute("SELECT * FROM paciente WHERE ID_Cuidador = '"+str(diccui[0]["ID"])+"'")
    resultado = cursorSQL.fetchall()
    dicpac = []
    for i in resultado:
        paciente = {
            "ID": (i[0]),
            "ID_Cuidador": (i[1]),
            "Nombre": (i[2]),
            "Apellido": (i[3]),
            "Edad": (i[4]),
            "Telefono": (i[5]),
            "Cedula": (i[6]),
            "Nacimiento": (i[7]),
            "Procedencia": (i[8]),                                             
            "Fase": (i[9]),
            "Escolaridad": (i[10]),
            "Mano_Dominante": (i[11]),
            "Tiempo_Alz": (i[12])
        }
        dicpac.append(paciente)
        
    cursorSQL.execute("SELECT * FROM seguimiento WHERE ID_Paciente = '"+str(dicpac[0]["ID"])+"'")
    resultado = cursorSQL.fetchall()
    dicrec = []
    for i in resultado:
        seguimiento = {
            "ID": (i[0]),
            "ID_Paciente": (i[1]),
            "Fecha_Registro": (i[2]),
            "Pregunta_1": (i[3]),
            "Pregunta_2": (i[4]),
            "Pregunta_3": (i[5]),
            "Pregunta_4": (i[6]),
            "Pregunta_5": (i[7]),
            "Pregunta_6": (i[8]),
            "Pregunta_7": (i[9]),
            "Pregunta_8": (i[10]),
            "Pregunta_9": (i[11]),
            "Pregunta_10": (i[12]),
            "Puntos_Totales": (i[13])       
        }
        dicrec.append(seguimiento)
        
    with open(direccion, 'w', encoding='utf-8') as file:
        json.dump({"Cuidador": diccui, "Paciente": dicpac, "Seguimiento": dicrec}, file, indent=3, ensure_ascii=False)
    desconectar_SQL(cnx,cursorSQL)
    return True

def importar_perfil(direccion):
    '''Importa el perfil del usuario en formato json'''
    with open(direccion, 'r', encoding='utf-8') as file:
        data = json.load(file)
    #try:
    listcui, listpac, listreg = obtener_dataSQL()
    cuidador = data["Cuidador"][0]
    paciente = data["Paciente"][0]
    seguimiento = data["Seguimiento"]
    x = len(listreg)
    y = len(listpac)
    z = len(listcui)
    añadir_cuidador(cuidador["Nombre"],cuidador["Apellido"],cuidador["Telefono"],cuidador["Cedula"],cuidador["Formacion"],cuidador["Usuario"],cuidador["Contraseña"], z)
    añadir_paciente(paciente["ID_Cuidador"],paciente["Nombre"],paciente["Apellido"],paciente["Edad"],paciente["Telefono"],paciente["Cedula"],paciente["Nacimiento"],paciente["Procedencia"],paciente["Fase"],paciente["Escolaridad"],paciente["Mano_Dominante"],paciente["Tiempo_Alz"], y)
    for i in seguimiento:
        añadir_respuestas(i["ID_Paciente"],i["Fecha_Registro"],i["Pregunta_1"],i["Pregunta_2"],i["Pregunta_3"],i["Pregunta_4"],i["Pregunta_5"],i["Pregunta_6"],i["Pregunta_7"],i["Pregunta_8"],i["Pregunta_9"],i["Pregunta_10"],i["Puntos_Totales"], x)
        x += 1
    return True
    #except:
    #    print("Error al importar perfil")
    #    return False

def id_paciente(usuario):
    '''Se obtiene el id del paciente'''
    cursorSQL, cnx = conectar_SQL()
    cursorSQL.execute("SELECT * FROM cuidador WHERE Usuario = '"+usuario+"'")
    resultado = cursorSQL.fetchall()
    for i in resultado:
        diccui = {}
        diccui = {
            "ID": (i[0]),
            "Nombre": (i[1]),
            "Apellido": (i[2]),
            "Telefono": (i[3]),
            "Cedula": (i[4]),
            "Formacion": (i[5]),
            "Usuario": (i[6]),
            "Contraseña": (i[7])
            }
    cursorSQL.execute("SELECT * FROM paciente WHERE ID_Cuidador = '"+str(diccui["ID"])+"'")
    resultado = cursorSQL.fetchall()
    listpac = []
    for i in resultado:
        dicpac = {}
        dicpac = {
            "ID": (i[0]),
            "ID_Cuidador": (i[1]),
            "Nombre": (i[2]),
            "Apellido": (i[3]),
            "Edad": (i[4]),
            "Telefono": (i[5]),
            "Cedula": (i[6]),
            "Nacimiento": (i[7]),
            "Procedencia": (i[8]),                                             
            "Fase": (i[9]),
            "Escolaridad": (i[10]),
            "Mano_Dominante": (i[11]),
            "Tiempo_Alz": (i[12])
            }
        listpac.append(dicpac)
    desconectar_SQL(cnx,cursorSQL)
    return listpac[0]["ID"]

class Cuidador:
    def __init__(self,listcui):
        self._listcui = listcui

    def get_listcui(self):
        return self._listcui
    
    def validar_usuario(self, usuario: str, contrasena: str) -> bool:
        for i in range(len(self._listcui)):
                if self._listcui[i]["Usuario"] == usuario and self._listcui[i]["Contraseña"] == contrasena:
                    return True
        return False

    def registro_cuidador(self,
            nombre: str, apellido: str,
            telefono: int, cedula: int, formacion: str, usuario: str, contraseña: str
            ) -> bool:
        self._listcui.append({"ID": len(self._listcui)+1, "Nombre": nombre, "Apellido": apellido, "Telefono": telefono, "Cedula": cedula, "Formacion": formacion, "Usuario": usuario, "Contraseña": contraseña})
        i = len(self._listcui)
        if añadir_cuidador(nombre,apellido,telefono,cedula,formacion,usuario,contraseña, i):
            return True
        else:
            return False
    
  
class Paciente:
    def __init__(self, listpac):
        self._listpac = listpac

    def get_listpac(self):
        return self._listpac
    
    def registro_paciente(self,
        nombre: str, apellido: str,
        edad: int, telefono: int, cedula: int, residencia: str, nacimiento: str, fase: str, estudio: str, dominancia: str, tiempoalz: str, listcui):
        ID_cuidador = listcui[-1]["ID"]
        self._listpac.append({"ID": len(self._listpac)+1, "ID_Cuidador": ID_cuidador , "Nombre": nombre, "Apellido": apellido, "Edad": edad, "Telefono": telefono, "Cedula": cedula, "Nacimiento": nacimiento, "Procedencia": residencia, "Fase": fase, "Escolaridad": estudio, "Mano_Dominante": dominancia, "Tiempo_Alz": tiempoalz})
        i = len(self._listpac)
        if añadir_paciente(ID_cuidador,nombre,apellido,edad,telefono,cedula,nacimiento,residencia,fase,estudio,dominancia,tiempoalz, i):
            return True
        else:
            return False
        
        
class Seguimiento:
    def __init__(self, listreg):
        self._listreg = listreg
    
    def get_listreg(self):
        return self._listreg
    
    def registro_seguimiento(self, id, fecha, p, puntaje):
        self._listreg.append({"ID": len(self._listreg)+1, "ID_Paciente": id, "Fecha_Registro": fecha, "Pregunta_1": p[0], "Pregunta_2": p[1], "Pregunta_3": p[2], "Pregunta_4": p[3], "Pregunta_5": p[4], "Pregunta_6": p[5], "Pregunta_7": p[6], "Pregunta_8": p[7], "Pregunta_9": p[8], "Pregunta_10": p[9], "Puntos_Totales": puntaje})
        i = len(self._listreg)
        if añadir_respuestas(id,fecha,p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],puntaje,i):
            return True
        else:
            return False
    
    def datos_histograma(self,id):
        fechas = []
        puntajes = []
        for i in range(len(self._listreg)):
            if self._listreg[i]["ID_Paciente"] == id:
                fechas.append(self._listreg[i]["Fecha_Registro"])
                puntajes.append(self._listreg[i]["Puntos_Totales"])
        return {"fechas": fechas, "puntajes": puntajes}

